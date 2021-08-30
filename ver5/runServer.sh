#!/bin/sh
echo "Enter Port:"
read port
python makeWebpage.py $port &
python Stream_Updater_ver5.py $port &
