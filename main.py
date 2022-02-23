import tkinter
from tkinter import DISABLED, LEFT, ttk
import ntkutils
import webbrowser
import cfgtools
import sv_ttk

cfg = cfgtools.init()

if cfg["PortalP_ID"] == "notfound" or cfg["Portal2SM_ID"] == "notfound":
    askid = tkinter.Tk()
    askid.iconbitmap("./assets/icon.ico")
    ntkutils.windowsetup(askid, "Setup", None, False, "550x250")
    ntkutils.dark_title_bar(askid)
    sv_ttk.set_theme("dark")

    def _validate():
        global PortalP_ID, Portal2SM_ID, cfg

        try:
            int(PortalP_Entry.get())
            int(Portal2SM_Entry.get())
            cfg["PortalP_ID"] = PortalP_Entry.get()
            cfg["Portal2SM_ID"] = Portal2SM_Entry.get()
            cfgtools.SaveCFG(cfg)
            askid.destroy()
        except ValueError:
            ntkutils.sv_msgbox(
                askid,
                "You entered letters",
                "Enter a number",
                None,
                buttons=[("Ok", None, "default")]
            )

    def idhelp():
        ntkutils.sv_msgbox(
            askid,
            "How to find the mods id",
            "Hover over the shortcut to your mod.\nYou should see some text starting with \"steam://rungameid/\".\nEnter the long number after that in here.",
            None,
            buttons=[("Ok", None, "default")],
        )

    ID_Label = ttk.Label(askid, text="Enter game ids", font=("", 30))

    PortalP_ID_Label = ttk.Label(askid, text="      Portal: Prelude", font=("", 15))
    PortalP_Entry = ttk.Entry(askid, width=38)
    PortalP_Entry.insert(0, "Enter the game id of Portal: Prelude")

    Portal2SM_ID_Label = ttk.Label(askid, text="Portal 2 Speedrun Mod", font=("", 15))
    Portal2SM_Entry = ttk.Entry(askid, width=38)
    Portal2SM_Entry.insert(0, "Enter the game id of Portal 2 Speedrun Mod")

    ID_Label.pack(pady=10)
    PortalP_ID_Label.place(x=20, y=77)
    PortalP_Entry.place(x=245, y=70)
    Portal2SM_ID_Label.place(x=20, y=147)
    Portal2SM_Entry.place(x=245, y=140)

    id_button = ttk.Button(askid, text = "How do i find the ids?", command=lambda: idhelp(), width=25)
    ok_button = ttk.Button(askid, text = "Ok", style = "Accent.TButton", command=lambda: _validate(), width=25)

    id_button.place(x=60, y=195)
    ok_button.place(x=290, y=195)

    askid.mainloop()

sv_ttk.inited = False

print(cfg["PortalP_ID"])

root = tkinter.Tk()
root.iconbitmap("./assets/icon.ico")
ntkutils.windowsetup(root, "Portal Launcher", None, False, "820x450")
ntkutils.dark_title_bar(root)
sv_ttk.set_theme("dark")

#PortalP_ID = 10163175146832003472
#Portal2SM_ID = 14884186873424511596

PortalP_ID = cfg["PortalP_ID"]
Portal2SM_ID = cfg["Portal2SM_ID"]

Portal_Image = tkinter.PhotoImage(master=root, file="assets/portal.png")
Portal2_Image = tkinter.PhotoImage(master=root, file="./assets/portal2.png")
PortalSM_Image = tkinter.PhotoImage(master=root, file="./assets/portalstoriesmel.png")
PortalR_Image = tkinter.PhotoImage(master=root, file="./assets/portalreloaded.png")
PortalP_Image = tkinter.PhotoImage(master=root, file="./assets/portalprelude.png")

Portal_Label = ttk.Label(root, image=Portal_Image, text="   Portal", compound=LEFT, font=("Segoe UI", 20)).place(x=55, y=50)
Portal2_Label = ttk.Label(root, image=Portal2_Image, text="   Portal 2", compound=LEFT, font=("Segoe UI", 20)).place(x=55, y=125)
PortalSM_Label = ttk.Label(root, image=PortalSM_Image, text="   Portal Stories: Mel", compound=LEFT, font=("Segoe UI", 20),).place(x=55, y=200)
PortalR_Label = ttk.Label(root, image=PortalR_Image, text="   Portal Reloaded", compound=LEFT, font=("Segoe UI", 20),).place(x=55, y=275)
PortalP_Label = ttk.Label(root, image=PortalP_Image, text="   Portal: Prelude", compound=LEFT, font=("Segoe UI", 20),).place(x=55, y=350)

Portal_Button = ttk.Button(root, text="Play", width=20, style="Accent.TButton", command=lambda:webbrowser.open("steam://rungameid/400"))
Portal_Speedrun_Button = ttk.Button(root, text="Source Unpack", width=20, state=DISABLED)
Portal2_Button = ttk.Button(root, text="Play", width=20, style="Accent.TButton", command=lambda:webbrowser.open("steam://rungameid/620"))
Portal2_Speedrun_Button = ttk.Button(root, text="Speedrun Mod", width=20, command=lambda:webbrowser.open(f"steam://rungameid/{Portal2SM_ID}"))
PortalSM_Button = ttk.Button(root, text="Play", width=20, style="Accent.TButton", command=lambda:webbrowser.open("steam://rungameid/317400"))
PortalR_Button = ttk.Button(root, text="Play", width=20, style="Accent.TButton", command=lambda:webbrowser.open("steam://rungameid/1255980"))
PortalP_Button = ttk.Button(root, text="Play", width=20, style="Accent.TButton", command=lambda:webbrowser.open(f"steam://rungameid/{PortalP_ID}"))

Portal_Button.place(x=400, y=55)
Portal_Speedrun_Button.place(x=600, y=55)
Portal2_Button.place(x=400, y=130)
Portal2_Speedrun_Button.place(x=600, y=130)
PortalSM_Button.place(x=400, y=205)
PortalR_Button.place(x=400, y=280)
PortalP_Button.place(x=400, y=355)

root.mainloop()
