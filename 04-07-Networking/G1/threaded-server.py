import socket
import threading

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(("localhost",9000))
s.listen()

def handle_client(client_socket):
    try:
        while True:
            message_from_client = client_socket.recv(1024)
            if message_from_client.decode() != "":
                print("Client said:", message_from_client.decode())
            client_socket.sendall((f"Echo {message_from_client}".encode("utf-8")))
    except BrokenPipeError:
        print("Client connection stopped")
    except ConnectionResetError:
        print("Client connection stopped")
    finally:
        client_socket.close()

threads = []

while True:  # while True is bad practice, discover input or so...
    client_socket, address = s.accept()

    t = threading.Thread(target=handle_client, args=(client_socket,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()
s.close()