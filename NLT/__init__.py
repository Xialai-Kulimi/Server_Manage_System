import yaml


def test():
    return 'NLT working great.'


class NLTCore:
    def __init__(self, name):
        self.name = name
        print(self.name)


def recv_convers(msg):
    #
    # 1. 解析訊息
    #
    with open('NL.yaml', 'br') as stream:
        nl_data = yaml.load(stream)

    author = msg.author
    msg = msg.content.split('，')

    if len(msg) != 3:
        return 1, 'Bad format'

    # print(msg)

    for the_type in nl_data['type_list']:
        if the_type == msg[0]:
            msg_type = the_type
            break
        else:
            return 1, 'Unknown type'

    for refer_object in nl_data['object_refer_dict']:  # Refer object
        print(refer_object, 1)
        msg[1] = msg[1].replace(refer_object, nl_data['object_refer_dict'][refer_object])

    for the_object in nl_data['object_list']:

        print(msg[1])

        if the_object == msg[1]:
            msg_object = the_object
            break
    else:
        return 1, 'Unknown object'

    for refer_status in nl_data['status_refer_dict']:  # Refer status
        msg[2] = msg[2].replace(refer_status, nl_data['status_refer_dict'][refer_status])

    for the_status in nl_data['status_list']:

        if the_status == msg[2]:
            msg_status = the_status
            break
    else:
        return 1, 'Unknown status'
    #
    # 2. 反應
    #
    with open('memory', 'br') as stream:
        memory_data = yaml.load(stream)

    if msg_type == '表達':
        memory_data
