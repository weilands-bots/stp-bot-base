import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from stpSongList import songList
import requests
from discord.ext import commands

# Set up the bot with a prefix
intents = discord.Intents.default()
intents.members = True  # Make sure the bot has permission to read member updates

load_dotenv()
    
TOKEN = os.getenv('DISCORD_TOKEN')
    
intents = discord.Intents.default()
client = discord.Client(intents=intents)
intents.message_content = True
    
    
bot = commands.Bot(command_prefix='!', intents=intents)
    
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!') 

@bot.command(name='lyrics')

async def lyrics(ctx, *, arg1=None):
    if arg1 is not None and arg1 in songList:
        url = f'https://api.lyrics.ovh/v1/Stone%20Temple%20Pilots/{arg1}'
    
        response = requests.get(url)

            
        data = response.json()
        j = data['lyrics'].replace("\n\n", "\n")
        await ctx.send("Lyrics for *"+arg1+"*:\n"+j)
    elif arg1 is None:
        await ctx.send("You need to give a song, ya big goof.")
    else: 
            await ctx.send("Song not in song list.")  
        
bot.run(TOKEN)