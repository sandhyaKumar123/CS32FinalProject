#We outline a rough idea of how a single-player Hangman Game may work!
#We used several online hangman models to help shape our approach

#Create a list of words to choose from, and randomly choose one
#For our actual project we aim to do this with an external dictionary, but for now, we defined a list of words

#import random to help choose a word
import random

# Define a function to pick a random word from a list and return it in lowercase.
def chooseWord():
    words = ["Hello", "Welcome", "To", "Our", "Hangman", "Game" ] # create a list of words they can choose from
    gameWord = random.choice(words) # choose one of the words randomly
    return gameWord.lower() # convert the word to lowercase so that an inputted capital or lowercase doesn't cause problems

#function to update if a letter in the word was guessed
def updateWord (displayWord, gameWord, letter): #takes parameter word and letter ... updates hidden word display when the player makes a correct guess
    output = '' # start with empty string that builds up to new version of the word
    for i in range(len(gameWord)): #add letter to word output if guessed correctly # go thru each position of the word, one letter at a time
        if displayWord[i] == '-': # only update the dash positions, and ignore already revealed letters
            if gameWord[i] == letter: # if teh guessed letter matches teh letter at that position, reveal it
                output += letter # add the correct letter or match, depending on the dash 
            else: #add dash for letters not guessed
                output+="-"
        else:
            output +=displayWord[i]
    return output

#Once we have our word, we want the Hangman game to take in a set number of responses
#For our final project we want to incorporate an illustration, but for now we will use words

#define our hangmnan game
def hangman():
    gameWord = chooseWord() #define our word
    guessedLetters = [] #keep a reccord of letters already guessed
    play = True #variable telling us to play or not play
    bodyParts = []
    bodyPartsRemaining = ["Head", "Body", "Left Arm", "Right Arm", "Left Leg", "Right Leg"]


    print("+++ WELCOME TO HANGMAN +++")
    displayWord = '-'*len(gameWord) #output of our word
    print(displayWord) #header

    while play: #while we are still playing the game
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() == False: #check to see if input is letter or probe further
            print("Please enter a single letter.")
            continue

        if guess in guessedLetters: #ensure letter has not been already guessed
            print("You guessed that letter. Please choose a letter you have not guessed.")
            continue

        guessedLetters.append(guess) #add gussed letter to reccord of letters already guessed

        if guess in gameWord: #if the letter is in our guessed word
            print("Good guess! This letter is in the word!")
            displayWord = updateWord(displayWord,gameWord, guess) #update the output
            print(displayWord) #print the updated dashed output
            if "-" not in displayWord:
                print("Congratulations! You guessed the word!") #check to see if the display is all letters, that means the game is over
                break
        else:
            bodyParts.append(bodyPartsRemaining[0]) #change our list of body parts remaining
            bodyPartsRemaining.pop(0) #remove the body part used
            print(f"Incorrect guess. Your hangman has a: " + str(bodyParts)) #pront out the body parts the hangman has
            if len(bodyPartsRemaining) == 0:
                play = False
    if play == False:
        print(f"You ran out of attempts. The word was {gameWord}!") #if the hangman is built the game ends

if __name__ == "__main__":
    hangman()

## TO DO ##
#use external dictionary, either from internet or csv file
#Create a visual of our hangman
#generate a client server option for multiple players

