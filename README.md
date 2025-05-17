# Multi-User Chat Application (Tkinter GUI)

This is a Multi-User Chat Application built with Python, utilizing Tkinter for the graphical user interface (GUI) and socket for network communication. The application allows multiple clients to connect to a server and exchange messages in real-time.

## Features

- **Multi-User Chat**: Allows multiple users to connect and chat simultaneously.
- **Real-Time Messaging**: Messages are sent and received instantly between users.
- **GUI Interface**: Easy-to-use graphical interface built with Tkinter.
- **Username Identification**: Each user is identified by a unique username.
- **Scroll Support**: Chat window supports scrolling for long conversations.

## Requirements

- Python 3.x
- Tkinter (comes pre-installed with Python standard library)

## Installation

Clone the repository or download the script files:

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```



## Usage  

### Start the Server

To start the server, run the following command in the terminal:  

```
bash
python3 server.py
```
> [!IMPORTANT]  
Make sure the server is running before starting the client application.  

You should see:
```bash 
[+] Server is listening...
```

### Start the Client
To connect a client to the server, run:

```bash
./client.py
```
When prompted, enter your username:


```bash
[+] Insert your username: JohnDoe
```

> [!NOTE]  
A chat window will appear, allowing you to send and receive messages in real time.


## Chat Features
-   **Send Messages:** Type your message in the input box and press **Enter** to send.
    
-   **Receive Messages:** Messages from other users are displayed in the chat window.
    
-   **Scroll Support:** The chat window supports scrolling for lengthy conversations.

>[!WARNING]  
If you close the server while clients are still connected, it will cause connection errors.  
Make sure to properly disconnect clients before shutting down the server.

## Script Overview

### Server Script (`server.py`)

-   Manages client connections and message broadcasting.
    
-   Listens for incoming connections on `localhost:1234`.
    
-   Uses threads to handle multiple clients simultaneously.
    

> **Functions:**
> 
> -   `client_thread`: Manages communication with individual clients.
>     
> -   `server_program`: Initializes the server and listens for client connections.
>     

----------

### Client Script (`client.py`)

-   Connects to the server and launches a Tkinter-based chat window.
    
-   Handles real-time message sending and receiving.
    

> **Functions:**
> 
> -   `send_message`: Sends messages to the server and displays them locally.
>     
> -   `receive_message`: Listens for incoming messages from other users.
>     
> -   `client_program`: Initializes the client connection and GUI interface.
>     

----------

## Author

Developed by **Marco Becerra**  


