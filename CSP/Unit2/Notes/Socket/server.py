import socket, select

HEADER_LENGTH = 10
IP = "127.0.0.1"
PORT=1234

serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#help deal when we have 2 address being used
serverSocket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,2)

serverSocket.bind((IP,PORT))
serverSocket.listen()
print(f'Listening for connections on {IP}:{PORT}...')

#dictionary of the clinets
clinets={}
#list of all of the sockets
socketsList = [serverSocket]

def reveiveMessage(clinetSocket):
    # try to process a good message
    try:
        messageheader = clinetSocket.revc(HEADER_LENGTH)
        print(messageheader)
        #check if our clinet loses connection
        if not (len(messageHeader)):
            return False
        messageLength = int(messageHeader.decode('utf-8').strip())
        return {'header':messageheader,'data':clinetSocket.recv(messageLength)}
    except:
    # if not good,
        return False

while True:
    readerSocket, _, exveptionSocket = select.select(socketsList,[],socketsList)
    
    for notifiedSocket in readSocket:
        #if the notified socket is our server socket, we have a new connecton
        if notifiedsocket == serverSocket:
            clinetSocket,clinetAddress = serverSocket.accept()
            user = reveiveMessage(clinetSocket)
            if user is False:
                continue
            socketsList.append(clinetSocket)
            clinets[clinetSocket]=user
            print('Accepted new connection form {},{}, username: {}'.format(*clinetAddress,user['data'].decode('utf-8')))
        #else we have an old connection or a new message
        else:
            message = receiveMessage(notifiedSocket)
            if message is False:
                #we have lost connectio to a clinet
                print('Closed connection from: {}'.format(client[notifiedSocket]['data'].decode('utf-8')))
                socketsList.remove(notifiedSocet)
                del client[notifiedSocket]
                continue
        user = clinets[notifiedSocket]
        print(f'Received message from {user["data"].decode("utf-8")}')
        print(f'\t{message["data"].decode("utf-8")}')
        
        for clinetSocket in clients:
            if clinetSocket != notifiedSocket:
                clientSocket.send(user['header']+user['data']+message['header']+message['data'])