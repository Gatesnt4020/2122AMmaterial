import socket, select, errno

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT=1234
myUsername = input('Username: ')

#creating the socke
clientSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#conection to the interwebs
clientSocket.connect((IP,PORT))

#we do not want any messaged block
clientSocket.setblocking(False)

#putting together our message
username = myUsername.encode('utf-8')
usernameHeader = f"{len(username):<{HEADER_LENGTH}}".encode('utf-8')
clinetSocket.send(usernameHeader + username)

while True:
    message = input(f'{myUsername} > ') #> is alignment
    if message:
        message = message.encode('utf-8')
        messageheader = f"{len(message):<{HEADER_LENGTH}}".encode('utf-8')
        clientSocket.send(messageHeader+message)
        try:        #prcessing data fomr the server
            while True:
                usernameHeader = clinetSocket.recv(HEADER_LENGTH)
                if not len(usernameheader):
                    print("closed connection")
                    sys.exit()  #close the program
                    
                usernameLength = int(usernameLength.decode('utf-8').strip())
                username = clinetSocket.recv(usernameLength).decode('utf-8')

                messageHeader = clinetSocket.recv(HEADER_LENGTH)                
                messageLength = int(messageLength.decode('utf-8').strip())
                message = clinetSocket.recv(messageLength).decode('utf-8')
                
                print(f'{username} > {message}')
        except IOError as e:
            print(e)
            continue
        except Exception as e:
            print(e)
            sys.exit()