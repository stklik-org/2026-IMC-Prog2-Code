import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("localhost", 9000))

try:
    while True:
        message = input("What would you like to say? ")
        s.send(message.encode("utf-8"))
        message_from_server = s.recv(4096)
        print("Server respondend", message_from_server)
finally:
    s.close()
