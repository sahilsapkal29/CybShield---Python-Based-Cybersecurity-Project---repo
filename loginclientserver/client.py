import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("127.0.0.1", 6000))

username = input("Enter username: ")
password = input("Enter password: ")

credentials = f"{username},{password}"
client.send(credentials.encode())

response = client.recv(1024).decode()
print("Server Response:", response)

client.close()