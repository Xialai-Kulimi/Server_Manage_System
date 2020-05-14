import time
import os

log_location = '/usr/local/Cellar/nginx/1.17.10/logs/access.log'


while True:
    with open(log_location, 'r') as f:
        log = f.read()

    if log != '':

        os.system(f'cat "{log_location}" >> {log_location}.backup')

        with open(log_location, 'w') as f:
            pass

        user_record = {}
        whole_connect_count = 0

        for line in log.split('\n'):
            line = line.split(' ')
            whole_connect_count += 1
            try:
                user_record[line[0]] += 1
            except:
                user_record[line[0]] = 1
        print(time.asctime(time.localtime(time.time())), user_record)

        os.system('echo "- - 表達" >> ~/Documents/GitHub/Server_Manage_System/memory_lib.yaml')
        os.system('echo "  - 連線紀錄" >> ~/Documents/GitHub/Server_Manage_System/memory_lib.yaml')
        os.system(f'echo "  - {whole_connect_count}個連線，{str(user_record).replace("{", "").replace("}", "").replace(",", ";").replace(" ", "")}" >> ~/Documents/GitHub/Server_Manage_System/memory_lib.yaml')
        os.system('echo "  - 710152892215984130" >> ~/Documents/GitHub/Server_Manage_System/memory_lib.yaml')

    time.sleep(600)

