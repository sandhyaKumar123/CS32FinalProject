#Play Hangman- Script to provide single and multiplayer options
import os
print("+++ WELCOME TO HANGMAN +++")
mode = input("Choose mode: [1] Single Player  [2] Multiplayer: ")

while True:
    #if single player, open our sinlge player file
    if mode == '1':
        os.system("python3 FPSingle.py")
        break
    #if multi-player, open our multiplayer option
    #specify roles
    elif mode == '2':
        role = input("Are you [1] Word Picker (server) or [2] Guesser (client)? ")
        while True:
            if role == '1':
                print('Open a split terminal and run: python3 FPClient.py')
                os.system("python3 FPServer.py") #open server
                break
            elif role == '2':
                print('Before continuing ensure the server is running in a seperate terminal.')
                print('To do this, open a split terminal and run: python3 FPServer.py')
                ready = 'run'
                while True:
                    ready = input('Type ok in this terminal once server is running!')
                    if ready == 'ok':
                        os.system("python3 FPClient.py") #open file
                        break
                    else:
                        print('Waiting... please type ok once server is running.')
                break
            else: #ensure valid input
                role = input("Invalid option. Please choose 1 or 2: ")
        break

    else: #ensure valid input
        mode = input("Invalid option. Please choose 1 or 2: ")

