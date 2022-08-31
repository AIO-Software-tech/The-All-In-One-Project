import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
from datetime import date

#Done
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

#Done
#!Incorect Username Or Password
class IccorectUserOrPass(QDialog):
    def __init__(self):
        super(IccorectUserOrPass, self).__init__()
        loadUi("IUOP.ui", self)
        self.Ok.clicked.connect(self.windowChange)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

#Done
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

#Done
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
        self.VotingSystem.clicked.connect(self.ChangeToVotingSystem)
        self.Close.clicked.connect(self.windowChange)
    
    def ChangeToBasicCaculator(self):
        widget.setCurrentIndex(widget.currentIndex()+1)

    def ChangeToConvertiionsMenu(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

    def ChangeToVotingSystem(self):
        widget.setCurrentIndex(widget.currentIndex()+3)

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

#Done
#*Convertions Menu
class ConvertionsMenu(QDialog):
    def __init__(self):
        super(ConvertionsMenu, self).__init__()
        loadUi("Convertions.ui", self)
        self.KmToMiles.clicked.connect(self.ChangeToKmToMiles)
        self.MilesToKm.clicked.connect(self.ChangeToMilesToKm)
        self.KgToLbs.clicked.connect(self.ChangeToKgToLbs)
        self.LbsToKg.clicked.connect(self.ChangeToLbsToKg)
        self.CmToInches.clicked.connect(self.ChangeToCmToInches)
        self.InchesToCm.clicked.connect(self.ChangeToInchesToCm)
        self.Close.clicked.connect(self.windowChange)

    def ChangeToKmToMiles(self):
        widget.setCurrentIndex(widget.currentIndex()+2)

    def ChangeToMilesToKm(self):
        widget.setCurrentIndex(widget.currentIndex()+3)

    def ChangeToKgToLbs(self):
        widget.setCurrentIndex(widget.currentIndex()+4)

    def ChangeToLbsToKg(self):
        widget.setCurrentIndex(widget.currentIndex()+5)

    def ChangeToCmToInches(self):
        widget.setCurrentIndex(widget.currentIndex()+6)

    def ChangeToInchesToCm(self):
        widget.setCurrentIndex(widget.currentIndex()+7)

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

#Done
#*Km To Miles Convertor
class KmToMiles(QDialog):
    def __init__(self):
        super(KmToMiles, self).__init__()
        loadUi("Km To Miles.ui", self)
        self.Submit.clicked.connect(self.OutputName)
        self.Close.clicked.connect(self.windowChange)

    def OutputName(self):
        Input_1=self.Input_1.text()
        Answer = float(Input_1) / 1.609
        self.Output_2.setText("Miles: " + str(Answer))

    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-2)

#Done
#*Miles To Km Convertor
class MilesToKm(QDialog):
    def __init__(self):
        super(MilesToKm, self).__init__()
        loadUi("MilesToKm.ui", self)
        self.Submit.clicked.connect(self.OutputName)
        self.Close.clicked.connect(self.windowChange)

    def OutputName(self):
        Input_1=self.Input_1.text()
        Answer = float(Input_1) * 1.609
        self.Output_2.setText("Km: " + str(Answer))
    
    def windowChange(self):
        widget.setCurrentIndex(widget.currentIndex()-3)

#Done
#*Kg To Lbs Convertor
class KgToLbs(QDialog):
    def __init__(self):
        super(KgToLbs, self).__init__()
        loadUi("KgToLbs.ui", self)
        self.Submit.clicked.connect(self.OutputName)
        self.Close.clicked.connect(self.windowChange)

    def OutputName(self):
        Input_1=self.Input_1.text()
        Answer = float(Input_1) * 2.205
        self.Output_2.setText("Lbs: " + str(Answer))

    def windowChange(self):
            widget.setCurrentIndex(widget.currentIndex()-4)

