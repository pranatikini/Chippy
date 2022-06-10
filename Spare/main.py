import os
import discord
import random
from discord.ext import commands

from keep_alive import keep_alive


client = commands.Bot(command_prefix="/")

truths = ["Who was your first crush?","Who is the person in the room who you hate the most?","What was the most boring joke you've ever told?","What was the most embarrassing dream you've ever had?","What is your worst fear?","When was the first time you ever called your teacher \"mom\"?","If you were marooned on an island with just a single person, who would you like it to be?"," If you woke up one day and notice, that you are invisible, then what will be the first thing that you would like to do?","What is the question that you do not want anyone to ask you in this game?"," If you could have anything in the world, what would it be?"," What is the strangest dream you've ever had?"," What do you like the most about everyone in the room?"," Have you ever lied to a teacher and what was it about?"," Do you sneak snacks when your Mom isn't looking?"," What's the dumbest thing you ever said or did, around a boy/girl you liked?"," What is the worst gift you have ever received?","Have you ever lied in truth in truth or dare?","If you had to be Crazy-Glued to any celebrity, who would it be and why? ","What's the strangest obsession you've ever had? ","What's the meanest thing you've ever done? ","What's the weirdest thing you've ever done","Who was the first person you kissed","Who is your crush right  now","What is the most embarrassing thing that happened to you?","What is one talent most people here don’t know you have?","What was the nastiest joke you ever played on someone?","Have you ever lied to a teacher and what was it about?","Do you sneak snacks when your Mom isn't looking?","What's the dumbest thing you ever said or did, around a boy/girl you liked?","What would you do if you won $100,000,000,000,000?"]

dares = ["I dare you to make your funniest monkey face.","Peel a banana with your feet.","Taste a dirty sock.","Eat a spoonful of mustard","Lick the person's sock closest to you.","I dare you to ask your neighbor for a roll of toilet paper.","I dare you to ask someone to do your makeup blindfolded.","I dare you to do 10 dares made up by your friends.","I dare you to lick a players' shoe.","I dare you to prank call a random person with an accent.","I dare you to wet willy the person across from you.","I dare you to say bad comments to everyone you see pass by."," Run around wearing socks on your hands, pants for a shirt and a shirt for pants, for 3 minutes."," Say the pledge of allegiance in your most hated teacher's voice."," Run down the street in your pajamas."," Have the person to the left of you do your makeup ... blindfolded."," After everything you say add \"Whoa ... I'm good!\" for the next 15 minutes."," Ask a neighbor for a roll of toilet paper."," What is one annoying habit of each person in the room?"," Stand in your front yard, wave and say 'Hi!' to everyone you see."," Moonwalk across the room."," Pretend that you are underwater for the next 10 minutes."," Act like a gorilla for one minute","Smell a dirty sock for ten seconds.","Sing your favorite song in a funny voice.","Have the other kids wrap you in toilet paper.","Bite into a lemon slice.","Go outside and pour a cup of ice cold water over your head.","Hold an ice cube in your hand until it melts.","Eat a pudding cup without using your hands.","Go outside and yell \"I believe in fairies\" loudly three times while clapping your hands as fast as you can.","Sing the \"I'm a little tea pot song\". Do all the motions","Eat a mouthful of crackers and then try and whistle.","Act out a favorite scene from a movie.","Spin around with your head on a bat 5 times and then jump rope.","Say the alphabet backwards as fast as you can.","Give every tree in the yard a big hug and tell each one that you love him/her.","For the next hour wear lampshade on your head for a hat.","Let the person standing closest to you do your make-up crazy. Keep it on for at least an hour.","Stick jelly between all your toes and leave it there for 20 minutes.","Go into the front yard and do the chicken dance for one minute –Don't forget to bark. ","I dare you to Put an ice cube in your pants pocket and keep it there until it completely melts.","Give a piggyback ride to or receive a piggyback ride from another player.","Lick the palm and back of hand for the player directly across from you","choose another player and repeat everything they say for the next 3 rounds.","Place some food on a plate on the floor do push-up over the plate and eat a bite every time you go down","Have another player write the name of their first love on your forehead.","Try to lick your elbow.","Go outside and yell “I believe in fairies” loudly three times while clapping your hands as fast as you can.","Sing the “I’m a little tea pot song”. Do all the motions.","Eat a mouthful of crackers and then try and whistle.","Act out a favorite scene from a movie.","Pretend that you are underwater for the next 10 minutes.","Act like a gorilla for one minute. "]

