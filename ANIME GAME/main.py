# import time
import random


# health='===================='

class Anime():
    def __init__(self, name, moves, m2, health):

        self.name = name
        self.moves = moves
        self.m2 = m2
        # self.ui = ui
        # self.computer_choice = computer_choice
        self.health = health
        health = '=========='

    def Anime_char(self):
        self.names = ["Naruto", "Sukuna", "Luffy", "Deku"]
        self.ui = input(f"Which character do you want to choose?\n {self.names}: ")
        print(f"You chose {self.ui}")
        self.computer_choice = (random.choice(self.names))
        print(f"Opponent chose {self.computer_choice}")
        # self.computer_choice = (random.choice(self.names))
        # print(f"Opponent chose {self.computer_choice}")

    def Naruto(self):
        # hp = print
        self.moves = ['1.Rasengan\n', '2.Rasenshuriken\n', '3.Kyuubi Charkra form']
        if self.ui == "Naruto":
            self.m1 = int(input(f"Which move do you want to use?\n {self.moves}"))
            if self.m1 == 1:
                print(f"{self.ui} used Rasengan...")
            elif self.m1 == 2:
                print(f"{self.ui} used Rasenshuriken...")
            elif self.m1 == 2:
                print(f"{self.ui} used Kyuubi Chakra form...")
        else:
            print("")

    def Sukuna(self):
        self.moves = ['1.Incarnation\n', '2.Reverse Cursed Technique\n', '3.Dismantle']
        if self.ui == "Sukuna":
            self.m2 = int(input(f"Which move do you want to use?\n {self.moves}"))
            if self.m2 == 1:
                print(f"{self.ui} used Incarnation...")
            elif self.m2 == 2:
                print(f"{self.ui} used Reverse Cursed Technique...")
            elif self.m2 == 2:
                print(f"{self.ui} used Dismantle...")
        else:
            print("")

    def Luffy(self):
        self.moves = ['1.Gomu no Gatling\n', '2.Gomu no Pistol\n', '3.Gomu no Rocket']
        if self.ui == "Luffy":
            self.m2 = int(input(f"Which move do you want to use?\n {self.moves}"))
            if self.m2 == 1:
                print(f"{self.ui} used Gomu no Gatling...")
            elif self.m2 == 2:
                print(f"{self.ui} used Gomu no Pistol...")
            elif self.m2 == 2:
                print(f"{self.ui} used Gomu no Rocket...")
        else:
            print("")

    def Deku(self):
        self.moves = ['1.Detroit Smash\n', '2.Full Cowl\n', '3.Double Detroit Smash']
        if self.ui == "Deku":
            self.m2 = int(input(f"Which move do you want to use?\n {self.moves}"))
            if self.m2 == 1:
                print(f"{self.ui} used Detroit Smash...")
            elif self.m2 == 2:
                print(f"{self.ui} used Full Cowl...")
            elif self.m2 == 2:
                print(f"{self.ui} used Double Detroit Smash...")
        else:
            print("")

    def Opponent(self):
        self.moves = ['Rasengan', 'Rasenshuriken', 'Kyuubi Charkra form']
        if self.computer_choice == "Naruto":
            randoom = random.choice(self.moves)
            print(f"Opponent used {randoom}.")


        else:
            print("")

        self.moves = ['Incarnation', 'Reverse Cursed Technique', 'Dismantle']
        if self.computer_choice == "Sukuna":
            randoom = random.choice(self.moves)
            print(f"Opponent used {randoom}.")
        else:
            print("")

        self.moves = ['Gomu no Gatling', 'Gomu no Pistol', 'Gomu no Rocket']
        if self.computer_choice == "Luffy":
            randoom = random.choice(self.moves)
            print(f"Opponent used {randoom}.")
        else:
            print("")

        self.moves = ['Detroit Smash', 'Full Cowl', 'Double Detroit Smash']
        if self.computer_choice == "Deku":
            randoom = random.choice(self.moves)
            print(f"Opponent used {randoom}.")
        else:
            print("")

    def Attack(self):
        # self.health = 10
        # while self.health < 0:
         if self.ui == "Naruto" or self.ui == "Sukuna" or self.ui == "Luffy" or self.ui == "Deku" and self.computer_choice == "Sukuna" or self.computer_choice == "Naruto" or self.computer_choice == "Luffy" or self.computer_choice == "Deku":
            l1 = ['It was very effective\nOpponent Died', 'Opponents attack was very effective\n You died']
            choice = random.choice(l1)
            # print(choice)
            if choice == l1[0]:
                print(f"Your opponents health lowered to ")
            else:
                print(f"Your health lowered to ")
        # else:
        #     print("nothing happened")


Anime.Anime_char(Anime)
Anime.Naruto(Anime)
Anime.Sukuna(Anime)
Anime.Luffy(Anime)
Anime.Deku(Anime)
Anime.Opponent(Anime)
Anime.Attack(Anime)
