# ChatGPT
This is a simple discord bot to interface with ChatGPT.

## Getting started

This is more of an intuitive overview than a precise step by step guide but it's easy to figure out.

Create a bot in [Discord Developer Portal](https://discord.com/developers/applications) by clicking `New application`.
Go to OAuth2 then URL Generator, select `bot`, give it permissions to `send messages`, then copy the generated URL and past it into a browser. From there, you can add the bot to your discord server.

If you don't have a Discord server, you can create one by clicking the `+` on the Discord app.

Once you've created the bot in the Discord Developer Portal, you can generate a token via the `bot` tab. You will need to add this token as a local environment variable under the key CHATTIE_DISCORD_TOKEN

You will also need an OpenAI API key, which you can get by creating an openai account, logging into [OpenAI](https://platform.openai.com/) and clicking on your account drop down menu (top right). Select 'View API Keys' and then 'create new secret key'.
Save this as a local environment variable under the key CHATTIE_OPEN_AI_KEY.


## Interacting with ChatGPT via your bot

If you follow the instructions above you should be able to get your bot into your server.

Once it's in the server you can start chatting to it via the discord app.

It will reply to every message sent in the channel it is in.

If you send one of the scenario keys (found in `config.py`) eg `--python` as a message in the channel, the bot will respond as the character the scenario pertains to. In this case it will become a Python instructor waiting for questions about programming in Python.

You can change the scenario by typing another one eg `--gp` and you can reset to the basic ChatGPT, but with the name Chattie using `--reset`.

You can create your own scenarios by adding more to the config or to the `private_config.py`.

The `private_config.py` exists just so that I can keep my growing list of silly characters out of the repo.

