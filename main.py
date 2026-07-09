import discord
from discord.ext import commands
from model import get_class
from bot_AI.simulado import gerar_simulado, rodar_simulado
import os, random
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')


@bot.command()
async def check(ctx):
    if ctx.message.attachments:
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_url = attachment.url
            await attachment.save(f"./{attachment.filename}")
            await ctx.send(get_class(model_path="./keras_model.h5", labels_path="labels.txt", image_path=f"./{attachment.filename}"))
    else:
        await ctx.send("You forgot to upload the image :(")

@bot.command()
async def vivo(ctx):
    await ctx.send("Sim!!! Estou aqui para te ajudar!")

@bot.command()
async def sorteio(ctx):
    numero = random.randint(1, 100)
    await ctx.send(f"🎲 O número sorteado é: {numero}")

@bot.command()
async def simulado(ctx):
    await rodar_simulado(ctx, bot)

def emoji_aleatorio():
    emojis = ['😀', '😁', '🤣','😇','🥰','🥲','🤪','🤑','🫣','😑','😒','😪','😷','🤢','😭','🥵','🥶','🥹','💩','😫','🤬','😤','😈','🤡']
    return random.choice(emojis)

@bot.command()
async def emoji(ctx):
    emoji_de_hoje = emoji_aleatorio()
    await ctx.send(f'Seu emoji de hoje é..... {emoji_de_hoje}')

bot.run('SEU TOKEN AQUI VIU!')
