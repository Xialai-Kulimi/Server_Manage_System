import os

rows, columns = os.popen('stty size', 'r').read().split()
rows = int(rows)
columns = int(columns)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
print('*' * columns + ('*' + ' ' * (columns - 2) + '*\n') * (rows - 2) + '*' * columns, end='')
while True:
    os.system('clear')
    print('*' * columns + ('*' + ' ' * (columns - 2) + '*\n') * (rows - 2) + '*' * columns, end='')
