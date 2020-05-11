import os
import threading


output_filename = 'tcpdump_output'


def exec_tcpdump():
    os.system(f'ping 8.8.8.8 >> {output_filename}')


exec_tcpdump_threading = threading.Thread(target=exec_tcpdump)
exec_tcpdump_threading.start()

while True:
    f = open(output_filename, 'r')
    try:
        line = f.readline().split(' ')
        if line[1] != 'PPPoE':  # Not PPPoE
            continue
        
    except:
        pass