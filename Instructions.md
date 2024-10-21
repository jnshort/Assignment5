# Echo Client-Server Instructions
This file explains how to operate the echo client-server program.

### Basic Operation
- After a connection is established between client and server
    - See following "To Run" instructions
- Client will be promted to input a message
- This message will be send to server
- Server will process message to be ALL UPPERCASE
    - And send it back to the client
- After recieving the reply
    - User may choose to send another message
    - Or terminate the session
- The server will only stay open for a single connection
    - But multiple messages can be sent within that session

### Prerequisites:
- Ensure python is installed on your device and is added to PATH

### To Run Server:  
- Navigate to directory containing server.py file
- Run command "python server.py"
    - or "python3 server.py"
- Program will automatically detect private IP of server
- Provide port to use when prompted
- Server should now be running
- Server will log the IP and messages of connecting device to console
- Since this server is for demonstration purposes
    - It will terminate after the connection is closed
    - But can recieve and send multiple messages to user while connection stays open

### To Run Client:
- Navigate to directory containing client.py file
- Run command "python client.py"
    - or "python3 client.py"
- Provide the server IP when prompted
    - If server is on same private network
        - This IP will be logged to the console when server is started
    - If server is on another network
        - This IP will be the public IP the server is on
        - Refer to "Connecting From Outside Server Network"

### Connecting From Outside Server Network:
- Client must enter the PUBLIC IP of the server
- Port forwarding must be set up for the chosen port
    - Port used in program must be set
    - This can be configured in router settings
    - Router forwards any TCP streams using chosen port
        - To the private IP of the server
