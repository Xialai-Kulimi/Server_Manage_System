import yaml
import asyncio


async def bot_run():
    while True:
        # print('98')
        await asyncio.sleep(0.5)
        with open('memory_lib.yaml', 'br') as stream:  # Load memory
            memory_data = yaml.load(stream, Loader=yaml.FullLoader)

        if len(memory_data['task']) > 1:
            # Do task below
            now_task = memory_data['task'][1]  # [0] is null
            print(memory_data['task'])
            if now_task[0] == '表達':
                await now_task[3].send(f'{now_task[0]}，{now_task[1]}，{now_task[2]}')
                memory_data['task'].remove(now_task)  # task compete, remove it

            with open('memory_lib.yaml', 'w', encoding='utf8') as stream:  # Save memory
                yaml.dump(memory_data, stream, default_flow_style=False, encoding='utf-8', allow_unicode=True)


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
        nl_data = yaml.load(stream, Loader=yaml.FullLoader)

    author = msg.author.name
    # print(author)

    # for object_name in nl_data['object_list']:  # Refer author
    #     author = author.replace(object_name, nl_data['object_refer_dict'][object_name])

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
        msg[1] = msg[1].replace(refer_object, nl_data['object_refer_dict'][refer_object])

    for the_object in nl_data['object_list']:
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
    with open('memory_lib.yaml', 'br') as stream:
        memory_data = yaml.load(stream, Loader=yaml.FullLoader)

    if msg_type == '表達':
        memory_data['memory'][msg_object] = msg_status
        memory_data['task'].append(['檢查', msg_object, msg_status, True])

    elif msg_type == '提問':
        memory_data['task'].append(['表達', author, '是'])
        try:
            if memory_data['memory'][msg_object] != msg_status:
                memory_data['task'][-1][2] = '否'
        except:
            memory_data['task'][-1][2] = '不清楚'

    with open('memory_lib.yaml', 'w', encoding='utf8') as stream:
        yaml.dump(memory_data, stream, default_flow_style=False, encoding='utf-8', allow_unicode=True)

    return 0
