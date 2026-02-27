import random


decision = int(input("What do you choose? Type 0 for rock, 1 for paper or 2 for sccissors \n"))


random_number = random.randint(0, 2)

def choice(option):
    match option:
        case 0:
                print("""
                _______7
            ---'   ____)
                  (_____)
                  (_____)
                  (____)
            ---.__(___)
            """)

        case 1:
            print("""
                 _______
            ---'    ____)____
                       ______)
                      _______)
                     _______)
            ---.__________)
            """)
        case 2:
            print("""
                _______
            ---'   ____)____
                      ______)
                   __________)
                  (____)
            ---.__(___)
            """)

print("\nYou chose: ")
choice(decision)

print("\nComputer Chose: ")
choice(random_number)

def rules(player, computer):
    if player == computer:
        return "Draw"
    elif (player == 0 and computer == 2)  or (player == 1 and computer == 0) or (player == 2 and computer == 1):
            return "You Win"

    else:
           return "you lose"

winner = rules(decision, random_number)
print(winner)