player1 = ""
player2 = ""
player3 = ""
player4 = ""
player5 = ""
player6 = ""
player7 = ""
turn = ""
gameOver = True


@client.command()
async def tod(ctx, p1: discord.Member, p2: discord.Member, p3: discord.Member, p4: discord.Member, p5: discord.Member, p6: discord.Member,p7: discord.Member):
    global player1
    global player2
    global player3
    global player4
    global player5
    global player6
    global player7
    global turn
    global gameOver

    if gameOver:
        gameOver = False

        player1 = p1
        player2 = p2
        player3 = p3
        player4 = p4
        player5 = p5
        player6 = p6
        player7 = p7

        # determine who goes 
        num = random.randint(1,7)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
        elif num == 3:
            turn = player3
            await ctx.send("It is <@" + str(player3.id) + ">'s turn.")
        elif num == 4:
            turn = player4
            await ctx.send("It is <@" + str(player4.id) + ">'s turn.")
        elif num == 5:
            turn = player5
            await ctx.send("It is <@" + str(player5.id) + ">'s turn.")
        elif num == 6:
            turn = player6
            await ctx.send("It is <@" + str(player6.id) + ">'s turn.")
        elif num == 7:
            turn = player7
            await ctx.send("It is <@" + str(player7.id) + ">'s turn.")
    else:
        await ctx.send("A game is already in progress! Finish it before starting a new one.")
    

#players = ["player1","player2","player3","player4","player5","player6"]

@client.command()
async def truth(ctx):
  await ctx.send(random.choice(truths))
  global turn
  global gameOver
  if not gameOver:
    # determine who goes 
        num = random.randint(1,7)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
        elif num == 3:
            turn = player3
            await ctx.send("It is <@" + str(player3.id) + ">'s turn.")
        elif num == 4:
            turn = player4
            await ctx.send("It is <@" + str(player4.id) + ">'s turn.")
        elif num == 5:
            turn = player5
            await ctx.send("It is <@" + str(player5.id) + ">'s turn.")
        elif num == 6:
            turn = player6
            await ctx.send("It is <@" + str(player6.id) + ">'s turn.")
        elif num == 7:
            turn = player7
            await ctx.send("It is <@" + str(player7.id) + ">'s turn.")
  else:
        await ctx.send("Please start a new game.")

@client.command()
async def dare(ctx):
  await ctx.send(random.choice(dares))
  global turn
  global gameOver
  if not gameOver:
    # determine who goes 
        num = random.randint(1,7)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
        elif num == 3:
            turn = player3
            await ctx.send("It is <@" + str(player3.id) + ">'s turn.")
        elif num == 4:
            turn = player4
            await ctx.send("It is <@" + str(player4.id) + ">'s turn.")
        elif num == 5:
            turn = player5
            await ctx.send("It is <@" + str(player5.id) + ">'s turn.")
        elif num == 6:
            turn = player6
            await ctx.send("It is <@" + str(player6.id) + ">'s turn.")
        elif num == 7:
            turn = player7
            await ctx.send("It is <@" + str(player7.id) + ">'s turn.")
  else:
        await ctx.send("Please start a new game.")
  

@client.command()
async def shuffle(ctx):
  global turn
  global gameOver
  if not gameOver:
    # determine who goes 
        num = random.randint(1,7)
        if num == 1:
            turn = player1
            await ctx.send("It is <@" + str(player1.id) + ">'s turn.")
        elif num == 2:
            turn = player2
            await ctx.send("It is <@" + str(player2.id) + ">'s turn.")
        elif num == 3:
            turn = player3
            await ctx.send("It is <@" + str(player3.id) + ">'s turn.")
        elif num == 4:
            turn = player4
            await ctx.send("It is <@" + str(player4.id) + ">'s turn.")
        elif num == 5:
            turn = player5
            await ctx.send("It is <@" + str(player5.id) + ">'s turn.")
        elif num == 6:
            turn = player6
            await ctx.send("It is <@" + str(player6.id) + ">'s turn.")
        elif num == 7:
            turn = player7
            await ctx.send("It is <@" + str(player7.id) + ">'s turn.")
  else:
        await ctx.send("Please start a new game.")

@client.command()
async def end(ctx):
  global gameOver
  global turn
  gameOver = False
  turn = ""


keep_alive()
client.run(os.environ['TOKEN'])
