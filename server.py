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
print("connected with ", addr1)
connection2, addr2 = sock.accept()
print("connected with ", addr2)
print(connection1)

while True:

    # data received by client1
    data1 = connection1.recv(1024)

    connection2.send(data1)
    print(data1.decode('utf8'))



    # data received by client2
    data2 = connection2.recv(1024)
    connection1.send(data2)
    print(data2.decode('utf8'))



