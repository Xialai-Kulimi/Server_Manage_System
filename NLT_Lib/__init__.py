
type_list = ['提問', '表達']

object_list = ['autoPull', 'Riza', 'Kulimi', 'Caleb', 'Server']
object_refer_dict = {'自動更新程式': 'autoPull', '我': 'Riza'}

status_list = ['提問', '表達']


def test():
    return 'NLT working great.'


class NLTCore:
    def __init__(self, name):
        self.name = name
        print(self.name)


def recv(msg):
    author = msg.author
    msg = msg.content.split('，')

    print(msg)

