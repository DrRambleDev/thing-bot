import discord
from discord import message
from discord import app_commands
from discord.ext import commands
from discord.ext import tasks
from discord.utils import get
from config import token
import datetime
from datetime import date, time
#from datetime import datetime

# Use default discord gateway intents
intents = discord.Intents.default()
intents.message_content = True

#client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix = "!", intents = discord.Intents.all())

# ** Global functions that are useful

def isTime(time):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    if current_time == time:
        return True
    else:
        return False
    
# **  Time defines ** #

local_tz = datetime.datetime.now().astimezone().tzinfo
goodNightTime = datetime.time(hour=15, minute=5, tzinfo=local_tz)
print("Goodnight time: ", goodNightTime)

# ** Tasks section ** #

@tasks.loop(time = goodNightTime)
async def Goodnight():
    print("Nigh Nigh")
    channel = bot.get_channel(1284357714708922443)
    await channel.send("Sleep ffs")
    print("It works")

@tasks.loop(minutes = 1)
async def Good_night_2():
    print("1 minute interval")
    print('current time', datetime.datetime.now())
    channel = bot.get_channel(1284357714708922443)
    await channel.send("1 minute interval")


# ** Events section ** #

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
    if not Goodnight.is_running():
        Goodnight.start()
        print("Good night task started")
    if not Good_night_2.is_running():
        Good_night_2.start()
        print("this shi running")

    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} commands")
    except Exception as e:
        print(f"Error syncing commands: {e}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('I\'m'):
        messageContent = message.content
        newstr = messageContent.replace("I'm", "")
        await message.channel.send(f'Hi{newstr}! I\'m Dad!')
    
    if message.content.startswith('im'):
        content = message.content
        newerStr = content.replace("im", "")
        await message.channel.send(f'Hi{newerStr}! I\'m Dad!')

# ** Commands section ** #

# Example command with a simple slash command
@bot.tree.command(name = "ping", description = "Replies with pong!")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("pong")

# Example command to show options
@bot.tree.command(name = "test", description = "To test discord.py options, ignore")
@app_commands.describe(thing_to_say = "What to say?")
async def test(interaction: discord.Interaction, thing_to_say: str):
    await interaction.response.send_message(f"{thing_to_say}")


bot.run(token)

'''

bot = commands.Bot(command_prefix='&', intents=intents)

goodNightTime = datetime.time(hour=19, minute=46) #Create the time on which the task should always run
print('goodNightTime: ', goodNightTime)

@tasks.loop(time=goodNightTime) #Create the task
async def Goodnight():
    print("BEGIN GOODNIGHT!!!!!!!!!!!")
    channel = bot.get_channel(522975347759775759)
    await channel.send("Good night! Make sure to go to sleep early, and get enough sleep!")
    print("Night Working")

@tasks.loop(minutes=1) #Create the task
async def Good_night_2():
    print("1 min interval")
    print('current time: ', datetime.datetime.now())
    channel = bot.get_channel(522975347759775759)
    await channel.send("1 min interval")


@bot.event
async def on_ready():
    if not Goodnight.is_running():
        Goodnight.start() #If the task is not already running, start it.
        print("Good night task started")
    if not Good_night_2.is_running():
        Good_night_2.start() #If the task is not already running, start it.
        print("Good night 2 task started")

local_tz = datetime.datetime.now().astimezone().tzinfo
goodNightTime = datetime.time(hour=19, minute=46, tzinfo=local_tz)

'''