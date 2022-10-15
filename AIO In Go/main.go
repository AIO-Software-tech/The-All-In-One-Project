package main

//Done
//? Imports
import (
    "fmt"
    "os"
    "syscall"
	"time"
    "golang.org/x/term"
)

//Done
//@ Who It Was Made By And The Current Version
func main() {

	fmt.Print("\n")
	fmt.Print("All-In-One By Imre Kiss And Oliver Boucher \n")
	fmt.Print("Version 0.0.1 REV-1 2022 \n")
	fmt.Print("\n")

	LoginInSystem()
}

//Done
//! Username and Password System:
func LoginInSystem() {
	var MRT int = 0
	fmt.Print("Username: ")
	var Username string
	fmt.Scanln(&Username)
    fmt.Print("Password: ")
    bytepw, err := term.ReadPassword(int(syscall.Stdin))
    if err != nil {
        os.Exit(1)
    }
    Password := string(bytepw)
	fmt.Scanln(&Password)

	fmt.Print("\n")
	if Username == "Ollie" && Password == "123"{
		MainMenu(Username, MRT)
	}
}

//ToDo
//? Main Menu
//This Prints The Main Menu And Takes The Selection Input
//MMS Stands For Main Menu Selection
//MRT Stands For Menu Run Times This Is To Stop The Main Menu Saying Hello Every Time
func MainMenu(Username string, MRT int) {
	if MRT < 1{
		fmt.Print("Hello ", Username, "\n")
	}
	MRT = MRT + 1
	fmt.Print("\n")
	fmt.Print("Selection Menu: Please Select One Of The Options:\n")
	fmt.Print("▣───────────────────────────────────────────────▣\n")
	fmt.Print("│                                               │\n")
	fmt.Print("│   1. = Personal                               │\n")
	fmt.Print("│                                               │\n")
	fmt.Print("│   2. = Calculations                           │\n")
	fmt.Print("│                                               │\n")
	fmt.Print("│   3. = Games                                  │\n")
	fmt.Print("│                                               │\n")
	fmt.Print("│   4. = Error Codes                            │\n")
	fmt.Print("│                                               │\n")
	fmt.Print("▣───────────────────────────────────────────────▣\n")
	fmt.Print("\n")
	fmt.Print("Please Select An Option From 1 To 4 \n")
	fmt.Print("Option: ")
	var MMS int
	fmt.Scanln(&MMS)

	if MMS >= 6 || MMS <= 0{
		fmt.Print("Please Try Again \n")
		fmt.Print("\n")
		MainMenu(Username, MRT)
	} else if MMS == 1{
		PersonalMenu(Username, MRT)
	} else if MMS == 2{
		CalculationsMenu(Username, MRT)
	} else if MMS == 3{
		GamesMenu(Username, MRT)
	} else if MMS == 4{
		ErrorCodes(Username, MRT)
	} else{
		fmt.Print("AIO Error Code 3 \n")
	}
	
}

//ToDo
//? Personal Menu
func PersonalMenu(Username string, MRT int) {
	fmt.Print("\n")
	fmt.Print("Currently In Develpment\n")
	fmt.Print("Please Check If You Are Running The Most Current Aphla Version\n")
	fmt.Print("\n")
	time.Sleep(1 * time.Second)
	MainMenu(Username, MRT)
}

//ToDo
//? Calculations Menu
func CalculationsMenu(Username string, MRT int) {
	fmt.Print("\n")
	fmt.Print("Currently In Develpment\n")
	fmt.Print("Please Check If You Are Running The Most Current Aphla Version\n")
	fmt.Print("\n")
	time.Sleep(1 * time.Second)
	MainMenu(Username, MRT)
}

//ToDo
//? Games Menu
func GamesMenu(Username string, MRT int) {
	fmt.Print("\n")
	fmt.Print("Currently In Develpment\n")
	fmt.Print("Please Check If You Are Running The Most Current Aphla Version\n")
	fmt.Print("\n")
	time.Sleep(1 * time.Second)
	MainMenu(Username, MRT)
}

//ToDo
//? Error Codes
func ErrorCodes(Username string, MRT int) {
	fmt.Print("▣──────────────────────────────────▣\n")
	fmt.Print("│                                   │\n")
	fmt.Print("│   1. = Invalid option/chose       │\n")
	fmt.Print("│                                   │\n")
	fmt.Print("│   2. = Invalid Username or Pass   │\n")
	fmt.Print("│                                   │\n")
	fmt.Print("│   3. = Invalid input              │\n")
	fmt.Print("│                                   │\n")
	fmt.Print("▣──────────────────────────────────▣\n")
	fmt.Print("\n")
	fmt.Print("Please Wait\n")
	fmt.Print("\n")
	time.Sleep(2 * time.Second)
	MainMenu(Username, MRT)
}
