import socket


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"   # Localhost
port = 5000


server.bind((host, port))


server.listen(1)

print("===================================")
print("Server is running...")
print("Listening on Port:", port)
print("Waiting for client connection...")
print("===================================")

conn, addr = server.accept()

print("\nClient Connected Successfully!")
print("Client IP Address :", addr[0])
print("Port Number       :", addr[1])
print("Connection Status : Connected\n")


for i in range(3):
    client_message = conn.recv(1024).decode()
    print("Client:", client_message)

    reply = input("Server Reply: ")
    conn.send(reply.encode())

print("\nChat Ended.")
conn.close()
server.close()