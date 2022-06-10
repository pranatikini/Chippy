from neuralintents import GenericAssistant
import discord
import os
from keep_alive import keep_alive

chatbot = GenericAssistant('intents.json')
chatbot.train_model()
chatbot.save_model()
client = discord.Client()
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("|"):
    response = chatbot.request(message.content[7:])
    await message.channel.send(response)
keep_alive()
client.run(os.environ['token'])