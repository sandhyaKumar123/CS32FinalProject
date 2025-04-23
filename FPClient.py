import socket
from FPSingle import updateWord, showMan, clearImages, parts

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

def main():
    # Client-side logic
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))  # Connect to the server
        except ConnectionRefusedError:
            print("Could not connect to server. Make sure the word picker (server) is running.")
            return

        gameWord = s.recv(1024).decode()  # Receive the word from the server
        displayWord = '-' * len(gameWord)
        guessedLetters = []
        play = True
        bodyParts = []
        bodyPartsRemaining = parts

        clearImages()

        print("+++ HANGMAN MULTIPLAYER +++")
        print(displayWord)

        while play:
            guess = input("Guess a letter: ").lower()

            if not guess.isalpha() or len(guess) != 1:
                print("Please enter a single letter.")
                continue

            if guess in guessedLetters:
                print("Already guessed that one.")
                continue

            s.sendall(guess.encode())  # Send the guess to the server
            guessedLetters.append(guess)

            if guess in gameWord:
                print("Good guess!")
                displayWord = updateWord(displayWord, gameWord, guess)
                print(displayWord)
                if "-" not in displayWord:
                    print("You win!")
                    done = 'exitw'
                    break
            else:
                bodyParts.append(bodyPartsRemaining[0])
                bodyPartsRemaining.pop(0)
                print(f"Incorrect! Parts: {bodyParts}")
                showMan(bodyParts[-1], len(bodyParts))
                if len(bodyPartsRemaining) == 0:
                    play = False

        if not play:
            print(f"Game over! The word was: {gameWord}")
            done = 'exitl'

        s.sendall(done.encode())  # Send "exit" to the server

if __name__ == '__main__':
    main()
