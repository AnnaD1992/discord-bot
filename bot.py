# bot.py
import os
import requests
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_ID = int(os.getenv('CHANNEL_ID'))
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents = intents)




@client.event
async def on_ready():
    # for guild in client.guilds:
    #     if guild.name == GUILD:
    #         break
    # print(
    #     f'{client.user} is connected to the following guild:\n'
    #     f'{guild.name}(id: {guild.id})'
    # )

    # members = '\n - '.join([member.name for member in guild.members])
    # print(f'Guild Members:\n - {members}')

    print(f'{client.user.name} has connected to Discord')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(

        f'Hi {member.name}, welcome to the Silent Book Club - Munich chapter'
    )
    await member.send("Hello, Darling!")
  
    channel = client.get_channel(CHANNEL_ID)
    await channel.send(      
          f'Hi {member.name}, welcome to the Silent Book Club - Munich chapter'
    )

@client.event
async def on_member_remove(member):

    channel = client.get_channel(CHANNEL_ID)

    await channel.send(

                  f'Hi {member.name}, see you later, Aligator'

    )



@client.event
async def on_message(message):
    print("Checked")
    if message.author == client.user:
        print(message.author)
        return 
    
    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]
    print(message.content)

    if message.content == "99!":
        response = random.choice(brooklyn_99_quotes)
        await message.channel.send(response)

    if message.content == "Hello ":
        response = "Hello, it is me"
        await message.channel.send(response)


client.run(TOKEN)