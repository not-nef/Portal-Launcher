import ntkutils, tkinter, os, sv_ttk, strsplit
from tkinter import ttk
from tkinter.filedialog import askdirectory


namelist = []
removedmods = []
idlist = []
finallist = []
steamdir = "C:/Program Files (x86)/Steam"


def cancelsetup(page):
    ntkutils.clearwin(setup)

    def goback():
        if page == "steamapps": steamapps()
        elif page == "selectmods": selectmods()

    def cancelsetup_cancel():
        if page == "selectmods": 
            namelist.clear()
            removedmods.clear()

        setup.destroy()

    cancel_biglabel = tkinter.Label(setup, text="Are you sure you want to cancel?", font=("", 20)).pack(pady=10)
    cancel_label = tkinter.Label(setup, text="You can always restart the setup in the settings!").pack(pady=10)
    cancel_btnyes = ttk.Button(setup, text="Yes", style="Accent.TButton", width=20, command=lambda:cancelsetup_cancel()).place(x=100, y=150)
    cancel_btnno = ttk.Button(setup, text="No", width=20, command=lambda:goback()).place(x=330, y=150)

def steamapps():
    ntkutils.clearwin(setup)

    def steamapps_error():
        ntkutils.sv_msgbox(
            setup,
            "This directory is not named Steam",
            "Therefore it cant be the Steam folder!",
            None,
            buttons=[("Ok", None, "default")],
            darktb=True
        )  

    def steamapps_browsedir():
        global steamdir
        steamdir = askdirectory(title="Open the Steam folder")
        steamapps_entry.insert(0, steamdir)
        if not steamdir.endswith("Steam"):
            steamapps_error()

    def steamapps_ok():
        if not steamapps_entry.get().endswith("steamapps"):
            steamapps_error()
        else:
            #cfg["steamapps"] = steamdir
            #ntkutils.cfgtools.SaveCFG(cfg)
            ntkutils.clearwin(setup)

    steamapps_biglabel = tkinter.Label(setup, text="Steamapps Folder", font=("", 25)).pack(pady=10)
    steamapps_label = tkinter.Label(setup, wraplength=550, text="PortalLauncher was not able to detect sourcemods because your steamapps directory does not appear to be the default one. Please enter the path of your steamapps directory below.").pack(pady=10)
    steamapps_entry = ttk.Entry(setup, width=50)
    steamapps_browse = ttk.Button(setup, text="Browse...", command=lambda:steamapps_browsedir()).place(x=450, y=140)
    steamapps_btnok = ttk.Button(setup, text="Ok", style="Accent.TButton", width=15, command=lambda:steamapps_ok()).place(x=135, y=200)
    steamapps_btncancel = ttk.Button(setup, text="Cancel Setup", width=15, command=lambda:cancelsetup("steamapps")).place(x=350, y=200)

    steamapps_entry.place(x=55, y=140)

def selectmods():
    ntkutils.clearwin(setup)
    selectmods_biglabel = tkinter.Label(setup, text="Select Mods", font=("", 25)).pack(pady=15)
    selectmods_btn = ttk.Button(setup, text="Continue", width=15, style="Accent.TButton", command=lambda:selectmods_continue())
    selectmods_btnreset = ttk.Button(setup, text="Reset", width=15, command=lambda:selectmods_reset())
    selectmods_cancel = ttk.Button(setup, text="Cancel Setup", width=15, command=lambda:cancelsetup("selectmods")).place(x=20, y=20)
    labely = 75

    def selectmods_continue():
        ntkutils.clearwin(setup)
        detect_ids()

    def selectmods_reset():
        namelist.clear()
        removedmods.clear()
        detect_sm()
        selectmods()

    def selectmods_remmod(mod):
        if not len(namelist) == 1:
            namelist.pop(namelist.index(mod))
            removedmods.append(mod)
        else: pass
        selectmods()

    for mod in namelist:
        tkinter.Label(setup, text=mod, font=("", 15)).place(x=50, y=labely)
        ttk.Button(setup, text="-", command=lambda x=mod:selectmods_remmod(x)).place(x=350, y=labely)
        labely = labely + 50

    setup.geometry("600x{}".format(labely))
    setup.update()
    selectmods_btn.place(x=setup.winfo_width() - 150, y=setup.winfo_height() - 50)
    selectmods_btnreset.place(x=setup.winfo_width() - 150, y=setup.winfo_height() - 100)

def nomods():
    ntkutils.clearwin(setup)
    nomods_biglabel = tkinter.Label(setup, text="Succes", font=("", 25)).pack(pady=15)
    nomods_label = tkinter.Label(setup, text="The automatic sourcemod detection did not find any Portal Mods!").pack(pady=10)
    nomods_btn = ttk.Button(setup, text="Ok", style="Accent.TButton", width=15, command=lambda: setup.destroy()).pack(pady=20)

def detect_ids():
    idfiledir = steamdir + "/userdata"
    idfiledir = idfiledir + "/" + os.listdir(idfiledir)[0] + "/760/screenshots.vdf"
    idfile = open(idfiledir)
    idfilecontent = idfile.readlines()
    for mod in namelist:
        for line in idfilecontent:
            if mod in line:
                idlist.append(strsplit.before(strsplit.after(line, "\""), "\""))
    for index in range(len(namelist)):
        finallist.append([namelist[index], idlist[index]])
    finish()

def detect_sm():
    global found
    if os.path.isdir(steamdir) and "sourcemods" in os.listdir(steamdir + "/steamapps"):
        sourcemodsdir_content = os.listdir(steamdir + "/steamapps/sourcemods")
        for mod in sourcemodsdir_content:
            gameinfo = open(steamdir + "/steamapps/sourcemods/" + mod + "/gameinfo.txt")
            gameinfo_content = gameinfo.readlines()

            for line in gameinfo_content:
                if "game" in line and "\"" in line and not "game" in strsplit.inbetween(line, "\"", "\""):
                    thing = line
                    break

            for line in gameinfo_content:
                if "SteamAppId" in line:
                    if "400" in line or "620" in line:
                        namelist.append(strsplit.inbetween(thing, "\"", "\""))
                        break
        if not namelist:
            nomods()
        else:
            selectmods()
    else:  
        steamapps()

def finish():
    ntkutils.clearwin(setup)
    setup.geometry("600x175")

    finish_biglabel = tkinter.Label(setup, text="Done", font=("", 20)).pack(pady=10)
    finish_label = tkinter.Label(setup, text="The setup was succesful!").pack(pady=10)
    finish_btn = ttk.Button(setup, text="Continue to launcher", width=25, command=lambda:setup.destroy(), style="Accent.TButton").pack(pady=10)


def init():
    global setup

    setup = tkinter.Tk()
    ntkutils.windowsetup(setup, "Sourcemods Setup", None, False, "600x175")
    ntkutils.dark_title_bar(setup)
    sv_ttk.set_theme("dark")

    setup_biglabel = tkinter.Label(setup, text="Sourcemods Setup", font=("", 20)).pack(pady=10)
    setup_label = tkinter.Label(setup, text="This setup automatically detects installed sourcemods!").pack(pady=10)
    setup_btnyes = ttk.Button(setup, text="Run Setup", width=15, style="Accent.TButton", command=lambda:detect_sm()).place(x=370, y=125)
    setup_btnno = ttk.Button(setup, text="Maybe Later", width=15).place(x=100, y=125)

    setup.mainloop()

    return finallist