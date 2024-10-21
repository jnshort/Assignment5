# Echo Client-Server Instructions
This file explains how to operate the echo client-server program.

### Basic Operation
1. Ensure connection is established between server and client (See Further Instructions)
2. Client will be promted to input a message
3. This message will be send to server
4. Server will process message to be all uppercase and send it back to the client
5. After recieving the replay, the user may choose to send another message or terminate the session
6. The server will only stay open for a single connection, but multiple messages can be sent within that session

### Prerequisites:
- Ensure python is installed on your device and is added to PATH

### To Run Server:  
1. Navigate to directory containing server.py file
2. Run command "python server.py"
    - or "python3 server.py"
3. Program will automatically detect private IP of server
4. Provide port to use when prompted
5. Server should now be running
6. Server will log the IP and messages of connecting device to console
7. Since this server is for demonstration purposes it will terminate after the connection is closed
    - Server can can recieve and send multiple messages to user while connection stays open

### To Run Client:
1. Navigate to directory containing client.py file
2. Run command "python client.py"
    - or "python3 client.py"
3. Provide the server IP when prompted
    - This is the private IP of the server unless client is on a separate network
    - Refer to following section for more information

### Connecting From Outside Server Network:
1. Client must enter the PUBLIC IP of the server
2. Port forwarding must be set up for the chosen port
    - Port used in program must be set
    - Router must forward to server's private IP