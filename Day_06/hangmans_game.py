import random
word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
print(chosen_word)
display = []
life = 6
for _ in range(len(chosen_word)):
    display.append("_")

while life > 0:
    guess = input("Guess a letter: ").lower()
    
    # Se a letra escolhida estiver na palavra, atualiza o display
    if guess in chosen_word:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
    # Se não estiver na palavra, perde apenas UMA vida
    else:
        life -= 1
        
    print(f"Word: {' '.join(display)}")
    print(f"Lifes: {life}")

    # Checa se o jogador venceu
    if "_" not in display:
        print("You win!")
        break
        
# Se sair do while e o jogador não tiver ganho, significa que a vida zerou
if life == 0:
    print("You lose!")
