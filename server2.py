import socket
#import pyperclip as pc

PORT = 50000
BUFFER_SIZE = 1024
signal_list = [-1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #s.bind(('127.0.0.1', PORT)) # NG
    #s.bind((socket.gethostname(), PORT)) # NG
    s.bind(("172.20.21.246", PORT)) # OK
    s.listen()
    while True:
        (connection, client) = s.accept()
        try:
            print('Client connected', client)
            data = connection.recv(BUFFER_SIZE)
            if data.decode("utf-8") == "get":
                connection.send(str(signal_list[-1]).encode())
            if data.decode("utf-8") == "0":
                signal_list.append(int(data.decode("utf-8")))
            if data.decode("utf-8") == "1":
                signal_list.append(int(data.decode("utf-8")))
            if data.decode("utf-8") == "2":
                signal_list.append(int(data.decode("utf-8")))
            print(signal_list)
            #pc.copy(signal_list)

        finally:
            connection.close()

            