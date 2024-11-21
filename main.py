from typing import Final
import os
from dotenv import load_dotenv
from discord import Intents, Client, Message, app_commands, Object
import discord
from responses import get_response

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print('Empty message')
        return

    try:
        response: str = get_response(user_message)
        await message.channel.send(response)
    except Exception as e:
        print(e)

@client.event
async def on_ready() -> None:
    print(f'{client.user} is now running!')

@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
        
    if message.content.startswith(f'<@{client.user.id}>'):
        user_message = message.content.replace(f'<@{client.user.id}>', '').strip()
        
        print(f'Responding to mention from {message.author}: {user_message}')
        
        await send_message(message, user_message)

def main() -> None:
    client.run(token=TOKEN)

if __name__ == '__main__':
    main()