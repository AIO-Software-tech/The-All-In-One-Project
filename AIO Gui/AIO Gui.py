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
        widget.setCurrentIndex(widget.currentIndex()+4)

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

#?Caculations Menu
class Caculations(QDialog):
    def __init__(self):
        super(Caculations, self).__init__()
        loadUi("Caculations.ui", self)
        self.Close.clicked.connect(self.windowChange)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-4)

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

#All The Menu
LoginSystem = Login()
MainMenu = MainMenu()
IccorectUserOrPass = IccorectUserOrPass()
AIOErrorCodes = ErrorCodes()
Personal = Personal()
PersonalNameMenu = PersonalNameMenu()
PersonalAgeMenu = PersonalAgeMenu()
PersonalAddressMenu = PersonalAddressMenu()
Caculations = Caculations()
Games = Games()


#Showing All The Menus
widget.addWidget(LoginSystem)
widget.addWidget(MainMenu)
widget.addWidget(IccorectUserOrPass)
widget.addWidget(AIOErrorCodes)
widget.addWidget(Personal)
widget.addWidget(PersonalNameMenu)
widget.addWidget(PersonalAgeMenu)
widget.addWidget(PersonalAddressMenu)
widget.addWidget(Caculations)
widget.addWidget(Games)

widget.show()
app.exec_()

