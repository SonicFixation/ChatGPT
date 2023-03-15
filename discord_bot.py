import discord
import os
from payload_creation import (
    create_message_history_list,
    get_scenario
)
from openai_chat_gpt import send_message_to_chattie

discord_bot_token = os.environ.get('CHATTIE_DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
message_history = create_message_history_list('Pretend your name is chattie')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged on as {client.user}!')


# -- listen for messages
@client.event
async def on_message(message):
    global message_history
    # -- ignore messages from self
    if message.author == client.user:
        return

    # -- change scenario if --tag in config.SCENARIOS
    if get_scenario(message.content):
        message_history = create_message_history_list(message.content)
        response, message_history = send_message_to_chattie("Hello", message_history)

    else:
        response, message_history = send_message_to_chattie(message.content, message_history)

    await message.channel.send(response)

# -- Run the bot
client.run(discord_bot_token)
