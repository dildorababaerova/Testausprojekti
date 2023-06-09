import random
import unittest
runtest=1

def yhdeksanhenkea(guess_test):
    lives = 9
    words = ['pizza', 'keiju', 'kieli', 'paita', 'sorsa', 'kirje']
    if runtest ==0:
        secret_word = random.choice(words)
    if runtest ==1:
        secret_word = guess_test
    print(secret_word)

    clue = list('?????')
    heart_symbol = u'\u2764'
    guessed_word_correctly = False
    def update_clue(guessed_letter, secret_word, clue):
        index = 0
        while index < len(secret_word):
            if guessed_letter == secret_word[index]:
                clue[index] = guessed_letter
            index = index + 1


    while lives > 0:
        print(clue)
        print('Henkiä jäljellä: ' + heart_symbol * lives)
        if runtest ==0:
            guess = input ('Arvaa kirjain tai koko sana: ')
        if runtest ==1:
            guess = secret_word

        if guess in secret_word:
            update_clue (guess, secret_word, clue)
            clue_str = ''.join(clue)

        #Jos arvaus on väärä (else), henkien määrä pienenee yhdellä. 
        else:
            print ('Väärin. Menetit yhden hengen.' )
            lives = lives - 1
            if lives == 0:
                print('Hävisit! Salainen sana oli ' + secret_word)
        if guess == secret_word or clue_str == secret_word:
            guessed_word_correctly = True
            if guessed_word_correctly:
                print('Voitit! Salainen sana oli ' + secret_word)
                return secret_word
        

if runtest == 0:
    yhdeksanhenkea('')

class test_yhdeksanhenkea(unittest.TestCase):
    def test_yhdeksanhenkea_saccess(self):
        actual = yhdeksanhenkea('pizza')
        expected = ['pizza', 'keiju', 'kieli', 'paita', 'sorsa', 'kirje']
        print('actual= ', actual)
        self.assertIn(actual, expected)

    def test_yhdeksanhenkea_saccess2(self):
         actual = yhdeksanhenkea('keiju')
         expected = ['pizza', 'keiju', 'kieli', 'paita', 'sorsa', 'kirje']
         print('actual= ', actual)
         self.assertIn(actual, expected)

    def test_yhdeksanhenkea_saccess3(self):
         actual = yhdeksanhenkea('kieli')
         expected = ['pizza', 'keiju', 'kieli', 'paita', 'sorsa', 'kirje']
         print('actual= ', actual)
         self.assertIn(actual, expected)

    def test_yhdeksanhenkea_saccess4(self):
         actual = yhdeksanhenkea('paita')
         expected = ['pizza', 'keiju', 'kieli', 'paita', 'sorsa', 'kirje']
         print('actual= ', actual)
         self.assertIn(actual, expected)

    def test_yhdeksanhenkea_saccess5(self):
         actual = yhdeksanhenkea('sorsa')
         expected = ['pizza', 'keiju', 'kieli', 'paita', 'sorsa', 'kirje']
         print('actual= ', actual)
         self.assertIn(actual, expected)

    def test_yhdeksanhenkea_saccess6(self):
         actual = yhdeksanhenkea('kirje')
         expected = ['pizza', 'keiju', 'kieli', 'paita', 'sorsa', 'kirje']
         print('actual= ', actual)
         self.assertIn(actual, expected)