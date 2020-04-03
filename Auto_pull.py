from github import Github
import time
import os

try:
    g = Github("")

    # Then play with your Github objects:
    print('Start pull the repos.')
    for repo in g.get_user().get_repos():
        try:
            print()
            print(repo.name, end='')
            if repo.name == 'kulimi.cnmc.tw':
                print('  -[Find Target]')
                print('[cd /Library/WebServer/kulimi.cnmc.tw && git pull]')
                os.system('cd /Library/WebServer/kulimi.cnmc.tw && git pull')

            elif repo.name == 'TRPG-Character-Sheet':
                print('  -[Find Target]')
                print('[cd /Library/WebServer/TRPG-Character-Sheet && git pull]')
                os.system('cd /Library/WebServer/TRPG-Character-Sheet && git pull')

            elif repo.name == 'Server_Manage_System':
                print('  -[Find Target]')
                print('[cd /Library/WebServer/Server_Manage_System && git fetch]')
                if str(os.system('cd /Library/WebServer/Server_Manage_System && git fetch')) != '':
                    os.system('cd /Library/WebServer/Server_Manage_System && git pull')
            else:
                print('  -[Skip]')
            print('\n----------------------------------------------')
        except Exception as e:
            print(e)
except Exception as e:
    print(e)

print('\n======================END=====================\n')

time.sleep(60)

os.system('cd /Library/WebServer/Server_Manage_System && python3 Auto_pull.py >> log.txt')
