from __future__ import annotations

import html

import streamlit as st

from config import DEFAULT_TOP_K, OLLAMA_MODEL, TOPIC_OPTIONS
from generator import OllamaUnavailable, answer_question
from indexer import build_index, index_status
from retriever import search


st.set_page_config(page_title="Slides RAG", page_icon=":books:", layout="wide")

st.title("Slides RAG")
st.caption("تطبيق RAG محلي فوق المواد المستخرجة من Slides/Output.")


def get_status() -> dict[str, object]:
    try:
        return index_status()
    except Exception as exc:
        return {"error": str(exc), "indexed_count": 0, "manifest_exists": False}


def render_source_card(index: int, result) -> None:
    metadata = result.metadata
    source_file = html.escape(str(metadata.get("source_file", "unknown")))
    chunk_id = html.escape(str(result.chunk_id))
    topics = html.escape(str(metadata.get("topics", "")))
    confidence = html.escape(str(metadata.get("confidence", "")))
    score = f"{result.score:.3f}"

    st.markdown(
        f"""
<div style="border:1px solid rgba(128,128,128,.35); border-radius:8px; padding:12px; margin:0 0 12px 0;">
  <div style="font-weight:700; margin-bottom:8px;">Source {index}</div>
  <table style="width:100%; border-collapse:collapse; font-size:0.92rem;">
    <tr><td style="width:95px; color:#8b949e;">File</td><td><code>{source_file}</code></td></tr>
    <tr><td style="color:#8b949e;">Chunk</td><td><code>{chunk_id}</code></td></tr>
    <tr><td style="color:#8b949e;">Topic</td><td><code>{topics}</code></td></tr>
    <tr><td style="color:#8b949e;">Confidence</td><td><code>{confidence}</code></td></tr>
    <tr><td style="color:#8b949e;">Score</td><td><code>{score}</code></td></tr>
  </table>
</div>
""",
        unsafe_allow_html=True,
    )
    with st.container(border=True):
        st.markdown(result.text[:1200])


with st.sidebar:
    st.header("Settings")
    topic = st.selectbox("Topic filter", TOPIC_OPTIONS, index=0)
    top_k = st.slider("Retrieved chunks", min_value=3, max_value=15, value=DEFAULT_TOP_K)
    st.text_input("Ollama model", value=OLLAMA_MODEL, key="ollama_model")

    if st.button("Show index status"):
        st.json(get_status())

    if st.button("Rebuild index"):
        with st.spinner("Building local Chroma index..."):
            st.json(build_index(force=True))

    if st.button("Clear chat"):
        st.session_state.messages = []
        st.rerun()

status = get_status()
if status.get("error"):
    st.error(f"Index status error: {status['error']}")
elif not status["manifest_exists"] or status["indexed_count"] == 0:
    st.warning("الفهرس غير مبني بعد. استخدم الزر في الشريط الجانبي أو شغّل: python rag_app/indexer.py --build")
else:
    st.success(f"Index ready: {status['indexed_count']} chunks in `{status.get('collection', 'slides_chunks_v1')}`.")

question = st.chat_input("اسأل عن مواد الساتلايت، الموبايل، الذكاء الاصطناعي، أو الامتحانات...")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        try:
            with st.spinner("Retrieving relevant chunks..."):
                results = search(question, top_k=top_k, topic=topic)
        except Exception as exc:
            results = []
            answer = (
                "Retrieval failed. Build the index first with `python rag_app/indexer.py --build`.\n\n"
                f"Error: `{exc}`"
            )
        else:
            if not results:
                answer = "لم أجد مقاطع مناسبة في الفهرس لهذا السؤال. جرّب إزالة فلتر الموضوع أو إعادة بناء الفهرس."
            else:
                try:
                    with st.spinner("Generating answer with Ollama..."):
                        answer = answer_question(question, results, model=st.session_state.ollama_model)
                except OllamaUnavailable as exc:
                    answer = str(exc)

        st.markdown(answer)

        if results:
            with st.expander("Retrieved sources", expanded=True):
                for index, result in enumerate(results, start=1):
                    render_source_card(index, result)

    st.session_state.messages.append({"role": "assistant", "content": answer})
