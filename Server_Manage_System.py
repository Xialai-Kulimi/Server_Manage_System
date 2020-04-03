import os
import socket
import getpass
import hashlib
import time


def sha256(input_str):
    sha_signature = hashlib.sha256(input_str.encode()).hexdigest()
    return sha_signature


def print_info(info):
    print('#' + ' ' * 59 + '#')
    print('# ' + f'[{info[0]}]' + '#')


f = open('config', 'ba')
f.close()

f = open('config', 'br')
config = f.read().split(b'\n')
f.close()

if len(config) == 1:
    print('Please input your user name and password for kulimi.cnmc.tw.')
    username = input('Please input your your username. username: ')
    # pwd = input('Please input your password. password: ')
    pwd = getpass.getpass("Please input your password. password: ")
    # print("your password is " + input)

    b_save_info = input('Save your information? (y/n)')

    if str.lower(b_save_info) == 'y':
        f = open('config', 'ba')
        f.write(bytes(f'{username}\n', 'utf8'))
        timer = 0
        for i in list(pwd):
            x = chr((ord(i) - ord(sha256(username)[timer])) % 256)
            # print(x)
            f.write(bytes(x, 'utf8'))
            timer += 1

else:
    username = str(config[0], 'utf8')
    pwd = ''
    # print(config)
    # print(str(config[1], 'utf8'))
    for i in range(len(str(config[1], 'utf8'))):
        pwd = pwd + chr((ord(str(config[1], 'utf8')[len(pwd)]) + ord(str(sha256(username)[len(pwd)]))) % 256)

print('Connect to the Server.', end='')
s = socket.socket()
print('.', end='')
s.connect(('220.135.245.148', 58787))
print('.', end='')

now_time = str(time.time())
for i in range(5):
    s.send(bytes(f'{username}\n{now_time}\n{sha256(f"{username}{now_time}")}', 'utf8'))
    if s.recv(1024) == b'Identity confirm.':
        s.close()
        break
else:
    print('Connection error.')
    os.system('pause')
    exit()
print('Done\nIdentity confirm.')

while True:
    s = socket.socket()
    s.connect(('220.135.245.148', 58787))
    s.send(bytes(f'{username}\n{now_time}\n{sha256(f"{username}{now_time}")}', 'utf8'))
    recv_str = str(s.recv(4096), 'utf8')
    recv_str = str(s.recv(4096), 'utf8')
    print(recv_str, end='\r')
    s.close()
    for i in range(2):
        print('#' + ' ' * 59 + '#')
        time.sleep(0.1)
    print('#' + ' ' * 59 + '#')
