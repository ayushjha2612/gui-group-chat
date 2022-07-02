import socket
import threading
from tkinter import *

PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDRESS = (SERVER, PORT)
FORMAT = "utf-8"


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(ADDRESS)


def start_client():

	global window
	window=Tk()
	window.title("CHATROOM")
	window.geometry("600x800")
	window.withdraw()

	login_window= Toplevel()
	login_window.title("Login Window")
	login_window.geometry("550x400")
	login_window.configure(bg='light slate blue')

	msg= Label(login_window, text= "Enter your Name : ",font=("Times", "14", "bold"),bg='light slate blue')
	msg.place(relwidth=0.4, relheight=0.1, relx=0.075, rely=0.25)

	entry = Entry(login_window, font=("Times", "14"))
	entry.place(relwidth=0.45, relheight=0.09, relx=0.475, rely=0.25)
	entry.focus()

	login_button= Button(login_window, text="Login", font=("Times", "14", "bold"), bg='PaleTurquoise3',
						command=lambda: start_chat(entry.get(),login_window))

	login_button.place(relwidth=0.4, relheight=0.12, relx=0.3, rely=0.5)
	window.mainloop()
	message = '$disconnect'
	client_socket.send(message.encode(FORMAT))
	client_socket.close()



def start_chat(name, login_window):

	login_window.destroy()
	window.deiconify()
	window.config(bg= 'light cyan')

	text_box = Text(window, font=("Times", "14"), bg='PaleTurquoise1')
	text_box.place(relheight=0.85,relwidth=1, rely=0.065)

	rcv = threading.Thread(target=receive_messages, args=(name, text_box))
	rcv.start()

	your_name = Label(window, text="You : " +name, font= ("Times", "15", "bold"))
	your_name.place(relwidth=1, relheight=0.05, rely=0)

	line = Label(window,bg='dim gray')
	line.place(relwidth=1, rely=0.055, relheight=0.01)

	enter_message = Entry(window, font=("Times", "15"))
	enter_message.place(relwidth=0.73,relheight=0.055, rely=0.935, relx=0.011)
	enter_message.focus()

	send = Button( window, text="Send", font= ("Times", "16", "bold"),
	              command=lambda: send_messages(name,enter_message), bg='pale green')
	send.place(relwidth=0.21, relheight=0.0625, relx=0.77, rely=0.93)

	scrollbar = Scrollbar(text_box)
	scrollbar.place(relheight=1,	relx=0.974)

	scrollbar.config(command=text_box.yview)
	text_box.config(state=DISABLED)



def receive_messages(name, text_box):
	while True:
			try:
				message = client_socket.recv(1024).decode(FORMAT)

				if message == '$name':
					client_socket.send(name.encode(FORMAT))
				else:

					text_box.config(state=NORMAL)
					text_box.insert(END, message+"\n\n")

					text_box.config(state=DISABLED)
					text_box.see(END)
			except:

				client_socket.close()
				break
 
def send_messages(name,enter_button):

	msg= enter_button.get()
	enter_button.delete(0, END)

	message = (f"{name}: {msg}")
	client_socket.send(message.encode(FORMAT))

start_client()

