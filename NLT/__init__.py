import yaml
import asyncio
import os


now_mode = 'Normal'


def test():
    return 'NLT working great.'


class ImagineObject:
    def __int__(self, type, name):
        pass


def generate_command(msg, client):
    pass


async def bot_run(client):
    await asyncio.sleep(0.5)
    with open('memory_lib.yaml', 'br') as stream:  # Load memory
        memory_data = yaml.load(stream, Loader=yaml.FullLoader)

    if len(memory_data['task']) > 1:
        # Do task below
        now_task = memory_data['task'][1]  # [0] is null
        print(memory_data['task'])
        if now_task[0] == '表達':
            send_channel = client.get_channel(now_task[3])

            await send_channel.send(f'{now_task[0]}，{now_task[1]}，{now_task[2]}')
            memory_data['task'].remove(now_task)  # task compete, remove it
        elif now_task[0] == '檢查':

            memory_data['task'].append(['表達', now_task[1], '是', now_task[3]])

        with open('memory_lib.yaml', 'w', encoding='utf8') as stream:  # Save memory
            yaml.dump(memory_data, stream, default_flow_style=False, encoding='utf-8', allow_unicode=True)


def generated_command(msg, client):
    pass


class NLTCore:
    def __init__(self, name):
        self.name = name
        print(self.name)


def recv_convers(msg, client):
    global now_mode
    #
    # 1. 解析訊息
    #

    with open('NL.yaml', 'br') as stream:
        nl_data = yaml.load(stream, Loader=yaml.FullLoader)

    if now_mode == 'Command':
        if msg.content == 'exit':
            now_mode = 'Normal'
            await msg.channel.send('[Command mode terminated.]')

        msg.content = msg.content.split(' ')

        if msg.content[0] == 'update':
            if msg.content[1] == 'Riza_I':
                try:
                    os.system("git pull")
                except Exception as e:
                    await msg.channel.send(f'[Error] Error occurred, debug information:\n{e}')

        return

    orin_msg = msg

    msg_channel_id = msg.channel.id
    msg_channel = msg.channel
    author = msg.author.name

    msg = msg.content

    if msg == nl_data['command_keyword']['enter']:
        now_mode = 'Command'
        await msg_channel.send('[Successfully enter command mode.]')
        return

    if msg.split('，')[0] == '指令':
        generate_command(msg, client)

    for i in nl_data['none_mean_list']:
        msg = msg.replace(i, '')

    for i in nl_data['question_word']:
        msg = msg.replace(i, '')

    msg = msg.split('，')

    # if len(msg) != 3:
    #     return 1, 'Bad format'

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
        memory_data['task'].append(['表達', author, '是', msg_channel_id])
        try:
            if memory_data['memory'][msg_object] != msg_status:
                memory_data['task'][-1][2] = '不清楚'
        except:
            memory_data['task'][-1][2] = '不清楚'
            memory_data['task'].append(['檢查', msg_object, author, msg_channel_id])

    with open('memory_lib.yaml', 'w', encoding='utf8') as stream:
        yaml.dump(memory_data, stream, default_flow_style=False, encoding='utf-8', allow_unicode=True)

    return 0
