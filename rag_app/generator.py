from __future__ import annotations

import ollama
import re

from config import OLLAMA_MODEL
from retriever import SearchResult


class OllamaUnavailable(RuntimeError):
    pass


def strip_thinking(text: str) -> str:
    return re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL | re.IGNORECASE).strip()


def format_context(results: list[SearchResult]) -> str:
    blocks = []
    for index, result in enumerate(results, start=1):
        source_file = result.metadata.get("source_file", "unknown")
        topics = result.metadata.get("topics", "")
        blocks.append(
            "\n".join(
                [
                    f"[Source {index}]",
                    f"chunk_id: {result.chunk_id}",
                    f"source_file: {source_file}",
                    f"topics: {topics}",
                    result.text[:3500],
                ]
            )
        )
    return "\n\n---\n\n".join(blocks)


def contains_arabic(text: str) -> bool:
    return bool(re.search(r"[\u0600-\u06FF]", text))


def answer_question(question: str, results: list[SearchResult], model: str = OLLAMA_MODEL) -> str:
    if not results:
        return "لا توجد مقاطع مسترجعة كافية للإجابة عن السؤال."

    language_instruction = (
        "السؤال عربي. يجب أن تكون الإجابة بالعربية الفصحى الواضحة، مع إبقاء المصطلحات العلمية الإنجليزية كما هي عند الحاجة."
        if contains_arabic(question)
        else "The question is in English. Answer in clear English."
    )

    prompt = f"""
أنت مساعد RAG للمواد التعليمية المستخرجة من Slides.

قواعد إلزامية:
- {language_instruction}
- أجب اعتماداً على السياق المرفق فقط.
- إذا لم تجد الدليل الكافي، قل بوضوح: "المعلومات المتاحة في المواد لا تكفي للإجابة بثقة."
- لا تخترع مصادر أو أرقاماً غير موجودة في السياق.
- إذا كانت المعادلات أو الرموز في السياق مشوشة بسبب OCR، اشرح المفهوم ولا تثبت صيغة رياضية غير واضحة.
- لا تعرض خطوات التفكير الداخلية أو أي وسوم مثل <think>.
- استخدم البنية التالية فقط:
  1. الإجابة
  2. الدليل من السياق
  3. المصادر
- لا تكرر الإجابة بعد قسم المصادر.

السؤال:
{question}

السياق:
{format_context(results)}
""".strip()

    try:
        response = ollama.chat(
            model=model,
            messages=[
                {
                    "role": "system",
                    "content": "You answer strictly from retrieved course context and cite source numbers.",
                },
                {"role": "user", "content": prompt},
            ],
            options={"temperature": 0.2, "num_ctx": 4096},
        )
    except Exception as exc:
        raise OllamaUnavailable(
            "Ollama is not reachable. Start it with `ollama serve`, then pull the model with "
            f"`ollama pull {model}`."
        ) from exc

    return strip_thinking(response["message"]["content"])
