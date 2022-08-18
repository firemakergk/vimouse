# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['F:/project/vimouse/src/main.py'],
    pathex=['F:/env/python/venv/vimmouse/Lib/site-packages'],
    binaries=[],
    datas=[('F:/project/vimouse/src/core', 'core/'), ('F:/project/vimouse/src/controller', 'controller/'), ('F:/project/vimouse/src/ui', 'ui/'), ('F:/project/vimouse/src/utils', 'utils/')],
    hiddenimports=['json'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [('v', None, 'OPTION')],
    exclude_binaries=True,
    name='vimouse',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='F:\\project\\vimouse\\logo.ico',
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='vimouse',
)
