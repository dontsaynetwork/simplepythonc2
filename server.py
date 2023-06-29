import socket
import subprocess

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

localhost = "127.0.0.1"
port = 4321

server.bind((localhost,port))
server.listen(1)

print("Waiting for incoming connection")

clientConnection, clientAddress = server.accept()
print("Connected client: ",clientAddress)

while True:
    receivedinstructions = clientConnection.recv(1024)
    instructions = receivedinstructions.decode()

    localOutput = subprocess.run([instructions], shell=True, capture_output=True, text=True)
    print("RECEIVED INSTRUCTIONS")
    print(instructions)
    print("")
    print("OUTPUT")
    print(localOutput.stdout)
   
    clientConnection.send(localOutput.stdout.encode())

    print("RESPOND SENT SUCCESFULLY")


