#!/bin/env python

import sys
import subprocess
import os

f = os.path.expanduser('~')+"/.config/dunst/dunstrc"

disable = "  {}"
enable = "  {}"

disabled_str = '\n[disable_{0}]\n\tappname = {0}\n\tformat = ""\n\tsummary = "*"'

apps = ["Signal","Telegram","KDE Connect","neomutt", "Chromium"] 

rofi_str = ""

disabled = []
with open(f,"r") as dunstrc:
    content = dunstrc.read()
    for i in apps:
        if disabled_str.format(i) in content:
            rofi_str += disable.format(i)
            disabled.append(i)
        else:
            rofi_str += enable.format(i)
        rofi_str += "|"

    bashcmd = 'echo "{}" |rofi -sep "|"  -dmenu -i -p "  Disable/Enable notification " "" -width 20 -hide-scrollbar -eh 1 -line-padding 4  -color-enabled'.format(rofi_str)
    
    ret = subprocess.check_output(["bash", "-c", bashcmd])

    for i in apps:
        if i.encode() in ret:
            if i not in disabled:
                content += disabled_str.format(i)
            else:
                content = content.replace(disabled_str.format(i),"")
    print(content)

with  open(f,"w") as dunstrc:
    dunstrc.write(content)

os.system("killall dunst; dunst &")
