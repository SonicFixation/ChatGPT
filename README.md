# ChatGPT
This is a simple discord bot to interface with ChatGPT.

## Getting started

This is more of an intuitive overview than a precise step by step guide but it's easy to figure out.

Create a bot in [Discord Developer Portal](https://discord.com/developers/applications) by clicking `New application`.
Go to OAuth2 then URL Generator, select `bot`, give it permissions to `send messages`, then copy the generated URL and past it into a browser. From there, you can add the bot to your discord server.

If you don't have a Discord server, you can create one by clicking the `+` on the discord app.

Once you've created the bot in the Discord Developer Portal, you can generate a token via the `bot` tab. You will need to add this token as a local environment variable under the key CHATTIE_DISCORD_TOKEN

You will also need an OpenAI API key, which you can get by creating an openai account, logging into [OpenAI](https://platform.openai.com/) and clicking on your account drop down menu (top right). Select 'View API Keys' and then 'create new secret key'.
Save this key as a local environment variable under the key CHATTIE_OPEN_AI_KEY.