#Done
#*Lbs To Kg Convertor
class LbsToKg(QDialog):
    def __init__(self):
        super(LbsToKg, self).__init__()
        loadUi("LbsToKg.ui", self)
        self.Submit.clicked.connect(self.OutputName)
        self.Close.clicked.connect(self.windowChange)

    def OutputName(self):
        Input_1=self.Input_1.text()
        Answer = float(Input_1) / 2.205
        self.Output_2.setText("Kg: " + str(Answer))
        
    def windowChange(self):
            widget.setCurrentIndex(widget.currentIndex()-5)

#Done
#*Cm To Inches Convertor
class CmToInches(QDialog):
    def __init__(self):
        super(CmToInches, self).__init__()
        loadUi("CmToInches.ui", self)
        self.Submit.clicked.connect(self.OutputName)
        self.Close.clicked.connect(self.windowChange)

    def OutputName(self):
        Input_1=self.Input_1.text()
        Answer = float(Input_1) / 2.540
        self.Output_2.setText("Inches: " + str(Answer))

    def windowChange(self):
            widget.setCurrentIndex(widget.currentIndex()-6)

#Done
#*Inches To Cm Convertor
class InchesToCm(QDialog):
    def __init__(self):
        super(InchesToCm, self).__init__()
        loadUi("InchesToCm.ui", self)
        self.Submit.clicked.connect(self.OutputName)
        self.Close.clicked.connect(self.windowChange)

    def OutputName(self):
        Input_1=self.Input_1.text()
        Answer = float(Input_1) * 2.540
        self.Output_2.setText("Cm: " + str(Answer))

    def windowChange(self):
            widget.setCurrentIndex(widget.currentIndex()-7)

#Done
#*Voting System
class VotingSystem(QDialog):
    def __init__(self):
        super(VotingSystem, self).__init__()
        loadUi("VotingSystem.ui", self)
        self.Vote1.clicked.connect(lambda: self.press_it("1"))
        self.Vote2.clicked.connect(lambda: self.press_it("2"))
        self.Vote3.clicked.connect(lambda: self.press_it("3"))
        self.Vote4.clicked.connect(lambda: self.press_it("4"))
        self.Vote5.clicked.connect(lambda: self.press_it("5"))
        self.Reset.clicked.connect(self.reset)
        self.Close.clicked.connect(self.windowChange)

    def reset(self):
        self.VoteCounter1.setText("0")
        self.VoteCounter2.setText("0")
        self.VoteCounter3.setText("0")
        self.VoteCounter4.setText("0")
        self.VoteCounter5.setText("0")

    def press_it(self, pressed):
        if pressed == "1":
            VoteFor1 = int(self.VoteCounter1.text()) + 1
            self.VoteCounter1.setText(str(VoteFor1))

        elif pressed == "2":
            VoteFor2 = int(self.VoteCounter2.text()) + 1
            self.VoteCounter2.setText(str(VoteFor2))

        elif pressed == "3":
            VoteFor3 = int(self.VoteCounter3.text()) + 1
            self.VoteCounter3.setText(str(VoteFor3))

        elif pressed == "4":
            VoteFor4 = int(self.VoteCounter4.text()) + 1
            self.VoteCounter4.setText(str(VoteFor4))

        elif pressed == "5":
            VoteFor5 = int(self.VoteCounter5.text()) + 1
            self.VoteCounter5.setText(str(VoteFor5))
            

    def windowChange(self):
            widget.setCurrentIndex(widget.currentIndex()-3)


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
KmToMiles = KmToMiles()
MilesToKm = MilesToKm()
KgToLbs = KgToLbs()
LbsToKg = LbsToKg()
CmToInches = CmToInches()
InchesToCm = InchesToCm()
VotingSystem = VotingSystem()
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
widget.addWidget(VotingSystem)

#Done
#? Convertions Menu
widget.addWidget(KmToMiles)
widget.addWidget(MilesToKm)
widget.addWidget(KgToLbs)
widget.addWidget(LbsToKg)
widget.addWidget(CmToInches)
widget.addWidget(InchesToCm)

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