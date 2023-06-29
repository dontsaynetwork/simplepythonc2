import socket #importing the socket librairy to use in the script

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #initialising the socket by using TCP/IP

server = "127.0.0.1" #remote server goes here. 127.0.0.1 is used to test the script on the same computer as the client
port = 4321

client.connect((server,port)) #starting the connection

while True:
    print("REMOTE SHELL OPERATOR")
    print("Enter your commands")
    inp = input("") #Requesting the command to be executed by the remote computer

    client.send(inp.encode()) #sending the command to the remote server and waiting for a response

    response = client.recv(1024) #receiving the response and saving it in the variable response

    print("COMMAND SENT: ", inp)
    print("REPONSE FROM SERVER")
    print(response.decode()) #printing the response from the remote server.

