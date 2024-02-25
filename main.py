import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        if message.content.startswith('~hello'):
            await message.channel.send('Wassupppp')
            
    client.run(MTIxMTQzNTc4NTI3NTA1NjEyOA.Getgnn.BugDWp6IkeVz93oWqColG5rmgZKTc45vrfxwVM)
        
    