import random

l1 = ['It was very effective\nOpponent Died', 'Opponents attack was very effective\n You died']
choice = random.choice(l1)
if choice == l1[0]:
        print("It was very effective.. health lowered to..")
elif choice == l1[1]:
        print("Oppenent attack was very effective.. health lowered to..")