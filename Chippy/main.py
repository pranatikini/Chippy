import os
import discord
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
#from discord.ext import commands
#import youtube_dl
#import urllib.parse, urllib.request, re


client = discord.Client()

#client = commands.Bot(command_prefix="/")


greetings = ["hello chippy", "hi chippy", "yo chippy","hey chippy"]

g_res = ["Hello!", "Hi!", "Hiii", "Beep Bop Beep Bop", "Yo!"]

sad_words = [
    "sad", "depressed", "upset", "unhappy", "angry", "mad", "miserable",
    "depressing", "unworthy", "regret", "heartbroken", "discouraged", "fail",
    "pathetic", "pain", "lonely"
]

starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person.",
    "Things will get better!",
    "This is temporary.",
    "I'm proud of you ❤",
    "Your emotions are valid. Hold on.",
]

happy_words = ["happy", "yay", "amazing", "great", "danc", "cool","eureka"]

hype_man = ["Yayyyy!", "🥳🥳🥳"]

identifiers = ["kini", "pranati", "prani", "pantu", "@pranatikini"]

id_res = [
    "She's probably asleep XD", "Patience...",
    "She'll be here in a moment if she isn't here already.",
    "She's probably eating", "She hasn't seen your messages yet.", "Wait :P"
]

if "responding" not in db.keys():
    db["responding"] = True

if "absence" not in db.keys():
    db["absence"] = True


def get_quote():
    response = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " -" + json_data[0]['a']
    return (quote)


def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]


def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    msg = message.content

    if msg.startswith('$hello'):
        await message.channel.send('Hello!')

    if msg.startswith('$goodnight'):
        await message.channel.send('Goodnight zZ')

    if msg.startswith('$ily'):
        await message.channel.send('I love you more ❤')

    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send(quote)

    if any(word in msg.lower() for word in greetings):
        await message.channel.send(random.choice(g_res))

    if any(word in msg.lower() for word in happy_words):
        await message.channel.send(random.choice(hype_man))

    if db["responding"]:

        options = starter_encouragements
        if "encouragements" in db.keys():
            options += db["encouragements"]

        if any(word in msg.lower() for word in sad_words):
            await message.channel.send(random.choice(options))

    if db["absence"]:
        if any(word in msg.lower() for word in identifiers):
            await message.channel.send(random.choice(id_res))

    if msg.startswith("$new"):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("New encouraging message added.")

    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1])
            delete_encouragement = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)

    if msg.startswith("$encourage"):
        value = msg.split("$encourage ", 1)[1]
        if value.lower() == "on" or value.lower() == "yes":
            db["responding"] = True
            await message.channel.send("Encourage: enabled.")
        else:
            db["responding"] = False
            await message.channel.send("Encourage: disabled.")

    if msg.startswith("$ima"):
        value = msg.split("$ima ", 1)[1]
        if value.lower() == "on":
            db["absence"] = True
            await message.channel.send("IMA: enabled.")
        else:
            db["absence"] = False
            await message.channel.send("IMA: disabled.")



keep_alive()
client.run(os.environ['TOKEN'])
