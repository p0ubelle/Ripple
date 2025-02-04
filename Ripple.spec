# -*- mode: python -*-
import os
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Define the main script
main_script = "ripple.py"

# Collect all submodules from 'src'
hidden_imports = collect_submodules('src')

# Collect all non-Python data files (JSON, images)
data_files = [("themes", "themes")]  # <-- This is the new line

# PyInstaller specification
a = Analysis(
    [main_script],
    pathex=["."],  # Search path
    binaries=[],
    datas=data_files,  # Include theme assets
    hiddenimports=hidden_imports,  # Import all submodules
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=None,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="Ripple",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Hide console window
    icon="themes/logo.png",  # Set app icon
)
