import socket


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 5000


client.connect((host, port))

print("===================================")
print("Connected to Server")
print("Server IP        :", host)
print("Port Number      :", port)
print("Connection Status: Connected")
print("===================================\n")


for i in range(3):
    message = input("You: ")
    client.send(message.encode())

    reply = client.recv(1024).decode()
    print("Server:", reply)

print("\nConnection Closed.")
client.close()