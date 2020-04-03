import os
import time
import socket
import hashlib


def sha256(input_str):
    sha_signature = hashlib.sha256(input_str.encode()).hexdigest()
    return sha_signature


login_log = open('login_log', 'a')

s = socket.socket()
s.bind(('220.135.245.148', 58787))
s.listen(1024)
while True:
    try:
        conn, addr = s.accept()
        login_log.write(f'\n{time.asctime(time.localtime(time.time()))}\n{conn}\n{addr}')
        recv_str = str(conn.recv(1024), 'utf8')
        print(recv_str)
        conn.send(b'Identity confirm.')
        print('Identity confirm.')

        conn.send(b'adsfasdfasdfasdfadsfdffffffffff')
    except Exception as e:
        print(e)
