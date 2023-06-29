import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server = "127.0.0.1"
port = 4321

client.connect((server,port))

while True:
    print("REMOTE SHELL OPERATOR")
    print("Enter your commands")
    inp = input("...")

    client.send(inp.encode())

    response = client.recv(1024)

    print("COMMAND SENT: ", inp)
    print("REPONSE FROM SERVER")
    print(response.decode())

#client.close()
