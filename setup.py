from sys import executable
from unicodedata import name
import cx_Freeze

executables = [
    cx_Freeze.Executable(
        "main.py",
        base="Win32GUI",
        icon="./assets/icon.ico",
        shortcut_name="Portal Launcher",
        target_name="PortalLauncher.exe",
        shortcut_dir="ProgramMenuFolder",
    )
]

build_exe_options = {
    "include_msvcr": True,
    "include_files": (r"./assets"),
    "includes": ["tkinter", "sv_ttk", "ntkutils", "webbrowser", "cfgtools"],
}

bdist_msi_options = {
    "add_to_path": False,
    "install_icon": "./assets/icon.ico",
    "target_name": "PortalLauncher",
}

cx_Freeze.setup(
    name="Portal Launcher",
    version = "0.1",
    description = "A Launcher for portal games and mods!",
    executables = executables,
    options = {
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
    },
)