# Local Slides RAG

This repository contains only the minimal local RAG app and the indexed Markdown chunks needed to run it.

It does not include the original Docling project, raw PDFs, slides, images, extracted assets, or Chroma database files.

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

## Notes

- The app builds Chroma locally in `rag_app/.chroma/`.
- `rag_app/.chroma/`, logs, and Python caches are intentionally ignored by Git.
- The default model is `qwen3:1.7b` because it is light enough for an 8GB RAM machine.
- Arabic questions work in retrieval, but answer generation quality depends on the local Ollama model.
