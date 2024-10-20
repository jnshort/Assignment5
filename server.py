import socket


def main():
    myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    myTCPSocket.bind(('localhost', 1234))
    myTCPSocket.listen(5)

    incomingSocket, incomingAddress = myTCPSocket.accept()
    while True:
        mesrecv = str(incomingSocket.recv(1024))
        mesrecv = mesrecv.upper()
        try:
            incomingSocket.send(bytearray(mesrecv, encoding='utf-8'))
        except (BrokenPipeError, ConnectionResetError):
            break
    incomingSocket.close()
    myTCPSocket.close()

main()
