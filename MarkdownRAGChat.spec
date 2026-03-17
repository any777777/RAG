# -*- mode: python ; coding: utf-8 -*-

from PyInstaller.utils.hooks import collect_all


chromadb_datas, chromadb_binaries, chromadb_hiddenimports = collect_all("chromadb")
genai_datas, genai_binaries, genai_hiddenimports = collect_all("google.genai")

datas = chromadb_datas + genai_datas
binaries = chromadb_binaries + genai_binaries
hiddenimports = chromadb_hiddenimports + genai_hiddenimports

a = Analysis(
    ["run_app.py"],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        "IPython",
        "matplotlib",
        "jupyter_client",
        "jupyter_core",
        "pytest",
    ],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name="MarkdownRAGChat",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
