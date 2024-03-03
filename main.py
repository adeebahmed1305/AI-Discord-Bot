from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message
from userresponse import get_response
from userresponse import chat_with_gpt

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents: Intents = Intents.default() 
intents.message_content = True
client: Client = Client(intents = intents)

async def send_message(message: Message, user_message: str):
    if not user_message:
        print("Message is empty because intents weren't enabled")
        return
    
    if is_private := user_message[0] == '~':
        user_message=user_message[1:]
        
    try:
        response: str = get_response(user_message)
        await message.channel.send(response) if is_private else await message.send(response)
    except Exception as e:
        print(e)
        
@client.event
async def on_ready():
    print(f'{client.user} is online!')
    
@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return
    
    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)
    
    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)
    
    command, the_message = None, None
    
    for text in ['/ai', '/mr']:
        if message.content.startswith(text):
            command = message.content.split(' ')[0]
            the_message = message.content.replace(text, '')
            print(command, the_message)
    
    if command == '/ai' or command == '/mr':
        bot_response = chat_with_gpt(prompt = the_message)
        await message.channel.send(f"{bot_response}")
        
def main():
    client.run(token=TOKEN)

if __name__ == '__main__':
    main() 