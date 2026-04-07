import socket
# Connecting to a local server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect(("localhost", 9000))
    while True:
        message = input("What would you like to say? ")
        s.send(message.encode("utf-8"))
        message_from_server = s.recv(4096).decode("utf-8")
        print(message_from_server)
finally:
    s.close()
