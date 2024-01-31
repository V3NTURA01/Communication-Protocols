import socket

# Create a new socket using RFCOMM protocol
server_sock = socket.socket(
    socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)

# Bind the socket to any valid port and the local Bluetooth adapter's address
port = 1
server_sock.bind(("", port))

# Listen for connection
server_sock.listen(1)
print("Waiting for connection on RFCOMM channel", port)

# Accept the connection request
client_sock, client_address = server_sock.accept()
print("Accepted connection from", client_address)

try:
    while True:
        data = client_sock.recv(1024)
        if not data:
            break
        print("Received:", data.decode('utf-8'))
        response = input("Reply: ")
        client_sock.send(response.encode('utf-8'))
except KeyboardInterrupt:
    print("Disconnected")

client_sock.close()
server_sock.close()
