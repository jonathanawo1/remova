import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# List of dares
dares = [
    "Do 10 pushups",
    "Sing a song chosen by the group",
    "Post an embarrassing photo on social media",
    "Let the group ask you any question and you must answer truthfully",
    "Do a silly dance for 1 minute",
    "Imitate a celebrity of the group's choosing",
    "Let someone write a text to anyone from your phone",
    "Wear socks on your hands until your next turn",
    "Speak in an accent until your next turn",
    "Do an impression of another player until someone can guess who you are",
    "Let the person to your right draw on your face with a pen",
    "Talk in a high-pitched voice until your next turn",
    "Imitate an animal and have others guess what you are",
    "Hold your breath for 10 seconds",
    "Eat a spoonful of a condiment chosen by the group",
    "Do your best impression of a baby being born",
    "Make a funny face and keep it that way until the next round",
    "Act like a mime until your next turn",
    "Do your best chicken dance outside on the lawn",
    "Call a random person and sing Happy Birthday to them",
    "Let another player redo your hairstyle"
]

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(name='dare')
async def dare(ctx):
    dare = random.choice(dares)
    await ctx.send(f'{ctx.author.mention}, your dare is: {dare}')

bot.run('MTI2NjE4ODQ1MzA1MDA2MDg5MQ.GHj-Tc._9qSVjoH4SNLYLiO3A_S_fWncy-60C6U_8mV14')
