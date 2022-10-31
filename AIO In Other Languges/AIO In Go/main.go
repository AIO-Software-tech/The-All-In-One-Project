package main

//Done
//? Imports
import (
    "fmt"
    "os"
    "syscall"
	"fromDate"
	"time"
    "golang.org/x/term"
)

//Done
//@ Who It Was Made By And The Current Version
func main() {

	fmt.Print("\n")
	fmt.Print("All-In-One By Imre Kiss And Oliver Boucher \n")
	fmt.Print("Version 0.0.3 REV-1 2022 \n")
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
	} else if Username == "Ollie" && Password == "#008701Boucher"{
		MainMenu(Username, MRT)
	} else if Username == "Imre" && Password == "#008803Kiss"{
		MainMenu(Username, MRT)
	} else if Username == "Admin" && Password == "abc"{
		MainMenu(Username, MRT)
	} else if Username == "Guest" && Password == "123"{
		MainMenu(Username, MRT)
	} else{
		fmt.Print("AIO Error Code 2 \n")
		fmt.Print("\n")
		LoginInSystem()
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
	fmt.Print("│   5. = Exit                                   │\n")
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
	} else if MMS == 5{
		os.Exit(1)
	} else{
		fmt.Print("AIO Error Code 3 \n")
	}
	
}

//ToDo
//? Personal Menu
//PMS Stands For Personal Menu Selection
func PersonalMenu(Username string, MRT int) {
	fmt.Print("Selection Menu: Please Select One Of The Options: ")
	fmt.Print("\n")
    fmt.Print("▣─────────────────▣\n")
    fmt.Print("│                 │\n")
    fmt.Print("│   1. = Name     │\n")
    fmt.Print("│                 │\n")
    fmt.Print("│   2. = Age      │\n")
    fmt.Print("│                 │\n")
    fmt.Print("│   3. = Address  │\n")
	fmt.Print("│                 │\n")
	fmt.Print("│   4. = Back     │\n")
	fmt.Print("│                 │\n")
    fmt.Print("▣─────────────────▣\n")
	fmt.Print("\n")
	fmt.Print("Please Select One Of The Following Options 1,2,3,4: ")
	var PMS int
	fmt.Scanln(&PMS)
	
	if PMS == 1{
		fmt.Print("What Is Your Forename: ")
		var Forename string
		fmt.Scanln(&Forename)
		fmt.Print("What Is Your Surname: ")
		var Surname string
		fmt.Scanln(&Surname)
		fmt.Print("Your Name Is ", Forename, " ", Surname,"\n")
		time.Sleep(1 * time.Second)
		MainMenu(Username, MRT)

	} else if PMS == 2{
		year := fromDate.Year()
		fmt.Print("What Is Your Age: ")
		var userAge int
		fmt.Scanln(&userAge)
		var yearBorn int = year - userAge
		if yearBorn < 0{
			print("Nice Try Kid.\n")
		} else{
			print("So You Were Born In ", yearBorn, "\n")
			time.Sleep(1 * time.Second)
		}
		MainMenu(Username, MRT)

	} else if PMS == 3{

	} else if PMS == 4{
		MainMenu(Username, MRT)
	}
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

//Done
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
