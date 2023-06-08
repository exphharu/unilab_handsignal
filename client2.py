import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.20.21.246", 50000))
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

full_msg = b''
while True:
    msg = s.recv(8)
    if len(msg) <= 0:
        break
    full_msg += msg
    print(full_msg.decode("utf-8"))