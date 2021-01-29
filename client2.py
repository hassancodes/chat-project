import socket

client2_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
PORT = 8080
HOST = socket.gethostbyname(socket.gethostname())

client2_sock.connect((HOST,PORT))
print("socket is connect with: " + HOST)

print(client2_sock.recv(1024).decode())
message = input("enter the message: ")
client2_sock.send(message.encode('utf8'))
print("message send")

