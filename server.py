import socket
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
PORT = 8080
HOST = socket.gethostbyname(socket.gethostname())
address = (HOST,PORT)

sock.bind(address)
print("Socket is binded")
sock.listen(10)
print("listening for connections....")

connection1, addr1 = sock.accept()

data = connection1.recv(1024)
print(data.decode('utf8'))


# connection1, addr1 = sock.accept()

# connection, addr = sock.accept()
