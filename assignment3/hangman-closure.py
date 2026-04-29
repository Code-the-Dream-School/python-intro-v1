def hangman_game(word):
    word = word.lower()
    guessed_letters = []

    def guess(letter):
        letter = letter.lower()
        if letter in guessed_letters:
            return f"You already guessed '{letter}'."
        
        guessed_letters.append(letter)
        
        display_word = [char if char in guessed_letters else "_" for char in word]
        
        if letter in word:
            return f"Correct! {' '.join(display_word)}"
        else:
            return f"Incorrect. {' '.join(display_word)}"
            
    return guess

play = hangman_game("Python")
print(play("p"))
print(play("y"))
print(play("z"))
print(play("p"))
