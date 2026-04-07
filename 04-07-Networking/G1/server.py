import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",9000))
s.listen()

client_socket, address = s.accept()

try:
    while True:
        message_from_client = client_socket.recv(1024)
        print("Client said:", message_from_client.decode())
        client_socket.sendall((f"Echo {message_from_client}".encode("utf-8")))
finally:
    client_socket.close()
    s.close()