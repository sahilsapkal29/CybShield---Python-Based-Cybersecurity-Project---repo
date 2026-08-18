import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 6000))
server.listen(5)

print("Bank Server Running...")

while True:
   client_socket, addr = server.accept()
   print(f"Connection from {addr}")

   data = client_socket.recv(1024).decode()
   username, password = data.split(",")

   if username == "admin" and password == "1234":
       client_socket.send("Login Successful".encode())
   else:
       client_socket.send("Login Failed".encode())

   client_socket.close()