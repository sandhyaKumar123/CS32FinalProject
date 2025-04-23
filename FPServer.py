import socket
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM)  as s:
        # Bind socket to address and publish contact info
        s.bind((HOST, PORT))
        s.listen()
        print("HANGMAN server started. Listening on", (HOST,PORT))

        # Answer incoming connection
        conn2client, addr = s.accept()
        print('Connected by', addr)

        with conn2client:
            word = input("Enter the word for the other player to guess: ").lower()
            conn2client.sendall(word.encode())

            while True:
                guess = conn2client.recv(1024).decode()
                if guess.lower()[0:4] == 'exit':
                    if guess.lower()[-1] == 'w':
                        print("You Loose! Game ended.")
                        break
                    else:
                        print("You Win! Game ended.")
                        break
                print(f"Opponent guessed: {guess}")

    conn2client.close()

if __name__ == '__main__':
    main()




