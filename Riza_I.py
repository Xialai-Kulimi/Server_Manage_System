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


client.loop.create_task(NLT.bot_run())
client.run(secret_data['token']['Riza_I'])
