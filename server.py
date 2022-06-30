import socket
import threading

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())

ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(ADDRESS)

connections= []

def start_server():

    print(f"Server has started on {SERVER}")

    server_socket.listen()

    while True:
        connection, address = server_socket.accept()
        connection.send("$name".encode(FORMAT))

        client_name= connection.recv(1024).decode(FORMAT)
        connections.append(connection)

        print(f"{client_name} has connected to the server")
        messageAll(f"{client_name} has joined the chat".encode(FORMAT))

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

    messageAll(f"{client_name} has the chat".encode(FORMAT))
    print(f"{client_name} has disconnected from the server")
    connections.remove(conn)

    

start_server()