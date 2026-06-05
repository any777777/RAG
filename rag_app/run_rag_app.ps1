$ErrorActionPreference = "Stop"

$ProjectRoot = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location $ProjectRoot

python rag_app/indexer.py --build

try {
    Invoke-WebRequest -Uri "http://localhost:11434/api/tags" -UseBasicParsing -TimeoutSec 5 | Out-Null
} catch {
    Start-Process -FilePath "ollama" -ArgumentList @("serve") -WorkingDirectory $ProjectRoot -WindowStyle Hidden
    Start-Sleep -Seconds 5
}

ollama pull qwen3:1.7b
streamlit run rag_app/app.py

