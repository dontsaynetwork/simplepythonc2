# simplepythonc2
This is a simple python script to send command information to a remote server.

This script uses two libraries in Python to create a simple C2 server. You can use it to send shell command to a remote computer.

The two scripts that were used in the script are:
1. socket; to initiate and hold the communication between the two computers
2. subprocess; to run the commands on the server and output the response

The response is then sent back to the user after it is process on the server. This projectis only for educational purpose to demonstrate the use of socket in python.

NOTE: You can send the command that would generate a standard output such as "ls" or "pwd" to the server. However, ff you send "mkdir test" on the client side, you will see a folder is created on the server side but it will stopped sending new response to the client.
