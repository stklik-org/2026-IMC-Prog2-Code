import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",9000))
s.listen()
try:
    client_socket, address = s.accept()
    while True:
        message_from_client = client_socket.recv(1024).decode("utf-8")
        client_socket.sendall((f"Echo: {message_from_client}".encode("utf-8")))
except BrokenPipeError:
    print("Client stopped connection")
except ConnectionResetError:
    print("Client stopped connection")
finally:
    client_socket.close()
    s.close()
