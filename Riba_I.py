import discord
import yaml

with open('env.secret', 'r') as stream:
    secret_data = yaml.load(stream)

client = discord.Client()

@client.event
async def on_ready


client.run(secret_data['token']['Riza_I'])
