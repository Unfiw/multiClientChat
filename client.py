#!/usr/bin/env python3 

import socket
import threading
from tkinter import *
from tkinter.scrolledtext import ScrolledText

def send_message( client_socket, username, text_widget, entry_widget):
    print(f"\n[+] Enter key pressed°")
    message = entry_widget.get()
    print(f"\n[+] User {username} message: {message}")
    client_socket.sendall(f"{username} : {message}".encode())

    entry_widget.delete(0, "end")
    text_widget.configure(state='normal')
    text_widget.insert("end", f"{username} : {message}\n")
    text_widget.configure(state='disabled')

def receive_message(client_socket, text_widget):
    while True:
        try:
            message = client_socket.recv(1024).decode()

            if not message:
                break
            
            text_widget.configure(state='normal')
            text_widget.insert("end", f"{message}")
            text_widget.configure(state='disabled')
        except:
            break

def list_users(client_socket):

    client_socket.sendall("!users".encode())

def exit(client_socket, username, window):
    client_socket.sendall(f"\n[+] User {username} has left the chat\n".encode())
    client_socket.close()
    window.quit()
    window.destroy()

def client_program():
    
    host = 'localhost'
    port = 1234

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    username = input(f"[+] Insert your username: ")

    client_socket.sendall(username.encode())

    window = Tk()
    window.title("Chat")

    text_widget = ScrolledText(window, state='disabled')
    text_widget.pack(padx=5, pady=5)
        
    frame_widget = Frame(window)
    frame_widget.pack(padx=5, pady=3, fill=BOTH, expand=1 )

    entry_widget = Entry(frame_widget, font=("Arial", 14))
    entry_widget.bind("<Return>", lambda _: send_message( client_socket, username, text_widget, entry_widget))
    entry_widget.pack(fill=BOTH, expand=1, side=LEFT)

    button_widget = Button(frame_widget, text="Send", command=lambda: send_message(client_socket, username, text_widget, entry_widget))
    button_widget.pack(side=RIGHT, padx=5)

    users_widget = Button(window, text="List users", command=lambda: list_users(client_socket))
    users_widget.pack(padx=5, pady=5)
    
    exit_widget = Button(window, text="Exit", command=lambda: exit(client_socket, username, window))
    exit_widget.pack(padx=5, pady=5)

    thread = threading.Thread(target=receive_message, args=(client_socket, text_widget))
    thread.daemon = True
    thread.start()


    window.mainloop()
    client_socket.close()

if __name__ == '__main__':
    client_program()
