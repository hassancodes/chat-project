import socket

client1_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
PORT = 8080
HOST = socket.gethostbyname(socket.gethostname())

client1_sock.connect((HOST,PORT))
print("socket is connect with: " + HOST)

while True:
    message = input("enter the message: ")
    client1_sock.send(message.encode('utf8'))
    print("message send")

    print(client1_sock.recv(1024).decode())