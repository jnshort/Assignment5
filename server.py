import socket

def validatePort(PortString):
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

def validateIP(IPstring):
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


def main():
    validPort = False
    while not validPort:
        print("Enter Port: ")
        port = input()
        validPort = validatePort(port)
    myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    host = socket.gethostname()
    serverIP = socket.gethostbyname(host)
    print(serverIP)

    myTCPSocket.bind((serverIP, int(port)))
    myTCPSocket.listen(5)

    incomingSocket, incomingAddress = myTCPSocket.accept()
    while True:
        try:
            mesrecv = str(incomingSocket.recv(1024))
            mesrecv = mesrecv.upper()
        except (ConnectionAbortedError):
            break
        try:
            incomingSocket.send(bytearray(mesrecv, encoding='utf-8'))
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            break
    incomingSocket.close()
    myTCPSocket.close()

main()
