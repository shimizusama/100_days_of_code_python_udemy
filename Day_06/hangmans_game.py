import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
for _ in range(len(chosen_word)):
    display.append("_")
life = 6
while life > 0:
    guess = input("Guess a letter: ").lower()
    length = len(chosen_word)
    tam_word = ""

    for i in range(length):
        tam_word += "_"
        display = ""

        for letter in chosen_word:
            if letter == guess:
                display += letter
            else:
                display += "_"
                life -= 1

        if "_" not in display:
            print("You win!")
            break
print(tam_word)

print (length)




print(display)