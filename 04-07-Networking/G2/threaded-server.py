import socket
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",9000))
s.listen()

clientlist = []

def handle_client(client_socket, address):
    print("New client connected")
    try:
        while True:
            message_from_client = client_socket.recv(1024).decode("utf-8")
            # client_socket.sendall((f"Echo: {message_from_client}".encode("utf-8")))
            for c in clientlist:
                c.sendall(message_from_client.encode("utf-8"))
    except BrokenPipeError:
        print("Client stopped connection")
    except ConnectionResetError:
        print("Client stopped connection")
    finally:
        client_socket.close()

try:
    while True:
        client_socket, address = s.accept()
        clientlist.append(client_socket)

        t = threading.Thread(target=handle_client, args=(client_socket, address))
        # handle_client(client_socket, address)
        t.start()
finally:
    s.close()

