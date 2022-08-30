import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from datetime import date


#!Login System
class Login(QDialog):
    def __init__(self):
        
        super(Login, self).__init__()
        loadUi("AIO Gui Login.ui",self)
        self.Login.clicked.connect(self.loginfunction)
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Close.clicked.connect(QtWidgets.qApp.quit)

    def loginfunction(self):
        Username=self.Username.text()
        Password=self.Password.text()
        if Username == "Ollie" and Password == "#008701Boucher":
            print("you loged in")
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif Username == "Imre" and Password == "n@KoRi<£":
            print("you loged in")
            widget.setCurrentIndex(widget.currentIndex()+1)
        elif Username == "Admin" and Password == "ABC":
            print("you loged in")
            widget.setCurrentIndex(widget.currentIndex()+1)
        else:
            widget.setCurrentIndex(widget.currentIndex()+2)
  
#!Incorect Username Or Password
class IccorectUserOrPass(QDialog):
    def __init__(self):
        super(IccorectUserOrPass, self).__init__()
        loadUi("IUOP.ui", self)
        self.Ok.clicked.connect(self.windowChange)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

#?The Main Menu
class MainMenu(QDialog):
    def __init__(self):
        super(MainMenu, self).__init__()
        loadUi("Aio Main Menu.ui", self)
        self.Personal.clicked.connect(self.ChangeToPersonal)
        self.Caculations.clicked.connect(self.ChangeToCaculatios)
        self.Games.clicked.connect(self.ChangeToGames)
        self.Errors.clicked.connect(self.ChangeToError)
        self.Close.clicked.connect(QtWidgets.qApp.quit)
    
    def ChangeToError(self):
        widget.setCurrentIndex(widget.currentIndex()+2)
    
    def ChangeToPersonal(self):
        widget.setCurrentIndex(widget.currentIndex()+3)
        
    def ChangeToCaculatios(self):
        widget.setCurrentIndex(widget.currentIndex()+7)

    def ChangeToGames(self):
        widget.setCurrentIndex(widget.currentIndex()+5)

#?Error Codes Menu
class ErrorCodes(QDialog):
    def __init__(self):
        super(ErrorCodes, self).__init__()
        loadUi("Error Codes.ui", self)
        self.Close.clicked.connect(self.windowChange)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-2)
