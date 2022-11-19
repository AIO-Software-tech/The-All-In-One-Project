#Done

#? Imports:
import time
import random
import sys
import platform

#Done
#! Username and Password System:
def UserPass():
    #@ Who It Was Made By:
    print("Tout-en-un par Imre Kiss et Oliver Boucher")
    print(" ")
    print("Version 2.2.3 REV-1 2022")
    print("this is a test")
    print(" ")
    username = input("Nom d'utilisateur: ")
    if username == "Ollie" or username == "Admin" or username == "Imre" or username == "Guest":
        password = input("Mot de passe: ")
        if username == "Ollie" and password == "#008701Boucher":
            Menu()
        elif username == "Imre" and password == "#008803Kiss":
            Menu()
        elif username == "Admin" and password == "abc":
            Menu()
        elif username == "Guest" and password == "123":
            Menu()
        else:
            print("Code d'erreur 2")
            UserPass()
    else:
        print("Code d'erreur 3")
        UserPass()

#Done
#? Select Menu:
def Menu():
    while True:
        print(" ")
        print("Menu de sélection : veuillez sélectionner l'une des options:")
        print("▣───────────────────────────────────────────────▣")
        print("│                                               │")
        print("│   1. = Personnel                              │")
        print("│                                               │")
        print("│   2. = Calculs                                │")
        print("│                                               │")
        print("│   3. = Jeux                                   │")
        print("│                                               │")
        print("│   4. = Code d'erreurs                         │")
        print("│                                               │")
        print("│   5. = proche                                 │")
        print("│                                               │")
        print("▣───────────────────────────────────────────────▣")

        unit = int(input("Veuillez sélectionner l'une des options suivantes 1,2,3,4: "))
        print()

        #Done
        #* Personal:
        if unit == 1:
            print("Menu de sélection: veuillez sélectionner l'une des options: ")
            print("▣─────────────────▣")
            print("│                 │")
            print("│   1. = Nom      │")
            print("│                 │")
            print("│   2. = Âge      │")
            print("│                 │")
            print("│   3. = Adresse  │")
            print("│                 │")
            print("│   4. = Retour   │")
            print("│                 │")
            print("▣─────────────────▣")

            PersonlMenu = int(input("Veuillez sélectionner l'une des options suivantes 1,2,3:"))

            #Done
            #£ Name:
            if PersonlMenu == 1:
                name1 = input("Quel est votre prénom: ")
                name2 = input("Quel est ton surnom: ")
                print("Ton nom est " + name1 + " " + name2)
                time.sleep(1)

            #Done
            #£ Age:
            elif PersonlMenu == 2:
                userAge = int(input("Quel âge avez-vous: "))
                yearBorn = 2022-userAge
                if yearBorn < 0:
                    print("Bel essai enfant")
                else:
                    print("Alors tu es né en " + str(yearBorn))
                    time.sleep(1)

            #Done
            #£ Address:
            elif PersonlMenu == 3:
                F3 = input("Quels sont les 3 premiers chiffres de votre code postal ?")
                L4 = input("Quels sont les 4 derniers chiffres de votre code postal ?")
                print("Votre code postal est: " +str(F3) + " " +str(L4))
                time.sleep(1)

            #Done
            #£ Go back to menu
            elif PersonlMenu == 3:
                Menu()

            #Done
            #£ Goes Back To The Main Menu
            else:
                Menu()
        #Done
        #* Calculations:
        elif unit == 2:
            print("Menu de sélection: veuillez sélectionner l'une des options: ")
            print("▣─────────────────────────────▣")
            print("│                              │")
            print("│   1. = Standard              │")
            print("│                              │")
            print("│   2. = Convertisseur         │")
            print("│                              │")
            print("│   3. = Zone rectangulaire    │")
            print("│                              │")
            print("│   4. = Système de vote       │")
            print("│                              │")
            print("│   5. = Système d'équitation  │")
            print("│                              │")
            print("│   6. = Charge de la batterie │")
            print("│                              │")
            print("│   7. = Arrondi               │")
            print("│                              │")
            print("│   8. = Retour                │")
            print("│                              │")
            print("▣─────────────────────────────▣")

            CalculationMenu = int(input("Veuillez sélectionner l'une des options suivantes 1,2,3,4,5,6: "))

            #Done
            #£ Standard:
            if CalculationMenu == 1:

                N1 = int(input("Entrez le premier numéro: "))
                N2 = int(input("Entrez le deuxième numéro: "))

                print("Entrez quelle opération souhaitez-vous effectuer?:")
                OP = input("Enter One Of These Operations: | + | - | * | / | ")

                Result = 0
                if OP == '+':
                    Result = N1 + N2
                elif OP == '-':
                    Result = N1 - N2
                elif OP == '*':
                    Result = N1 * N2
                elif OP == '/':
                    Result = N1 / N2
                else:
                    print("Le caractère d'entrée n'est pas reconnu.")

                print(N1, OP, N2, "=", Result)
                time.sleep(1)

            #Done
            #£ Converter:
            elif CalculationMenu == 2:
       
                    print("Que voudriez-vous savoir?: ")
                    print("▣───────────────────▣")
                    print("│                   │")
                    print("│  1 = Km - Milles  │")
                    print("│                   │")
                    print("│  2 = Milles - Km  │")
                    print("│                   │")
                    print("│  3 = Kg - Lbs     │")
                    print("│                   │")
                    print("│  4 = Lb - Kg      │")
                    print("│                   │")
                    print("│  5 = Cm - Pouces  │")
                    print("│                   │")
                    print("│  6 = Pouces - Cm  │")
                    print("│                   │")
                    print("│  7 = Retour       │")
                    print("│                   │")
                    print("▣───────────────────▣")

                    unit = int(input("Veuillez sélectionner l'une des options suivantes: 1,2,3,4,5,6: "))

                    if unit == 1:
                        Km = int(input("Combien de km voulez-vous convertir?: "))
                        print(str(Km) + " Km est " + str(Km / 1.609) + " Mi.")
                        time.sleep(1)

                    elif unit == 2:
                        Mi = int(input("Combien de milles voulez-vous convertir?: "))
                        print(str(Mi) + " Mi est " + str(Mi * 1.609) + " Km.")
                        time.sleep(1)

                    elif unit == 3:
                        Kg = int(input("Combien de kg voulez-vous convertir?: "))
                        print(str(Kg) + " Kg est " + str(Kg * 2.205) + " Lb.")
                        time.sleep(1)

                    elif unit == 4:
                        Lb = int(input("Combien de livres voulez-vous convertir?: "))
                        print(str(Lb) + " Lb est " + str(Lb / 2.205) + " Kg.")
                        time.sleep(1)

                    elif unit == 5:
                        Cm = int(input("Combien de cm voulez-vous convertir?: "))
                        print(str(Cm) + " Cm est " + str(Cm / 2.540) + " In.")
                        time.sleep(1)

                    elif unit == 6:
                        In = int(input("Combien voulez-vous convertir?: "))
                        print(str(In) + " In est " + str(In * 2.540) + " Cm.")
                        time.sleep(1)

                    #Done
                    #£ Go back to menu
                    elif unit == 7:
                        Menu()

                    #Done
                    #£ Goes Back To The Main Menu
                    else:
                        Menu()


            #Done
            #£ Rectangle Area:
            elif CalculationMenu == 3:

                    Width = float(input("Veuillez entrer la largeur d'un rectangle: "))
                    Height = float(input("Veuillez entrer la hauteur d'un rectangle: "))

                    Area = Width * Height

                    Perimeter = 2 * (Width + Height)

                    print("Aire d'un rectangle est: %.2f" % Area)
                    print("Périmètre du rectangle est: %.2f" % Perimeter)

            #Done
            #£ Voting System:
            elif CalculationMenu == 4:

                    TotalA = 0
                    TotalB = 0
                    TotalC = 0
                    TotalD = 0
                    TotalE = 0
                    TotalAll = 0
                    Vote = True

                    while Vote == True:

                        Cast = input("Veuillez inscrire votre vote pour le candidat A, B, C, D ou E: ")
                        if Cast == "A" or Cast == "a":
                            TotalA = TotalA + 1
                        elif Cast == "B" or Cast == "b":
                            TotalB = TotalB + 1
                        elif Cast == "C" or Cast == "c":
                            TotalC = TotalC + 1
                        elif Cast == "D" or Cast == "d":
                            TotalD = TotalD + 1
                        elif Cast == "E" or Cast == "e":
                            TotalE = TotalE + 1
                        elif Cast == "End" or Cast == "end":
                            Vote = False

                    print("Votes exprimés pour le candidat A: " + str(TotalA))
                    print("Votes exprimés pour le candidat B: " + str(TotalB))
                    print("Votes exprimés pour le candidat C: " + str(TotalC))
                    print("Votes exprimés pour le candidat D: " + str(TotalD))
                    print("Votes exprimés pour le candidat E: " + str(TotalE))
                    print("Total Amount Of Votes Cast: " + str(TotalA + TotalB + TotalC + TotalD + TotalE))
                    if TotalA > TotalB and TotalC and TotalD and TotalE:
                        print("Le candidat A remporte le sondage.")
                    elif TotalB > TotalA and TotalC and TotalD and TotalE:
                        print("Le candidat B remporte le sondage.")
                    elif TotalC > TotalA and TotalB and TotalD and TotalE:
                        print("Le candidat C remporte le sondage.")
                    elif TotalD > TotalA and TotalB and TotalC and TotalE:
                        print("Le candidat ré remporte le sondage.")
                    elif TotalE > TotalA and TotalB and TotalC and TotalD:
                        print("Le candidat E remporte le sondage.")
                    elif TotalA == TotalB and TotalC and TotalD and TotalE:
                        print("They All Draw.")
                        Menu()

            #Done
            #£ Riding System:
            elif CalculationMenu == 5:
                                ride = 0

                                def progressbar(it, prefix="", size=120, out=sys.stdout): # Python3.3+
                                    count = len(it)
                                    def show(j):
                                        x = int(size*j/count)
                                        print("{}[{}{}] {}/{}".format(prefix, "█"*x, "."*(size-x), j, count), 
                                                end='\r', file=out, flush=True)
                                    show(0)
                                    for i, item in enumerate(it):
                                        yield item
                                        show(i+1)
                                    print("\n", flush=True, file=out)

                                def count():
                                    ride = 0
                                    while ride < 8:
                                        print(" ")
                                        rider = int(input("Veuillez entrer votre taille en cm: "))

                                        if rider >= 140:
                                            print("Veuillez monter.")
                                            ride = ride + 1
                                        elif rider >= 120 and rider < 140:
                                            adult = input("Êtes-vous un adulte o/n: ")
                                            if adult == "y":
                                                print("Veuillez rouler tous les deux!")
                                                ride = ride + 2
                                            else:
                                                print("Pas de trajet!")
                                        else:
                                            print("Pas de trajet!")
                                    print("Le trajet est complet Veuillez patienter.")
                                    print(" ")

                                    for i in progressbar(range(120), "Temps restant: ", 60):
                                        time.sleep(2)

                                count()

            #Done
            #£ Battery:
            elif CalculationMenu == 6:

                BatteryCharge = int(input("Veuillez entrer les frais restants: "))
                if BatteryCharge == 100:
                    print("Complètement chargé.")
                elif BatteryCharge < 100 and BatteryCharge > 0:
                    print("Batterie faible.")

            #Done
            #£ Rounding caculator:
            elif CalculationMenu == 7:
                numIn = float(input("Veuillez saisir votre numéro: "))
                numOut = round(numIn)
                print("Votre nombre arrondi est: ", numOut)

            #Done
            #£ Go back to menu
            elif CalculationMenu == 8:
                Menu()

            #Done
            #£ Goes Back To The Main Menu
            else:
                Menu()


        #Done
        #* Games:
        elif unit == 3:
            print("A quel jeu aimeriez-vous jouer?:")
            print("▣──────────────────────────▣")
            print("│                          │")
            print("│  1 = Navires de combat   │")
            print("│                          │")
            print("│  2 = Coin Flip           │")
            print("│                          │")
            print("│  3 = Connectez quatre    │")
            print("│                          │")
            print("│  4 = Morpion             │")
            print("│                          │")
            print("│  5 = Perte               │")
            print("│                          │")
            print("│  6 = Retour              │")
            print("│                          │")
            print("▣──────────────────────────▣")

            gameSelecte = int(input("Veuillez choisir un jeu dans le menu ci-dessus 1,2,3,4: "))

            #Done
            #£ Battle Ships:
            if gameSelecte == 1:
                
                from random import randint

                class Ship:
                    def __init__(self, size, orientation, location):
                        self.size = size

                        if orientation == 'Horizontal' or orientation == 'Vertical':
                            self.orientation = orientation
                        else:
                            raise ValueError("La valeur doit être 'Horizontale' ou 'Verticale'.")

                        if orientation == 'Horizontal':
                            if location['Row'] in range(row_size):
                                self.coordinates = []
                                for index in range(size):
                                    if location['Col'] + index in range(col_size):
                                        self.coordinates.append({'Row': location['Row'], 'Col': location['Col'] + index})
                                    else:
                                        raise IndexError("Colonne est hors plage.")
                            else:
                                raise IndexError("Ligne est hors plage.")
                        elif orientation == 'Vertical':
                            if location['Col'] in range(col_size):
                                self.coordinates = []
                                for index in range(size):
                                    if location['Row'] + index in range(row_size):
                                        self.coordinates.append({'Row': location['Row'] + index, 'Col': location['Col']})
                                    else:
                                        raise IndexError("Row est Out Of Range.")
                            else:
                                raise IndexError("Colonne est hors plage.")

                        if self.filled():
                            print_board(board)
                            print(" ".join(str(coords) for coords in self.coordinates))
                            raise IndexError("Un navire occupe déjà cet espace.")
                        else:
                            self.fillBoard()

                    def filled(self):
                        for coords in self.coordinates:
                            if board[coords['Row']][coords['Col']] == 1:
                                return True
                        return False

                    def fillBoard(self):
                        for coords in self.coordinates:
                            board[coords['Row']][coords['Col']] = 1

                    def contains(self, location):
                        for coords in self.coordinates:
                            if coords == location:
                                return True
                        return False

                    def destroyed(self):
                        for coords in self.coordinates:
                            if board_display[coords['Row']][coords['Col']] == 'O':
                                return False
                            elif board_display[coords['Row']][coords['Col']] == '*':
                                raise RuntimeError("Affichage du tableau inexact")
                        return True

                row_size = 9  
                col_size = 9  
                num_ships = 4
                max_ship_size = 5
                min_ship_size = 2
                num_turns = 40

                ship_list = []

                board = [[0] * col_size for x in range(row_size)]

                board_display = [["O"] * col_size for x in range(row_size)]

                def print_board(board_array):
                    print("\n  " + " ".join(str(x) for x in range(1, col_size + 1)))
                    for r in range(row_size):
                        print(str(r + 1) + " " + " ".join(str(c) for c in board_array[r]))
                    print()


                def search_locations(size, orientation):
                    locations = []

                    if orientation != 'Horizontal' and orientation != 'Vertical':
                        raise ValueError("L'orientation doit avoir une valeur 'Horizontal' ou 'Vertical'.")

                    if orientation == 'Horizontal':
                        if size <= col_size:
                            for r in range(row_size):
                                for c in range(col_size - size + 1):
                                    if 1 not in board[r][c:c + size]:
                                        locations.append({'Row': r, 'Col': c})
                    elif orientation == 'Vertical':
                        if size <= row_size:
                            for c in range(col_size):
                                for r in range(row_size - size + 1):
                                    if 1 not in [board[i][c] for i in range(r, r + size)]:
                                        locations.append({'Row': r, 'Col': c})

                    if not locations:
                        return 'None'
                    else:
                        return locations


                def random_location():
                    size = randint(min_ship_size, max_ship_size)
                    orientation = 'Horizontal' if randint(0, 1) == 0 else 'Vertical'

                    locations = search_locations(size, orientation)
                    if locations == 'None':
                        return 'None'
                    else:
                        return {'Location': locations[randint(0, len(locations) - 1)], 'Size': size,
                                'Orientation': orientation}


                def get_row():
                    while True:
                        try:
                            guess = int(input("Conjecture de ligne: "))
                            if guess in range(1, row_size + 1):
                                return guess - 1
                            else:
                                print("\nOups, ce n'est même pas dans l'océan.")
                        except ValueError:
                            print("\nVeuillez entrer un numéro")


                def get_col():
                    while True:
                        try:
                            guess = int(input("Conjecture de colonne: "))
                            if guess in range(1, col_size + 1):
                                return guess - 1
                            else:
                                print("\nOups, ce n'est même pas dans l'océan.")
                        except ValueError:
                            print("\nVeuillez entrer un numéro")

                temp = 0
                while temp < num_ships:
                    ship_info = random_location()
                    if ship_info == 'None':
                        continue
                    else:
                        ship_list.append(Ship(ship_info['Size'], ship_info['Orientation'], ship_info['Location']))
                        temp += 1
                del temp


                def play_game():
                    print_board(board_display)

                    for turn in range(num_turns):
                        print("Turn:", turn + 1, "Of", num_turns)
                        print("Ships Left:", len(ship_list))
                        print()

                        guess_coords = {}
                        while True:
                            guess_coords['Row'] = get_row()
                            guess_coords['Col'] = get_col()
                            if board_display[guess_coords['Row']][guess_coords['Col']] == 'X' or \
                                    board_display[guess_coords['Row']][guess_coords['Col']] == '*':
                                print("\nVous l'avez déjà deviné.")
                            else:
                                break

                        ship_hit = False
                        for ship in ship_list:
                            if ship.contains(guess_coords):
                                print("Succès!")
                                ship_hit = True
                                board_display[guess_coords['Row']][guess_coords['Col']] = 'X'
                                if ship.destroyed():
                                    print("Navire détruit!")
                                    ship_list.remove(ship)
                                break
                        if not ship_hit:
                            board_display[guess_coords['Row']][guess_coords['Col']] = '*'
                            print("Vous avez raté!")

                        print_board(board_display)

                        if not ship_list:
                            break

                    if ship_list:
                        print("Tu as perdu!")
                    else:
                        print("Tous Les Navires Sont Coulés. Vous gagnez!")

                play_game()

            #Done
            #£ Coin Flip:
            elif gameSelecte == 2:
                
                import random
                    
                def CoinFlip():
                    NumCoinFlips = int(input("Combien de fois voulez-vous jouer?: "))
                    print()

                    score = 0   

                    for x in range(NumCoinFlips):
                        HeadsOrTails = input("Pile ou face: ")
                        print()
                        FlipResult = random.randint(1, 2)
                        if FlipResult == 1 and HeadsOrTails == "Pile" or HeadsOrTails =="Pile":
                            print()
                            print("Vous avez raison")
                            score = score + 1
                            print ("Ton score est: " + str(score))
                            print()
                            
                        elif FlipResult == 2 and HeadsOrTails == "Tace" or HeadsOrTails == "Tace":
                            print()
                            print("Vous avez raison")
                            score = score + 1
                            print ("Ton score est: " + str(score))
                            print()
                        
                        else:
                            print()
                            print("Wrong")
                            score = score - 1
                            print("Ton score est: " + str(score))
                            print()
                    
                    print("Oui / Non")
                    PlayAgain = input("Voulez-vous rejouer: ")
                    
                    if PlayAgain == "Oui":
                        CoinFlip()

                    elif PlayAgain == "Non":
                        Menu()
                    

                CoinFlip()

            #Done
            #£ Connect 4:                    
            elif gameSelecte == 3:
                board = [] 

                for x in range(6):
                    board.append(["\U0001F532"] * 7) 

                def print_board(board):  
                    for row in board:
                        print (" ".join(row))

                print ('Bienvenue pour connecter quatre')

                player_one = input('Joueur 1. Entrez votre nom: ')
                player_two = input('Joueur 2. Entrez votre nom: ') 

                print ('%s vs. %s' % (player_one, player_two))
                print ('--------------')
                print (print_board(board))
                print ('Joueur 1 est \U0001F7E1 et Joueur 2 est \U0001F534')
                print ('Let\'s play!') 

                turn = 0 

                while turn < 42: 

                    if turn % 2 == 0:  

                        print ('%s. Choisissez une colonne pour déposer votre jeton' % (player_one))
                        one_choice = int(input('Colonne: ')) 

                        if (board[5][one_choice - 1] == '\U0001F532'):             
                            board[5][one_choice - 1] = '\U0001F7E1'
                            print_board(board)
                            turn += 1

                        elif(board[4][one_choice - 1] == '\U0001F532'):
                            board[4][one_choice - 1] = '\U0001F7E1'
                            print_board(board)
                            turn += 1

                        elif(board[3][one_choice - 1] == '\U0001F532'):
                            board[3][one_choice - 1] = '\U0001F7E1'
                            print_board(board)
                            turn += 1

                        elif (board[2][one_choice - 1] == '\U0001F532'):
                            board[2][one_choice - 1] = '\U0001F7E1'
                            print_board(board)
                            turn += 1

                        elif (board[1][one_choice - 1] == '\U0001F532'):
                            board[1][one_choice - 1] = '\U0001F7E1'
                            print_board(board)
                            turn += 1

                        elif (board[0][one_choice - 1] == '\U0001F532'):
                            board[0][one_choice - 1] = '\U0001F7E1'
                            print_board(board)
                            turn += 1

                        else:
                            print ("Colonne est pleine.")      
                    else:         

                        print ('%s. Choisissez une colonne pour déposer votre jeton' % (player_two))
                        one_choice = int(input('Colonne: '))

                        if (board[5][one_choice - 1] == '\U0001F532'):
                            board[5][one_choice - 1] = '\U0001F534'
                            print_board(board)
                            turn += 1

                        elif(board[4][one_choice - 1] == '\U0001F532'):
                            board[4][one_choice - 1] = '\U0001F534'
                            print_board(board)
                            turn += 1

                        elif(board[3][one_choice - 1] == '\U0001F532'):
                            board[3][one_choice - 1] = '\U0001F534'
                            print_board(board)
                            turn += 1

                        elif (board[2][one_choice - 1] == '\U0001F532'):
                            board[2][one_choice - 1] = '\U0001F534'
                            print_board(board)
                            turn += 1

                        elif (board[1][one_choice - 1] == '\U0001F532'):
                            board[1][one_choice - 1] = '\U0001F534'
                            print_board(board)
                            turn += 1

                        elif (board[0][one_choice - 1] == '\U0001F532'):
                            board[0][one_choice - 1] = '\U0001F534'
                            print_board(board)
                            turn += 1

                        else:
                            print ("Colonne est pleine.")

                if turn == 42:
                    print ('Jeu terminé.')

                else:
                    print("Noyau d'erreur: 1")
                    Menu()

            #Done
            #£ Noughts And Crosses:
            elif gameSelecte == 4:
                import random

                class TicTacToe:

                    def __init__(self):
                        self.board = []

                    def create_board(self):
                        for i in range(3):
                            row = []
                            for j in range(3):
                                row.append('-')
                            self.board.append(row)

                    def get_random_first_player(self):
                        return random.randint(0, 1)

                    def fix_spot(self, row, col, player):
                        self.board[row][col] = player

                    def is_player_win(self, player):
                        win = None

                        n = len(self.board)

                        for i in range(n):
                            win = True
                            for j in range(n):
                                if self.board[i][j] != player:
                                    win = False
                                    break
                            if win:
                                return win

                        for i in range(n):
                            win = True
                            for j in range(n):
                                if self.board[j][i] != player:
                                    win = False
                                    break
                            if win:
                                return win

                        win = True
                        for i in range(n):
                            if self.board[i][i] != player:
                                win = False
                                break
                        if win:
                            return win

                        win = True
                        for i in range(n):
                            if self.board[i][n - 1 - i] != player:
                                win = False
                                break
                        if win:
                            return win
                        return False

                        for row in self.board:
                            for item in row:
                                if item == '-':
                                    return False
                        return True

                    def is_board_filled(self):
                        for row in self.board:
                            for item in row:
                                if item == '-':
                                    return False
                        return True

                    def swap_player_turn(self, player):
                        return 'X' if player == 'O' else 'O'

                    def show_board(self):
                        for row in self.board:
                            for item in row:
                                print(item, end=" ")
                            print()

                    def start(self):
                        self.create_board()

                        player = 'X' if self.get_random_first_player() == 1 else 'O'
                        while True:
                            print(f"Joueur {player} Tour")

                            self.show_board()

                            row, col = list(
                                            map(int, input("Entrez les numéros de ligne et de colonne pour fixer le point, par exemple 1 1 ou 3 3: ").split()))
                            print()

                            self.fix_spot(row - 1, col - 1, player)

                            if self.is_player_win(player):
                                print(f"Player {player} Gagne le jeu!")
                                break

                            if self.is_board_filled():
                                print("Match nul!")
                                break

                            player = self.swap_player_turn(player)

                        print()
                        self.show_board()


                tic_tac_toe = TicTacToe()
                tic_tac_toe.start()

            #Done
            #£ Doom and Doom inports:
            elif gameSelecte == 5:
                try:
                    import main
                    import pygames
                    import numba
                    print("Pour modifier les paramètres, ouvrez settings.py")
                    print("En course")
                    import main
                except ModuleNotFoundError:
                    print("'Doom' n'est pas installé")
                    print("Télécharger depuis: lien")
                    print("Vous devrez peut-être installer pygame et numba")
                    print("pip install pygame")
                    print("pip install numba")
                    time.sleep(1)

                
                


            #Done
            #£ Go back to menu
            elif gameSelecte == 6:
                Menu()

            #Done
            #£ Goes Back To The Main Menu
            else:
                Menu()

        #Done
        #* Code d'erreurs:
        elif unit == 4:

            print("▣────────────────────────────────────────────▣")
            print("│                                             │")
            print("│   1. = Option/choix invalide                │")
            print("│                                             │")
            print("│   2. = Nom d'utilisateur ou Pass invalide   │")
            print("│                                             │")
            print("│   3. = Entrée invalide                      │")
            print("│                                             │")
            print("▣────────────────────────────────────────────▣")
            
            print()
            print("Please Wait")
            time.sleep(2)
            Menu()

        #Done
        #£ Exits AIO
        elif unit == 5:
            sys.exit()
UserPass()

def versionChecker():
    version = platform.python_version()
    part1 = version[2]
    part2 = version[3]
    part3 = version[0]

    if int(part1) >= 7 and int(part2) != "." and int(part3) == 3:
        UserPass()

    else:
        print("veuillez utiliser AIO 3.6 Edition.py ou Python 3.7")
versionChecker()