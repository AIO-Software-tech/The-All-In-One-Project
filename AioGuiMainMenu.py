import PySimpleGUI as sg
import time
import AioGui
import AioGuiLayouts
import sys

IncorectPassword = 0

window = sg.Window("Incrorect Password", AioGuiLayouts.IncorectPassword1)
window = sg.Window("AIO", AioGuiLayouts.UandP1)
values = window.read()
window.close()

if values[0] == "OGB" and values[1] == "#008701Boucher":
    AioGui.Menu()
elif values[0] == "Imre" and values[1] == "n@KoRi<£":
    AioGui.Menu()
elif values[0] == "Admin" and values[1] == "abc":
    AioGui.Menu()


