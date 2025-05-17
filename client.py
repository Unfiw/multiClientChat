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
            text_widget.insert("end", f"{message}\n")
            text_widget.configure(state='disabled')
        except:
            break

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
    text_widget.pack(padx=5, pady=5, fill=BOTH,expand=1)

    entry_widget = Entry(window)
    entry_widget.bind("<Return>", lambda _: send_message( client_socket, username, text_widget, entry_widget))
    entry_widget.pack(padx=5, pady=5, fill=BOTH, expand=1)

    thread = threading.Thread(target=receive_message, args=(client_socket, text_widget))
    thread.daemon = True
    thread.start()


    window.mainloop()
    client_socket.close()

if __name__ == '__main__':
    client_program()
