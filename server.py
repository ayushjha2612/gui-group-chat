import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

# Address defined as tuple of server, port
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

# Defining the socket and binding to address to intialise server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDRESS)

#Empty list to store active connections
connections= []

def start_server():

    print(f"Server has started on {SERVER}")

    # Server listening on connections
    server_socket.listen()
    
    while True:
        connection, address = server_socket.accept()
        connection.send("$name".encode(FORMAT))

        client_name= connection.recv(1024).decode(FORMAT)
        connections.append(connection)

        print(f"\n{client_name} has connected to the server")
        print(f"Active Connections: {len(connections)}")
        messageAll(f"{client_name} has joined the chat\nMembers online : {len(connections)}".encode(FORMAT))
        
        # Starting a thread to handle each individual Client
        thread = threading.Thread(target=handle_client, args=(connection, address, client_name))
        thread.start()


def messageAll(message):
    for client in connections:
        client.send(message)

def handle_client(conn, addr, client_name):
    
    while True:
        message= conn.recv(1024).decode(FORMAT)
        if message == '$disconnect' :
            break
        else:
            messageAll(message.encode(FORMAT))

    print(f"\n{client_name} has disconnected from the server")
    print(f"Active Connections: {len(connections)-1}")
    
    messageAll(f"{client_name} has left the chat\nMembers online : {len(connections)-1}".encode(FORMAT))
    connections.remove(conn)
    


start_server()