import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 5000))

msg = input("Enter your message: ")
client.send(msg.encode())

response = client.recv(1024).decode()
print("Server Response:", response)

client.close()
