import asyncio
import imp
import discord
import yaml
import NLT
import threading
import time


print(NLT.test())

with open('env.secret', 'r') as stream:
    secret_data = yaml.load(stream, Loader=yaml.FullLoader)

client = discord.Client()

loop = asyncio.get_event_loop()


async def bot_run():
    while True:
        try:
            imp.reload(NLT)
            await NLT.bot_run(client)
        except Exception as e:
            print(e)


@client.event
async def on_ready():
    print(f'{client.user} on ready.')
    admin_kulimi = client.get_user(secret_data['admin']['kulimi'])
    await admin_kulimi.send('Riza_I online.')
    # thread_do_loop = threading.Thread(target=do_loop)
    # thread_do_loop.start()


@client.event
async def on_message(message):
    try:
        print(message)
        if message.author == client.user:
            return
        try:
            print(f'[{message.guild.name}][{message.channel.name}][{message.author.name}]: {message.content}')
        except:
            print(f'[{message.author.name}(tell)]: {message.content}')

        NLT.recv_convers(message, client)
    except Exception as e:
        print(e)


client.loop.create_task(bot_run())
client.run(secret_data['token']['Riza_I'])
