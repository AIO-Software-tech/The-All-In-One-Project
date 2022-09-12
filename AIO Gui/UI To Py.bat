@echo off
title .UI to .py files converter !
echo Generate Python files from .UI files!
pause
echo ""
echo ""
echo ""
echo ""
echo UI file Name
set /p UiName=Enter .UI file Name: 
echo ""
echo ""
echo ""
echo ""
echo PY file Name
set /p PyName=Enter .PY file Name: 
echo ""
echo ""
echo ""
echo Start Converting Files Please wait.



call python -m PyQt5.uic.pyuic -x "%UiName%" -o "%PyName%"

echo QRC file Name
set /p QrName=Enter .qrc file Name: 
echo ""
echo ""
echo ""
echo ""
echo PY file Name
set /p PiName=Enter .PY file Name: 
echo ""
echo ""
echo ""
echo Start Converting Files Please wait.

pyrcc5 -o "%PiName%" "%QrName%"

echo Job Completed.
pause