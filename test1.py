b, values = window.Read()  # read input values from GUI
        
        # if you click config button, close main window and open config window:
	if b == "config": # main menu config button press
		window.Close()
		window = sg.Window('Test Anatomy - Configuration Panel').Layout(
					[[sg.Column(layout2)]]).Finalize()

        # if you click button on new window, close it and reopen main window:
	if b == "Connect Database":
		sg.Popup("Settings Saved")
		window.Close()
		window = sg.Window("Test Anatomy - Main Menu", grab_anywhere=True, no_titlebar=False, auto_size_text=False, icon=MY_WINDOW_ICON).Layout(layout).Finalize()