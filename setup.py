from cx_Freeze import Executable, setup

executables = [
    Executable(
        "main.py",
        base="Win32GUI",
        icon="./assets/icon.ico",
        shortcutName="Portal Launcher",
        shortcut_dir="DesktopFolder",
    )
]

build_exe_options = {
    "include_msvcr": True,
    "include_files": (r"./assets"),
    "includes": ["tkinter", "sv_ttk", "ntkutils", "webbrowser"],
}

bdist_msi_options = {
    "add_to_path": False,
    "install_icon": "./assets/icon.ico",
    "target_name": "PortalLauncher",
}

setup(
    name="Portal Launcher",
    version = "0.1",
    description = "A Launcher for portal games and mods!",
    executables = executables,
    options = {
        "build_exe": build_exe_options,
        "bdist_msi": bdist_msi_options,
    },
)