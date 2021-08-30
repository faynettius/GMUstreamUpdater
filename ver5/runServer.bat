@echo off
set /p port="Enter port:"
start cmd /k python makeWebpage.py %port%
python Stream_Updater_ver5.py %port%
