#!/usr/bin/env python3

import socket
import threading 
import ssl

def client_thread(client_socket, clients, usernames):

    print(f"\n[+] In client thread")
    username = client_socket.recv(1024).decode()
    usernames[client_socket] = username


    print(f"\n{client_socket} : {username}")

    for client in clients:
        if client is not client_socket:
            client.sendall(f"\n[+] User {username} has joined chat\n\n".encode())

    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break

            if message == "!users":
                client_socket.sendall(f"\n[+] Users available: {','.join(usernames.values())}\n\n".encode())
                continue

            for client in clients:
                if client is not client_socket:
                    client.sendall(f"{message}\n".encode())
        except:
            break
    client_socket.close()
    clients.remove(client_socket)
    del usernames[client_socket]

def server_program():

    host = 'localhost'
    port = 1234

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # Time wait 
    server_socket.bind((host, port))
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER) 
    context.load_cert_chain(certfile="server-cert.pem", keyfile="server-key.key") 
    server_socket = context.wrap_socket(server_socket, server_side=True) 
    server_socket.listen()

    print(f"[+] Server is listening...")

    clients = []
    usernames = {}

    while True:

        client_socket, address = server_socket.accept()
        clients.append(client_socket)

        print(f"[+] New user connected: {address}")

        thread = threading.Thread(target=client_thread, args=(client_socket, clients, usernames))
        thread.daemon = True
        thread.start()

    server_socket.close()

if __name__ == '__main__':
    server_program()
