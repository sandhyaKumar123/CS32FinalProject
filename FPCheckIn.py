
#We used several online hangman models to help shape our approach

#Create a list of words to choose from, and randomly choose one
#import random to help choose a word
import random

#using an external dictionary
#use random word
from random_word import RandomWords #note need to run pip install random-word in terminal

def chooseWord():
    #create a RandomWords instance
    inst = RandomWords()
    #get a random word
    gameWord = inst.get_random_word()
    return gameWord.lower()

#function to update if a letter in the word was guessed
def updateWord (displayWord, gameWord, letter): #takes parameter word and letter
    output = ''
    for i in range(len(gameWord)): #add letter to word output if guessed correctly
        if displayWord[i] == '-':
            if gameWord[i] == letter:
                output += letter
            else: #add dash for letters not guessed
                output+="-"
        else:
            output +=displayWord[i]
    return output

#a function for visual output
#create dictionary of images
import os
from PIL import Image
personImages = {}

parts = ["Head", "Body", "Left Arm", "Right Arm", "Left Leg", "Right Leg"]
folderPath = '/workspaces/CS32FinalProject/CS32FP Images'

for i in range(len(parts)):
    personImages[parts[i]] = folderPath+'/'+str(i+1)+'.jpg'


def showMan(part, step):
    image = Image.open(personImages[part])
    output_folder = 'images'
    os.makedirs(output_folder, exist_ok=True)  # make sure 'images' folder exists
    output_path = f'{output_folder}/hangman_step{step}.png'
    image.save(output_path)
    print(f"Saved hangman image: {output_path}")
    image.show()

#a function that will clear the images folder
import glob
def clearImages():
    files = glob.glob('images/hangman_step*.png')
    for f in files:
        os.remove(f)


#Once we have our word, we want the Hangman game to take in a set number of responses
#For our final project we want to incorporate an illustration, but for now we will use words

#define our hangmnan game
def hangman():
    #make sure clear visual output
    clearImages()

    gameWord = chooseWord() #define our word
    guessedLetters = [] #keep a reccord of letters already guessed
    play = True #variable telling us to play or not play
    bodyParts = []
    bodyPartsRemaining = parts


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
            print(f"Incorrect guess. Your hangman has a: " + str(bodyParts)) #print out the body parts the hangman has
            showMan(bodyParts[-1], len(bodyParts))
            if len(bodyPartsRemaining) == 0:
                play = False
    if play == False:
        print(f"You ran out of attempts. The word was {gameWord}!") #if the hangman is built the game ends

if __name__ == "__main__":
    hangman()

## TO DO ##
#use external dictionary, either from internet or csv file -done
#Create a visual of our hangman -done
#generate a client server option for multiple players
