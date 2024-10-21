# Short, Justin
# CECS 327
# Due 10/20/24
# Assignment 5 - Socket Programming

import socket

def validateIP(IPstring):
    """Validates user input is within range of valid IP 
    addresses. Also ensure it contains only numeric digits.
    params: str
    Return: bool
    """    
    octet_list = IPstring.split(".")
    if len(octet_list) != 4:
        print("Invalid IP")
        return False
    for octet in octet_list:
        if not octet.isnumeric():
            print("Invalid IP")
            return False
        if int(octet) > 255:
            print("Invalid IP")
            return False
        if int(octet) < 0:
            print("Invalid IP")
            return False
    return True

def validatePort(PortString):
    """Validates user input is within range of valid port
    numbers. Also ensure it contains only numeric digits.
    params: str
    Return: bool
    """
    if not PortString.isnumeric():
        print("Invalid Port")
        return False
    if int(PortString) < 0:
        print("Invalid Port")
        return False
    if int(PortString) > 65535:
        print("Invalid Port")
        return False
    return True

def main():
    # Get server IP and port from user
    validIP = False
    validPort = False

    # Validate IP and port
    while not validIP:
        print("Enter Server IP Address: ")
        serverIP = input()
        validIP = validateIP(serverIP)
    while not validPort:
        print("Enter Port Number: ")
        port = input()
        validPort = validatePort(port)

    # Create a socket and connect to server
    myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    myTCPSocket.connect((serverIP, int(port)))

    # Loop until client is done sending messages
    loop = True
    while loop:
        # User inputs message
        print("Enter Message: ")
        message = input()

        # Send user message to server
        myTCPSocket.send(bytearray(message, encoding='utf-8'))

        # Wait for server response
        serverResponse = myTCPSocket.recv(1024)

        # Decode utf-8 back to string
        resp = serverResponse.decode()

        # Extract only message from response
        resp = resp[2:len(resp)-1]
        print(resp)

        # Give user option to send again or quit
        print("Type 'q' to quit or type nothing to send another message to server: ")
        inp = input()
        if inp.lower() == 'q':
            loop = False
    # End the connection to server
    myTCPSocket.close()


main()
