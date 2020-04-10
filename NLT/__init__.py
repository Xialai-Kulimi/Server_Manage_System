
type_list = ['提問', '表達']

object_list = ['autoPull', 'Riza', 'Kulimi', 'Caleb', 'Server']
object_refer_dict = {'自動更新程式': 'autoPull', '你': 'Riza', 'Riza_I': 'Riza'}

status_list = ['提問', '表達']
status_refer_dict = {}

def test():
    return 'NLT working great.'


class NLTCore:
    def __init__(self, name):
        self.name = name
        print(self.name)


def recv_convers(msg):
    global type_list

    author = msg.author
    msg = msg.content.split('，')

    if len(msg) != 3:
        return 1, 'Bad format'

    # print(msg)

    for the_type in type_list:
        if the_type == msg[0]:
            msg_type = the_type
            break
        else:
            return 1, 'Unknown type'

    for refer_object in object_refer_dict:  # Refer object
        print(refer_object, 1)
        msg[1] = msg[1].replace(refer_object, object_refer_dict[refer_object])

    for the_object in object_list:

        print(msg[1])

        if the_object == msg[1]:
            msg_object = the_object
            break
    else:
        return 1, 'Unknown object'

    for refer_status in status_refer_dict:  # Refer status
        msg[2] = msg[2].replace(refer_status, status_refer_dict[refer_status])

    for the_status in status_list:

        if the_status == msg[2]:
            msg_status = the_status
            break
    else:
        return 1, 'Unknown status'

    print(msg_type, msg_object, msg_status)

