import PySimpleGUI as sg
import AioGuiLayouts

def Menu():
    window = sg.Window("AIO", AioGuiLayouts.Main)
    event, values = window.read()

    if event == "Personal":
        window.close()
        window = sg.Window("Person Menu", AioGuiLayouts.PersonalMenu)
        event, values = window.read()
        window.close()
        if event == "Name":
            window.close()
            window = sg.Window('Personal 1', AioGuiLayouts.UserInput)
            event, values = window.read()
            window.close()

            Forename = values[0]
            Surname = values[1]
            output = [
                [sg.Text("Your name is " + Forename + " " + Surname)],
                [sg.Button("Close")]
            ]
            window = sg.Window('Personal 1', output)
            event, values = window.read()
            if event == "close" or event == sg.WIN_CLOSED:
                window.close()
                window = sg.Window("AIO", AioGuiLayouts.Main2)
        else:
            window.close()
            window = sg.Window("AIO", AioGuiLayouts.Main3)

    elif event == "Close" or event == sg.WIN_CLOSED:
        window.close()    
    else:
        window = sg.Window("AIO", AioGuiLayouts.Main3)