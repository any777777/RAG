# Markdown RAG Chat for Windows

Local desktop RAG application that indexes one Markdown file directly, stores embeddings in a persistent local ChromaDB database, and answers questions only from retrieved Markdown chunks using Gemini Flash.

## What it does

- Lets the user choose a single local `.md` or `.markdown` file.
- Reads the Markdown file directly. No OCR. No PDF processing.
- Cleans and chunks the Markdown text with configurable chunk size and overlap.
- Generates embeddings with Gemini and stores them in a persistent local ChromaDB collection.
- Provides a Windows desktop chat UI built with Tkinter.
- Answers only from retrieved chunks and returns chunk-based citations with every answer.
- Says `The information is not available in the source.` when the retrieved context does not support the answer.

## Project structure

```text
.
|-- .env
|-- build.ps1
|-- MarkdownRAGChat.spec
|-- README.md
|-- requirements.txt
|-- run_app.py
`-- app
    |-- __init__.py
    |-- config.py
    |-- gemini_client.py
    |-- markdown_processor.py
    |-- models.py
    |-- rag_service.py
    |-- ui.py
    `-- vector_store.py
```

## Runtime storage

- Persistent ChromaDB path: `%LOCALAPPDATA%\MarkdownRAGChat\chroma`
- App settings and manifest: `%LOCALAPPDATA%\MarkdownRAGChat`

The vector database persists between runs of both the Python app and the packaged `.exe`.

## Prerequisites

- Windows 10 or Windows 11
- Python 3.12 or newer installed and available on `python`
- Internet access for Gemini API calls

## Development run

1. Open PowerShell in the project folder.
2. Install dependencies:

```powershell
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

3. Start the desktop app:

```powershell
python run_app.py
```

## How to use the app

1. Click `Browse...` and choose a Markdown file.
2. Adjust `Chunk size`, `Overlap`, and `Top-k` if needed.
3. Click `Build / Rebuild DB`.
4. After the build completes, enter a question and click `Send`.
5. Read the answer and the citations shown under it.

## Windows `.exe` build

Run the build script from PowerShell:

```powershell
.\build.ps1
```

Build output:

- The script creates an isolated `.venv-build` environment for packaging.
- Executable: `dist\MarkdownRAGChat.exe`
- `.env` is copied next to the `.exe`
- `README.md` is copied into `dist`

You can run the packaged app by launching `dist\MarkdownRAGChat.exe`.

## Notes about the Gemini API key

- `.env` is already initialized with the provided key:
- هذا الapi الي يفضل انته تحط واحد من عندك احسن

```env
API_KEY="AIzaSyAYWTOE5H7HWq9DLbUnxBjPuD-Wcv11LQ8"
```

- The app also maps `API_KEY` to `GEMINI_API_KEY` automatically at startup.

## Grounding behavior

- The app retrieves the top-k most relevant chunks from the local Chroma collection.
- Gemini Flash receives only the retrieved chunk context plus recent chat history.
- The answer generator is instructed to use only that context.
- If the context does not support the answer, the app returns:

```text
The information is not available in the source.
```

## Troubleshooting

- If you see a `429 RESOURCE_EXHAUSTED` error while building the database, Gemini has rate-limited embedding requests for the current API key.
- The app now retries automatically and respects Gemini retry delays when possible.
- If the limit is still exceeded, wait a little and run `Build / Rebuild DB` again, or enable billing in Google AI Studio for higher quota.

## Constraints intentionally enforced

- No OCR
- No PDF support
- No web upload
- No accounts or login
- No cloud deployment
- No Docker
- No authentication
- Markdown is the only knowledge source
