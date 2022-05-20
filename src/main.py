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

gammaenergy = tkinter.PhotoImage(master=root, file="./assets/gammaenergy.png")
p2sm = tkinter.PhotoImage(master=root, file="./assets/p2sm.png")
portalepicedition = tkinter.PhotoImage(master=root, file="./assets/portalepicedition.png")
portalprelude = tkinter.PhotoImage(master=root, file="./assets/portalprelude.png")
#endregion

#region Tab 1 + 2
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
#endregion

#region Tab 3
labely = 50
pages = int(len(mods) / 4) + 1
page = 1

def getimage(mod):
    if mod == "Gamma Energy": return gammaenergy
    elif mod == "Portal 2 Speedrun Mod": return p2sm
    elif mod == "Portal Epic Edition": return portalepicedition
    elif mod == "Portal: Prelude": return portalprelude
    else: return Portal2_Image

def pageswitch(direction):
    global page, labely, pages
    for slave in tab3.place_slaves(): slave.destroy()
    if direction == "right":
        page = page + 1
        pageleft.configure(state="normal")
        if page == pages: pageright.configure(state="disabled")
    else:
        page = page - 1
        pageright.configure(state="normal")
        if page == 1: pageleft.configure(state="disabled")
    labely = 50
    buildmods()

pageright = ttk.Button(tab3, text="->", command=lambda:pageswitch("right"))
pageright.pack(side=tkinter.RIGHT, anchor=tkinter.S, padx=10, pady=10)
pageleft = ttk.Button(tab3, text="<-", command=lambda:pageswitch("left"), state="disabled")
pageleft.pack(side=tkinter.LEFT, anchor=tkinter.S, padx=10, pady=10)

def buildmods():
    global labely, mods
    for mod in mods:
        if not mods.index(mod) > (page * 4 - 1) and not mods.index(mod) < (page * 4 - 4):
            tkinter.Label(tab3, text=f"   {mod[0]}", font=("Segoe UI", 20), image=getimage(mod[0]), compound=tkinter.LEFT).place(x=55, y=labely)
            ttk.Button(tab3, text="Play", width=20, style="Accent.TButton", command= lambda id=mod:webbrowser.open(f"steam://rungameid/{id[1]}")).place(x=600, y=labely+5)
            labely = labely+75
    pagelabel = tkinter.Label(tab3, text=f"Page {page} out of {pages}").place(x=55, y=370)

buildmods()
#endregion

root.mainloop()
