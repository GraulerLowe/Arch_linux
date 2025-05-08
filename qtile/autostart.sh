#!/bin/sh
feh --bg-scale ~/Imágenes/20547943-2449214942.jpg 

#Start betterlockscreen
xautolock -time 15 -locker "betterlockscreen -l" &

# Start picom
picom --config ~/.config/picom/picom.conf &
