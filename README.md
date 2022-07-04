
# Python GUI Group Chat Application

This project uses python socket programming, tkinter, multithreading to create an application where multiple clients can chat with each other. For this, each client connect to the central server and send messages to server where server sends the message received to each and every client.

## Description

Here is a brief description of the project along with features and technologies used  
**server.py :** 
*  Using **socket programming** in server.py an address is defined and the server socket is bound to that address
*  Server is started and accepts conections and recives client's name
*  Using **multithreading** a thread to handle each client is started so that simultaneously many clients can send and receive messages via server.  
<img src="Screenshots\server.png" alt="Server" width="600"/>  

**client.py:**
*  On the client side using **Tkinter** for python login page and chatroom window is created.
*  Client initialises its socket and connects to the server using the same port and server.
*  Separate functions and threads for sending and receiving messages.

<img src="Screenshots\login_window.png" alt="Login" width="300"/>  
<img src="Screenshots\chatroom.png" alt="Chatroom" width="400"/>  



## Getting Started

### Dependencies

* This project uses python3 and tkinter. Install both of these on your system.
* To install tkinter use command on linux:
```
sudo apt-get install python-tk
```

### Installing

* Clone this repository by 
```
git clone https://github.com/ayushjha2612/gui-group-chat Chat-application
```

### Executing program

* To run the server open the directory where you have cloned the repository and type on the terminal
```
python server.py
```
* To connect client on to a server change SERVER on line 6 in clinet.py to the server that appears after running server.py and then type on terminal:
```  
python client.py
```
* Enter the name in login window, hit login button and it redirects you to chatroom. 
* In order to add multiple clients repeat above step multiple times.
