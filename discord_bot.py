import discord
import os
import textwrap
import time
from openai_chat_gpt import send_message_to_chattie
from payload_creation import (
    create_message_history_list,
    get_scenario
)
from utils import message_history_has_been_reset

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

        if message_history_has_been_reset(message_history):
            response = "Message history in memory is cleared"

        else:
            response, message_history = send_message_to_chattie("Hello", message_history)

    else:
        response, message_history = send_message_to_chattie(message.content, message_history)

    if len(response) > 2000:
        # Break long responses into smaller chinks so Discord won't complain
        response_chunks = textwrap.wrap(response, width=2000, break_long_words=False)
        for chunk in response_chunks:
            await message.channel.send(chunk)
            time.sleep(1)

    else:
        await message.channel.send(response)

# -- Run the bot
client.run(discord_bot_token)
