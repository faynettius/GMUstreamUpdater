@echo off
set /p ip="Enter Host's IP:"
set /p port="Enter Host's Port:"
python clientwindow.py %ip% %port%
