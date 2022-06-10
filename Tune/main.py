import os
import pafy
import discord
import asyncio
import youtube_dl
from discord.ext import commands
import urllib.parse,urllib.request,re
from side import keep_alive
from side2 import mix1,mix2,premix1,premix2
#from side import keep_alive,mix1,mix2,premix1,premix2
#from pyg import mix1,mix2,premix1,premix2





client = commands.Bot(command_prefix="$")


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))



@client.command()
async def play(ctx, *,search):
    song_there = os.path.isfile("song.webm")
    try:
        if song_there:
            os.remove("song.webm")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return
    query_string = urllib.parse.urlencode({'search_query':search})
    htm_content = urllib.request.urlopen('https://www.youtube.com/results?'+ query_string)
    search_results = re.findall(r"watch\?v=(\S{11})", htm_content.read().decode())
    global url
    url = 'https://youtube.com/watch?v=' + search_results[0]
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='Lounge')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': '251'
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download(['https://youtube.com/watch?v=' + search_results[0]])
    for file in os.listdir("./"):
        if file.endswith(".webm"):
            os.rename(file, "song.webm")
    voice.play(discord.FFmpegOpusAudio("song.webm"))
    await ctx.send("**Currently Playing : **" + 'https://youtube.com/watch?v=' + search_results[0])
    premix1()
    




@client.command()
async def next(ctx, *,searchq):
    ct = mix1()
    qsong_there = os.path.isfile("qsong.webm")
    song_there = os.path.isfile("song.webm")

    query_stringq = urllib.parse.urlencode({'search_query':searchq})
    htm_contentq = urllib.request.urlopen('https://www.youtube.com/results?'+ query_stringq)
    search_resultsq = re.findall(r"watch\?v=(\S{11})", htm_contentq.read().decode())

    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_optsq = {
        'format': '251'
    }
    if voice.is_playing():
      if song_there:
        with youtube_dl.YoutubeDL(ydl_optsq) as ydl:
            ydl.download(['https://youtube.com/watch?v=' + search_resultsq[0]])
        for file in os.listdir("./"):
            if file.endswith(".webm"):
                os.rename(file, "qsong.webm")
        await ctx.send("**Playing Next : **" + 'https://youtube.com/watch?v=' + search_resultsq[0])
        
        video = pafy.new(url)
        await asyncio.sleep(video.length - (ct + 30))
        voice.play(discord.FFmpegOpusAudio("qsong.webm"))
        await ctx.send("**Currently Playing : **" + 'https://youtube.com/watch?v=' + search_resultsq[0])
        global urlq
        urlq = 'https://youtube.com/watch?v=' + search_resultsq[0]
        premix2()
        
      if qsong_there:
        ct = mix2()
        with youtube_dl.YoutubeDL(ydl_optsq) as ydl:
            ydl.download(['https://youtube.com/watch?v=' + search_resultsq[0]])
        for file in os.listdir("./"):
            if file.endswith(".webm"):
                os.rename(file, "qsong.webm")
        await ctx.send("**Playing Next : **" + 'https://youtube.com/watch?v=' + search_resultsq[0])
        video = pafy.new(urlq)
        await asyncio.sleep(video.length - (ct + 30))
        voice.play(discord.FFmpegOpusAudio("qsong.webm"))
        await ctx.send("**Currently Playing : **" + 'https://youtube.com/watch?v=' + search_resultsq[0])
        urlq = 'https://youtube.com/watch?v=' + search_resultsq[0] 


@client.command()
async def skip(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        voice.stop()
        voice.play(discord.FFmpegOpusAudio("qsong.webm"))
    else:
        await ctx.send("The bot is not connected to a voice channel.")

@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def youtube(ctx, *,search):
  query_string = urllib.parse.urlencode({'search_query':search})
  htm_content = urllib.request.urlopen('https://www.youtube.com/results?'+ query_string)
  search_results = re.findall(r"watch\?v=(\S{11})", htm_content.read().decode())
  await ctx.send('https://youtube.com/watch?v=' + search_results[0])

keep_alive()
client.run(os.environ['TOKEN'])