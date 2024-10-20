import socket


def main():
    myTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    myTCPSocket.bind(('192.168.1.151', 1234))
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
