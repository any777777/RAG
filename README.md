# Local Slides RAG

This repository contains only the minimal local RAG app and the indexed Markdown chunks needed to run it.



## What Is Included

- `rag_app/`: Python Streamlit RAG app.
- `data/rag-chunks/`: Markdown chunks used as the retrieval corpus.
- `requirements.txt`: Python dependencies.
- `run_rag_app.ps1`: Windows helper script.

## Local Setup

Install dependencies:

```powershell
pip install -r requirements.txt
```

Install Ollama, then pull the default small model:

```powershell
ollama serve
ollama pull qwen3:1.7b
```

## Build The Vector Index

```powershell
python rag_app/indexer.py --build
```

Expected current count:

```text
3101 chunks
```

Check status:

```powershell
python rag_app/indexer.py --status
```

## Run The App

```powershell
streamlit run rag_app/app.py
```

Then open:

```text
http://localhost:8501
```

On Windows you can also run:

```powershell
powershell -ExecutionPolicy Bypass -File rag_app/run_rag_app.ps1
```

## Smoke Tests

Test indexing and retrieval:

```powershell
python rag_app/smoke_test.py
```

Test retrieval plus Ollama generation:

```powershell
python rag_app/smoke_test.py --with-ollama
```
## كيف تسحبه و تشغله عندك مباشرة 
بس اعمل copy و paste لهاي جوى الterminal 
ملاحظة افتح الterminal من جوى الfolder تبع المشروع 
```powershell
git clone https://github.com/any777777/RAG.git
cd RAG
pip install -r requirements.txt
ollama serve
ollama pull qwen3:1.7b
python rag_app/indexer.py --build
streamlit run rag_app/app.py
```
بعدين رح يفتح معك هون 
```text
http://localhost:8501
```
لازم يكون مثبت عندك 
- Python مثبت.
- Ollama مثبت.
- اتصال إنترنت في أول تشغيل لتحميل:
  - نموذج Ollama `qwen3:1.7b`
  - نموذج embeddings من Hugging Face.
- بعد أول بناء للفهرس، التطبيق يعمل محلياً من `data/rag-chunks`.
و غالبا انهم عندك 
## Notes

- The app builds Chroma locally in `rag_app/.chroma/`.
- `rag_app/.chroma/`, logs, and Python caches are intentionally ignored by Git.
- The default model is `qwen3:1.7b` because it is light enough for an 8GB RAM machine.
- Arabic questions work in retrieval, but answer generation quality depends on the local Ollama model.
