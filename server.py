import socket #importing socket to use for the communication between the two computers
import subprocess #importing subprocess to run commmand on the shell and capturing the output

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #initialising the communication protocol

localhost = "127.0.0.1"
port = 4321

server.bind((localhost,port)) #starting the local server
server.listen(1) #waiting for a connection to the local server

print("Waiting for incoming connection")

clientConnection, clientAddress = server.accept() #when a new connection is made, clientConnection and clientAddress stores the variables
print("Connected client: ",clientAddress)

while True:
    receivedinstructions = clientConnection.recv(1024) #grab the message sent by the client
    instructions = receivedinstructions.decode() #decode the message and store in instructions

    localOutput = subprocess.run([instructions], shell=True, capture_output=True, text=True) #run the instructions in the shell of the remote computer
    print("RECEIVED INSTRUCTIONS")
    print(instructions)
    print("")
    print("OUTPUT")
    print(localOutput.stdout) 
   
    clientConnection.send(localOutput.stdout.encode()) #send back the output of the instructions.

    print("RESPOND SENT SUCCESFULLY")


