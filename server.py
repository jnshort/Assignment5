# Short, Justin
# CECS 327
# Due 10/20/24
# Assignment 5 - Socket Programming

import socket

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

def get_local_ip():
    """Opens a socket to find local IP of the server. 
    This is later used to bind the socket to.
    Params: None
    Return: Address
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect(("8.8.8.8", 80))
        local_ip = s.getsockname()[0]
    return local_ip


def main():
    # Determine what IP to bind server socket to
    local_ip = get_local_ip()
    print(f"Binding to IP: {local_ip}")

    # Get a valid port number from user
    validPort = False
    while not validPort:
        print("Enter Port: ")
        port = input()
        validPort = validatePort(port)

    # Open a socket it to IP and port, begin listening
    myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    myTCPSocket.bind((local_ip, int(port)))
    myTCPSocket.listen(5)

    # Accept connetion
    incomingSocket, incomingAddress = myTCPSocket.accept()

    # Log client IP 
    print(f"Connected to: {incomingAddress}")
    while True:
        try:
            # cast incoming message back to string
            mesrecv = str(incomingSocket.recv(1024))

            # Log client message
            print(f"Recieved message: {mesrecv}")

            # Process client message to uppercase
            mesrecv = mesrecv.upper()

        # break out and close sockets if errors occur
        except (ConnectionAbortedError, KeyboardInterrupt):
            break

        try:
            # Send processed message back to client
            incomingSocket.send(bytearray(mesrecv, encoding='utf-8'))

            # Log processed client message
            print(f"Response send: {mesrecv}")
        # break out and close socket and connection if errors occur
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError, KeyboardInterrupt):
            break
    print("Connection ended")
    incomingSocket.close()
    myTCPSocket.close()

main()
