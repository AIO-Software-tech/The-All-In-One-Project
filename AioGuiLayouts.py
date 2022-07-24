import PySimpleGUI as sg

UandP1 = [
    [sg.Text('Username', size =(9, 1)), sg.InputText()],
    [sg.Text('Password', size =(9, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
UandP2 = [
    [sg.Text('Username', size =(9, 1)), sg.InputText()],
    [sg.Text('Password', size =(9, 1)), sg.InputText()],
    [sg.Button("Submit")]
]
UandP3 = [
    [sg.Text('Username', size =(9, 1)), sg.InputText()],
    [sg.Text('Password', size =(9, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
IncorectPassword1 = [
    [
        sg.Text("Increct Username OR Password")
    ],
    [
        sg.Button("Retry"),
        sg.Button("Cancel")
    ]
]
PersonalMenu = [
    [
        sg.Text("Personal"),
        sg.Text(" "),
    ],
    [
        sg.Button("Name"),
        sg.Button("Age"),
        sg.Button("Address")
    ]
]
UserInput = [
    [sg.Text('Forename', size =(15, 1)), sg.InputText()],
    [sg.Text('Surname', size =(15, 1)), sg.InputText()],
    [sg.Submit(), sg.Cancel()]
]
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

Main3 = [
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
        


