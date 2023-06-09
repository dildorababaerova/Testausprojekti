# Yhdeksän henkeä 

import random 

  

lives = 9 
words = ['pizza', 'keiju', 'kieli', 'paita', 'sorsa', 'kirje'] 
secret_word = random.choice(words) 
# print(secret_word) 

clue = '?????'

heart_symbol = u'♥'  
guessed_word_correctly = False 

def update_clue(guessed_letter, secret_word, clue): 
    """Updates the clue pattern according to the guess

    Args:
        guessed_letter (str): letter or word given
        secret_word (str): word to check against
        clue (list): letter pattern (list of characters)
    Returns:
        list: updated clue pattern
    """
    index = 0 
    while index < len(secret_word): 
        if guessed_letter == secret_word[index]: 
            clue[index] = guessed_letter 
        index = index + 1 
    updated_clue = clue
    return updated_clue

#Prevent this module to be run by other modules tests

if __name__ == "__main__":
    

    while lives > 0: 
        print
        print(clue) 
        print('Henkiä jäljellä: ' + heart_symbol * lives) 
        guess = input('Arvaa kirjain tai koko sana: ') 
        
        if guess in secret_word: 
            update_clue(guess, secret_word, clue) 

        else: 
            print('Väärin. Menetit yhden hengen.') 
            lives = lives - 1 
            if lives == 0: 
                print('Hävisit! Salainen sana oli ' + secret_word) 

        if guess == secret_word: 
            guessed_word_correctly = True 
            #print(guessed word correctly) 

            if guessed_word_correctly: 
                print('Voitit! Salainen sana oli ' + secret_word) 
                break 