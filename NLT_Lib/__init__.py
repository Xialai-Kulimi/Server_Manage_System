
type_list = ['提問', '表達']

object_list = ['autoPull', 'Riza', 'Kulimi', 'Caleb', 'Server']
obhect_refer_dict = {'自動更新程式': 'autoPull', '我': 'Riza', 'Riza_I': 'Riza'}

status_list = ['提問', '表達']
status_refer_dict = {}

def test():
    return 'NLT working great.'


class NLTCore:
    def __init__(self, name):
        self.name = name
        print(self.name)


def recv(msg):
    global type_list

    author = msg.author
    msg = msg.content.split('，')

    if len(msg) != 3:
        return 'Bad format'

    print(msg)

    for type in type_list:

