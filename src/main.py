import tkinter, ntkutils, webbrowser, sv_ttk
from tkinter import DISABLED, LEFT, ttk
import os

import setupdialog

mods = ntkutils.cfgtools.init([], "mods.json")

if not mods:
    mods = setupdialog.init()
    ntkutils.SaveCFG(mods, "mods.json")

sv_ttk.inited = False

root = tkinter.Tk()
root.iconbitmap("./assets/icon.ico")
ntkutils.windowsetup(root, "Portal Launcher", None, False, "820x450")
ntkutils.dark_title_bar(root)
sv_ttk.set_theme("dark")

#region tabview
tabview = ttk.Notebook(root)
tabview.pack(fill="both", expand=True)

tab1 = ttk.Frame(tabview)
tab2 = ttk.Frame(tabview)
tab3 = ttk.Frame(tabview)

tabview.add(tab1, text="Portal")
tabview.add(tab2, text="Steam Mods")
tabview.add(tab3, text="Sourcemods")
#endregion

#region IMAGES
Portal_Image = tkinter.PhotoImage(master=root, file="assets/portal.png")
Portal2_Image = tkinter.PhotoImage(master=root, file="./assets/portal2.png")
PortalSM_Image = tkinter.PhotoImage(master=root, file="./assets/portalstoriesmel.png")
PortalR_Image = tkinter.PhotoImage(master=root, file="./assets/portalreloaded.png")
#endregion

Portal_Label = ttk.Label(tab1, image=Portal_Image, text="   Portal", compound=LEFT, font=("Segoe UI", 20)).place(x=55, y=50)
Portal2_Label = ttk.Label(tab1, image=Portal2_Image, text="   Portal 2", compound=LEFT, font=("Segoe UI", 20)).place(x=55, y=125)
PortalSM_Label = ttk.Label(tab2, image=PortalSM_Image, text="   Portal Stories: Mel", compound=LEFT, font=("Segoe UI", 20),).place(x=55, y=50)
PortalR_Label = ttk.Label(tab2, image=PortalR_Image, text="   Portal Reloaded", compound=LEFT, font=("Segoe UI", 20),).place(x=55, y=125)

Portal_Button = ttk.Button(tab1, text="Play", width=20, style="Accent.TButton", command=lambda:webbrowser.open("steam://rungameid/400"))
Portal_Speedrun_Button = ttk.Button(tab1, text="Source Unpack", width=20, state=DISABLED)
Portal2_Button = ttk.Button(tab1, text="Play", width=20, style="Accent.TButton", command=lambda:webbrowser.open("steam://rungameid/620"))
PortalSM_Button = ttk.Button(tab2, text="Play", width=20, style="Accent.TButton", command=lambda:webbrowser.open("steam://rungameid/317400"))
PortalR_Button = ttk.Button(tab2, text="Play", width=20, style="Accent.TButton", command=lambda:webbrowser.open("steam://rungameid/1255980"))

Portal_Button.place(x=400, y=55)
Portal_Speedrun_Button.place(x=600, y=55)
Portal2_Button.place(x=400, y=130)
PortalSM_Button.place(x=400, y=55)
PortalR_Button.place(x=400, y=130)

root.mainloop()
