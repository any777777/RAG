param(
    [string]$Python = "python"
)

$ErrorActionPreference = "Stop"
$VenvPath = ".\.venv-build"

if (-not (Test-Path $VenvPath)) {
    & $Python -m venv $VenvPath
}

$VenvPython = Join-Path $VenvPath "Scripts\python.exe"

& $VenvPython -m pip install --upgrade pip
& $VenvPython -m pip install -r requirements.txt

if (Test-Path ".\build") {
    Remove-Item ".\build" -Recurse -Force
}

if (Test-Path ".\dist") {
    Remove-Item ".\dist" -Recurse -Force
}

& $VenvPython -m PyInstaller ".\MarkdownRAGChat.spec" --noconfirm --clean

Copy-Item ".\.env" ".\dist\.env" -Force
Copy-Item ".\README.md" ".\dist\README.md" -Force

Write-Host ""
Write-Host "Build complete."
Write-Host "Executable: dist\MarkdownRAGChat.exe"
