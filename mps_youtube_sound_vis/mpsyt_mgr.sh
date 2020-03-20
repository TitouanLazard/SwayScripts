#!/bin/sh
if swaymsg -t get_tree | grep MPYSTX8945 >/dev/null;
then
   swaymsg '[app_id=MPYSTX8945]' scratchpad show
else
   swaymsg exec  "termite --name=MPYSTX8945 --exec=~/.config/sway/tmux_lay_mpsyt.sh"
   sleep 1
   swaymsg '[app_id=MPYSTX8945]' floating enable
   swaymsg '[app_id=MPYSTX8945]' resize set height 600 px
   swaymsg '[app_id=MPYSTX8945]' move scratchpad
   swaymsg '[app_id=MPYSTX8945]' scratchpad show
   
fi
