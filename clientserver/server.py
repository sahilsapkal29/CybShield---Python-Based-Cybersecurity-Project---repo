import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("127.0.0.1", 5000))
server.listen(5)

print("Server is listening...")
while True:
   client_socket, addr = server.accept()
   print(f"Connection from {addr}")
   
   message = client_socket.recv(1024).decode()
   print(f"Employee Message: {message}")
   
   client_socket.send("Message received securely".encode())
   client_socket.close()
   