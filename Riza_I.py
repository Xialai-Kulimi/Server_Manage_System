import discord
import yaml
import NLT

print(NLT.test())

with open('env.secret', 'r') as stream:
    secret_data = yaml.load(stream)

client = discord.Client()

print(secret_data)


@client.event
async def on_ready():
    global main_channel
    # main_channel = 0
    print(f'{client.user} on ready.')
    for guild in client.guilds:
        for channel in guild.channels:
            if channel.id == secret_data['channels']['main']:
                main_channel = channel
    await main_channel.send('Riza_I online.')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    try:
        print(f'[{message.guild.name}][{message.channel.name}][{message.author.name}]: {message.content}')
    except:
        print(f'[{message.author.name}(tell)]: {message.content}')

    print(NLT.recv_convers(message))

    await main_channel.send(NLT.recv_convers(message))


client.run(secret_data['token']['Riza_I'])
