# Evan
# ekirchst@uci.edu
# 59946460

from pathlib import Path
import ui as ui
import admin as admin
import user as user
from ds_client import send

if __name__ == "__main__":
    send("168.235.86.101", 3021, "juanita", "757575", "Monke MONKE MONKE MONKE BANANA YUMMY MONKE MONKE BANANANANA")
    
    if ui.user() == 1:
        admin.start()
    else:
        user.comm_list()
        user.start()