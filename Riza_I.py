import asyncio
import imp
import discord
import yaml

import NLT

print(NLT.test())

with open('env.secret', 'r') as stream:
    secret_data = yaml.load(stream, Loader=yaml.FullLoader)

client = discord.Client()

loop = asyncio.get_event_loop()


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
                await main_channel.send(f'{now_task[0]}，{now_task[1]}，{now_task[2]}')
                memory_data['task'].remove(now_task)  # task compete, remove it

            with open('memory_lib.yaml', 'w', encoding='utf8') as stream:  # Save memory
                yaml.dump(memory_data, stream, default_flow_style=False, encoding='utf-8', allow_unicode=True)


def do_loop():
    # time.sleep(5)

    print('do tasks')
    loop.run_until_complete(bot_run())


@client.event
async def on_ready():
    global main_channel
    print(f'{client.user} on ready.')
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.id == secret_data['channels']['main']:
                main_channel = channel
    await main_channel.send('Riza_I online.')
    # thread_do_loop = threading.Thread(target=do_loop)
    # thread_do_loop.start()


@client.event
async def on_message(message):
    imp.reload(NLT)
    print(message)
    if message.author == client.user:
        return
    try:
        print(f'[{message.guild.name}][{message.channel.name}][{message.author.name}]: {message.content}')
    except:
        print(f'[{message.author.name}(tell)]: {message.content}')

    NLT.recv_convers(message)


client.loop.create_task(bot_run())
client.run(secret_data['token']['Riza_I'])
