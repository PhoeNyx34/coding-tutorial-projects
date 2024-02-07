import random

word_list = ['gravy','subtle','confusion','light','space','twinkle','simple','strategy','crave','proud']
logged_guesses = []
incorrect_guesses = 0

print("Welcome to Hangman!\nOne moment while I generate a word...\n")

# randomly choose a word from the list
word_index = random.randint(0,len(word_list)-1)
chosen_word = word_list[word_index]

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
    while incorrect_guesses < 6:
        if s.join(correct_guess) != s.join(answer):
            print(f"Your guess: {s.join(correct_guess)}")

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
                print("No match")
                incorrect_guesses +=1
        else:
            print(f"Congratulations! You've guessed the correct word: {chosen_word}") 
            game_on = False
            break
    
    if incorrect_guesses == 6 and s.join(correct_guess) != s.join(answer):
        print("Out of tries. Game over!")
        break