#Done
#?Personal Menus
class Personal(QDialog):
    def __init__(self):
        super(Personal, self).__init__()
        loadUi("Personal Menu.ui", self)
        self.Name.clicked.connect(self.ChangeToName)
        self.Age.clicked.connect(self.ChangeToAge)
        self.Address.clicked.connect(self.ChangeToAddress)
        self.Close.clicked.connect(self.windowChange)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-3)

    def ChangeToName(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def ChangeToAge(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

    def ChangeToAddress(self):
        widget.setCurrentIndex(widget.currentIndex()+3)

#Done
#*Personal Name Menu
class PersonalNameMenu(QDialog):
    def __init__(self):
        super(PersonalNameMenu, self).__init__()
        loadUi("PersonalNameMenu.ui", self)
        self.Submit.clicked.connect(self.OutputName)
        self.Close.clicked.connect(self.windowChange)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

    def OutputName(self):
        FirstName=self.Forname.text()
        LastName=self.Surname.text()
        print(FirstName + LastName)
        self.Output.setText(FirstName + " " + LastName)

#Done
#*Personal Age Menu
class PersonalAgeMenu(QDialog):
    def __init__(self):
        super(PersonalAgeMenu, self).__init__()
        loadUi("PersonalAgeMenu.ui", self)#
        self.Submit.clicked.connect(self.OutputAge)
        self.Close.clicked.connect(self.windowChange)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

    def OutputAge(self):
        YourAge=self.YourAge.text()
        current_year = date.today().year
        Output = int(current_year) - int(YourAge)
        self.Output.setText(str(Output))

#Done
#*Personal Address Menu
class PersonalAddressMenu(QDialog):
    def __init__(self):
        super(PersonalAddressMenu, self).__init__()
        loadUi("PersonalAddressMenu.ui", self)
        self.Submit.clicked.connect(self.OutputAddress)
        self.Close.clicked.connect(self.windowChange)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-3)

    def OutputAddress(self):
        First4 = self.First4.text()
        Last3 = self.Last3.text()
        self.Output.setText(First4 + " " + Last3)

#Done
#?Caculations Menu
class Caculations(QDialog):
    def __init__(self):
        super(Caculations, self).__init__()
        loadUi("Caculations.ui", self)
        self.BasicCaculator.clicked.connect(self.ChangeToBasicCaculator)
        self.Conversions.clicked.connect(self.ChangeToConvertiionsMenu)
        self.Close.clicked.connect(self.windowChange)
    
    def ChangeToBasicCaculator(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def ChangeToConvertiionsMenu(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-7)

#Done
#*Basic Calculator
class BasicCaculator(QDialog):
    def __init__(self):
        super(BasicCaculator, self).__init__()
        loadUi("Basic Caculator.ui", self)
        self.Num_1.clicked.connect(lambda: self.press_it("1"))
        self.Num_2.clicked.connect(lambda: self.press_it("2"))
        self.Num_3.clicked.connect(lambda: self.press_it("3"))
        self.Num_4.clicked.connect(lambda: self.press_it("4"))
        self.Num_5.clicked.connect(lambda: self.press_it("5"))
        self.Num_6.clicked.connect(lambda: self.press_it("6"))
        self.Num_7.clicked.connect(lambda: self.press_it("7"))
        self.Num_8.clicked.connect(lambda: self.press_it("8"))
        self.Num_9.clicked.connect(lambda: self.press_it("9"))
        self.Num_0.clicked.connect(lambda: self.press_it("0"))
        self.Clear.clicked.connect(lambda: self.press_it("C"))
        self.Persent.clicked.connect(lambda: self.press_it("%"))
        self.Equalse.clicked.connect(lambda: self.math_it())
        self.devicde.clicked.connect(lambda: self.press_it("/"))
        self.times.clicked.connect(lambda: self.press_it("*"))
        self.minus.clicked.connect(lambda: self.press_it("-"))
        self.plus.clicked.connect(lambda: self.press_it("+"))
        self.NegToPos.clicked.connect(lambda: self.plus_minus_it("-/+"))
        self.Bot.clicked.connect(lambda: self.dot_it())
        self.Close.clicked.connect(self.windowChange)

    def math_it(self):
        screen = self.Output.text()
        answer = eval(screen)
        self.Output.setText(str(answer))

    def plus_minus_it(self):
        screen = self.Output.text()
        if "-" in screen:
            self.Output.text(screen.replace("-", ""))
        else:
            self.Output.setText(f'-{screen}')

    def dot_it(self):
        screen = self.Output.text()
        if screen[-1] == ".":
            pass
        else:
            self.Output.setText(f'{screen}.')

    def press_it(self, pressed):
        if pressed == "C":
            self.Output.setText("0")

        else:
            if self.Output.text() == "0":
                self.Output.setText("")
            self.Output.setText(f'{self.Output.text()}{pressed}')


    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-1)

#ToDo
#*Convertions Menu
class ConvertionsMenu(QDialog):
    def __init__(self):
        super(ConvertionsMenu, self).__init__()
        loadUi("Convertions.ui", self)
        self.Close.clicked.connect(self.windowChange)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

#ToDo
#?Game Menu
class Games(QDialog):
    def __init__(self):
        super(Games, self).__init__()
        loadUi("Game Menu.ui", self)
        self.Close.clicked.connect(self.windowChange)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-5)

app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()

#?All The Menu

LoginSystem = Login()
MainMenu = MainMenu()
IccorectUserOrPass = IccorectUserOrPass()
AIOErrorCodes = ErrorCodes()
Personal = Personal()
PersonalNameMenu = PersonalNameMenu()
PersonalAgeMenu = PersonalAgeMenu()
PersonalAddressMenu = PersonalAddressMenu()
Caculations = Caculations()
BasicCaculator = BasicCaculator()
ConvertionsMenu = ConvertionsMenu()
Games = Games()


#?Showing All The Menus

#Done
#? Login In System
widget.addWidget(LoginSystem)

#Done
#? Main Menu
widget.addWidget(MainMenu)

#Done
#? Incorect Uuer Name Or Password
widget.addWidget(IccorectUserOrPass)

#Done
#? Error Code Menu
widget.addWidget(AIOErrorCodes)

#Done
#? Person menus 
widget.addWidget(Personal)
widget.addWidget(PersonalNameMenu)
widget.addWidget(PersonalAgeMenu)
widget.addWidget(PersonalAddressMenu)

#ToDo
#? Caculation Menu
widget.addWidget(Caculations)
widget.addWidget(BasicCaculator)
widget.addWidget(ConvertionsMenu)

#ToDo
#?Game Menus
widget.addWidget(Games)

#Done
#? Create Windows
widget.show()
app.exec_()


#ToDo To Do List
#£ Add AIO Notepad
    #£ Add Notepad class
        #£ Add Notepad def __into__
            #£ Add Close to Notepad

        #£ Add Save system to notepad

#£ Add Caculations
    #£ Add Caculation class
        #£ add def __into__
            #£ Add close button
        
        #£ menu slections system
            #£ make caculations ui files
            #£ code the backen for the ui files

#£ Add Games
    #£ Add Games class
        #£ Add Games slections menu
        #£ Make Game ui's
        #£ Code backend for ui files