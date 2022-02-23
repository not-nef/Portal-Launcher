import json
import os

def LoadCFG():
    with open("cfg.json") as cfg_file:
        cfg = json.load(cfg_file)

    return cfg

def SaveCFG(cfg):
    with open("cfg.json", "w") as cfg_file:
        json.dump(cfg, cfg_file)

def init():
    if not os.path.isfile("cfg.json"):
        with open("cfg.json", "w") as cfg_file:
            json.dump(
                {
                    "PortalP_ID": "notfound",
                    "Portal2SM_ID": "notfound",
                },
                cfg_file,
            )

        return LoadCFG()
    else:
        return LoadCFG()