import PySimpleGUI as sg
import time

Main = [
    [
        sg.Text("Weclome To AIO"),
    ], 
    [
        sg.Text(" ")
    ],
    [
        sg.Button("Personal"), 
        sg.Button("Calculations"),
        sg.Button("Games"),
        sg.Button("Error Codes")
    ],
    [
        sg.Button("Close")
    ]
]

Main2 = [
    [
        sg.Text("Weclome To AIO"),
    ], 
    [
        sg.Text(" ")
    ],
    [
        sg.Button("Personal"), 
        sg.Button("Calculations"),
        sg.Button("Games"),
        sg.Button("Error Codes")
    ],
    [
        sg.Button("Close")
    ]
]

# Create the window
window = sg.Window("AIO", Main)

time.sleep(1)
# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "Personal":    
        UserInput = [
            [sg.Text('Forename', size =(15, 1)), sg.InputText()],
            [sg.Text('Surname', size =(15, 1)), sg.InputText()],
            [sg.Submit(), sg.Cancel()]
        ]

        window.close()
        window = sg.Window('Personal 1', UserInput)
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
        if event == "close":
            window.close()
            window = sg.Window("AIO", Main2)
        else:
            window.close()
            window = sg.Window("AIO", Main2)

    elif event == "Close":
        break
    
    else:
        window = sg.Window("AIO", layout)


