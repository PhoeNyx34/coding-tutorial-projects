import random
from hangman_words import word_list
import hangman_art

logged_guesses = []
lives = 6

print(f"Welcome to Hangman!{hangman_art.logo}\n\nOne moment while I generate a word...\n")

# randomly choose a word from the list
chosen_word = random.choice(word_list)

# split word into array of letters
answer = []
correct_guess = []
for letter in chosen_word:
    answer.append(letter)
    correct_guess.append('_ ')
s = ''

print(f"All set! I'm thinking of the word: {s.join(correct_guess)}")

# check if correct_guess matches answer

game_on = True

while game_on:
    while lives > 0:
        if s.join(correct_guess) != s.join(answer):
            print(f"Current letters: {s.join(correct_guess)}")
            print(hangman_art.stages[lives])

        # ask the user to guess a letter
            guess = input("Guess a letter: ").lower()
            while guess in logged_guesses:
                guess = input(f"You've already guessed {guess}. Guess a different letter: ").lower()
            
            logged_guesses.append(guess)

            # check if the letter is in array
            letter_match = []
            for i in range(0,len(answer)):
                if answer[i] == guess:
                    letter_match.append('match')
                    correct_guess[i] = guess
                else:
                    letter_match.append('false')
            
            if not 'match' in letter_match:
                print("No match\n\n")
                lives -=1
        else:
            print(f"Congratulations! You've guessed the correct word: {chosen_word}") 
            game_on = False
            break
    
    if lives == 0 and s.join(correct_guess) != s.join(answer):
        print(hangman_art.stages[0])
        print("Out of tries. Game over!")
        break





