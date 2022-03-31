import socket
import time
import random

arquivo = open(input('Accounts file: '))
multimsg = input("MultiMSG [S/N]: ").lower().strip()
if multimsg == "s":
    msg1 = input("Message 1: ").strip()
    msg2 = input("Message 2: ").strip()
    msg3 = input("Message 3: ").strip()
if multimsg == "n":
    msg = input("Message: ").strip()
channel = input("Channel: ").lower().strip()

k = arquivo.read().splitlines()
while True:
    for c in k:
        s = socket.socket()
        s.settimeout(0.5)
        s.connect(('irc.chat.twitch.tv', 6667))
        ac = c.split(":")
        password = ac[1].lower()
        username = ac[3].lower()
        s.send(f"PASS oauth:{password}\r\n".encode('utf-8'))
        s.send(f"NICK {username}\r\n".encode('utf-8'))
        s.send(f"JOIN #{channel}\r\n".encode('utf-8'))
        r9k = random.choice(range(4309,2121301))
        if multimsg == "n":
            s.send(f"PRIVMSG #{channel} :{r9k} {msg}\r\n".encode('utf-8'))
            print(f"{username}: {msg} ")
            s.close
        if multimsg == "s":
            RM = [msg1,msg2,msg3]
            x = random.choice(RM)
            s.send(f"PRIVMSG #{channel} :{r9k} {x}\r\n".encode('utf-8'))
            print(f"{username}: {x}")
            s.close
            
