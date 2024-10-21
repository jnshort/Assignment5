"""
This is the Echo Server. It will listen on a specific port (12345 in this case) in order to receive messages from the
client. It will take that message, capitalize it, and then send it back the client using the same socket.
"""
import socket

serverPort = int(input("Enter Server Port Number: "))  # User must input the port number the server will be using
TCPsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Sets up the socket to send/receive data
TCPsocket.bind(('192.168.1.151', serverPort))  # Binds the socket to the port
TCPsocket.listen(5)  # Listen for incoming connections (Queue length of 5 for incoming connection requests)

print("Server is running...")

while True:
    incomingSocket, incomingAddress = TCPsocket.accept()  # Accepts a connection from the client
    print(f"Client {incomingAddress} has connected")  # Displays the address and port number of the client

    while True:
        message = incomingSocket.recv(1024)  # Receives a message from the client (1024 bytes)
        if not message:  # If message is empty, the client has closed the connection
            break

        print(f"Received message from {incomingAddress}: {message.decode()}")

        response = message.decode().upper()  # Capitalizes the message

        incomingSocket.send(bytearray(str(response), encoding='utf-8'))  # Sends the response through the same socket
        print(f"Sent following response to {incomingAddress}: {response}")

    incomingSocket.close()  # Closes the connection to the client whenever the client exits
    print(f"Connection with {incomingAddress} has been closed.")
    exit()


