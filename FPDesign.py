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
                output += letter # add the correct letter or dash, depedning on the match
            else: #add dash for letters not guessed
                output+="-" or # dash, depedning on the match
        else:
            output +=displayWord[i]
    return output # return the updated dispaly string

#Once we have our word, we want the Hangman game to take in a set number of responses
#For our final project we want to incorporate an illustration, but for now we will use words

#define our hangmnan game...
def hangman():
    gameWord = chooseWord() #define our word using the chooseword function
    guessedLetters = [] #keep a reccord of letters already guessed to avoid repeats
    play = True #variable telling us to play or not play... keeps the game running (True) or stops it (False).
    bodyParts = [] # list of parts already added to the hangman
    bodyPartsRemaining = ["Head", "Body", "Left Arm", "Right Arm", "Left Leg", "Right Leg"] # list of parts still left before losing


    print("+++ WELCOME TO HANGMAN +++")
    displayWord = '-'*len(gameWord) #output of our word.... Create displayWord made of dashes, one for each letter in the word.
    print(displayWord) # Show the dashed word so the player knows how many letters they’re trying to guess.

    while play: #while we are still playing the game... Start a loop that repeats asking for guesses until the game is won or lost; input is always forced to lowercase.
        guess = input("Guess a letter: ").lower()

        if guess.isalpha() == False: #check to see if input is letter or probe further ... If the input isn’t alphabetical (e.g., numbers or punctuation), tell the player and skip the rest of the loop.
            print("Please enter a single letter.")
            continue

        if guess in guessedLetters: #ensure letter has not been already guessed
            print("You guessed that letter. Please choose a letter you have not guessed.")
            continue

        guessedLetters.append(guess) #add gussed letter to reccord of letters already guessed

        if guess in gameWord: #if the letter is in our guessed word
            print("Good guess! This letter is in the word!")
            displayWord = updateWord(displayWord,gameWord, guess) #update the output... Call updateWord() to reveal all spots where the letter belongs.
            print(displayWord) #print the updated dashed output
            if "-" not in displayWord: # If there are no more dashes left (all letters guessed), announce victory and exit the loop.
                print("Congratulations! You guessed the word!") #check to see if the display is all letters, that means the game is over
                break
        else: # If the guess is wrong:
            bodyParts.append(bodyPartsRemaining[0]) #change our list of body parts remaining
            bodyPartsRemaining.pop(0) #remove the body part used
            print(f"Incorrect guess. Your hangman has a: " + str(bodyParts)) #pront out the body parts the hangman has
            if len(bodyPartsRemaining) == 0: # If no body parts are left, end the game by setting play to False.
                play = False
    if play == False: # After losing (running out of attempts), reveal what the correct word was.
        print(f"You ran out of attempts. The word was {gameWord}!") #if the hangman is built the game ends

if __name__ == "__main__":
    hangman()

## TO DO ##
#use external dictionary, either from internet or csv file
#Create a visual of our hangman
#generate a client server option for multiple players

# choosewords function to csv file or server of smth online... so that theres

# now we have list of body parts using -- but isntead of listing them, we'll use them as keys in a dictionary to have a betterv isual outptu

# well split into client and server to have a mutliplayer game


