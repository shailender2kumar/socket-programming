import random
import socket
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.bind(("localhost", random.randint(8000, 9000)))

name = input("Nickname: ")

def recieve():
    while True:
        try:
            message, _ = client.recvfrom(1024)
            print(message.decode())
        except:
            pass

t = threading.Thread(target=recieve)
t.start()

client.sendto(f"SIGNUP_TAG:{name}".encode(), ("localhost", 8081))

while True:
    message = input("")
    if message == "bye":
        exit()
    else:
        client.sendto(f"{name}: {message}".encode(), ("localhost", 8081))