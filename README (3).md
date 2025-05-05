# CS32FinalProject
Final Project for CS32 for Sandhya Kumar and Gabi Poniz

This is a single-player and multiplayer hangman game. For the single-player option, our code chooses a word from a dictionary, from an external source, and for the multiplayer option, one player has a choice to enter a word, and the other guesses what the word is. We would have two kinds of visual displays, similar to a typical hangman game. The first draws the head, arm, legs, and body of a person in the terminal with characters. The second generates an image added to a folder.

Instructions:
1. Download the FPSingle.py, FPClient.py, FPServer.py, hangmanPrint.py, PlayHangman.py, and CS32FP Images files.
2. Run pip install random-word in terminal, as we use the random-words package in our code.
3. Run PlayHangman.py script.
4. Follow terminal instructions.
    a. If single player, the script will open and run FPSingle.py
    b. If multiplayer:
            i. If you choose to be the word picker, the script will run the FPServer.py script, and you need to run the FPClient.py script in a seperate bash terminal.
            ii. If you choose to be the word guesser, the script will prompt you to run the FPServer.py script in a seperate bash terminal. After doing this type 'ok' in the original terminal, at which point the script witll run FPClient.py.
5. To view images as you go, refer to the images folder, which will be populated each time a player guesses an incorrect letter.
6. Play again!

Scripts:

FPSingle: A single-player Hangman game.

FPClient: A multiplayer Hangman game, where this player is the one guessing letters.

FPServer: A multiplayer Hangman game, where this player is the one choosing the word.

hangmanPrint: A file containing an character print version of the hangman figures, and a function to print them. This script was modified from <script src="https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c.js"></script>.

PlayHangman: A script to setup single player or nultiplayer game options. For multiplayer
you would need to run the client or server as specified in a seperate window.

We used AI sparingly in this, and where it was used is acknowldeged in our code. Mainly it was used to help us figure out our image modification and output, as well as debug any code that wasn't working.

Images is a folder of the visual output. We would like to try and make this a GUI that updates. This seems difficult on GitHub though!
