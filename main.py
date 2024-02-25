import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='~', intents = discord.Intents.all())

@client.event
async def on_ready():
    print('I am {0.user}'.format(client) )
    print("-----------------------------")
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content.startswith('~hello'):
            await message.channel.send('Wassupppp')
            
    client.run(os.getenv('TOKEN'))
        
    