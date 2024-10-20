import socket

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

def main():
    validIP = False
    validPort = False
    while not validIP:
        print("Enter Server IP Address: ")
        serverIP = input()
        validIP = validateIP(serverIP)
    while not validPort:
        print("Enter Port Number: ")
        port = input()
        validPort = validatePort(port)

    myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    myTCPSocket.connect((serverIP, int(port)))

    loop = True
    while loop:
        print("Enter Message: ")
        message = input()
        myTCPSocket.send(bytearray(message, encoding='utf-8'))

        serverResponse = myTCPSocket.recv(1024)
        resp = serverResponse.decode()
        resp = resp[2:len(resp)-1]
        print(resp)

        print("Type 'q' to quit or type nothing to send another message to server: ")
        inp = input()
        if inp.lower() == 'q':
            loop = False
    myTCPSocket.close()


main()
