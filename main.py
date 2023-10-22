import discord 
from settings import settings
from bot_logic import *
from discord.ext import commands
import os
import requests
# Zmienna intencje przechowuje uprawnienia bota
intents = discord.Intents.default()
# Włączanie uprawnienia do czytania wiadomości
intents.message_content = True
# Tworzenie bota w zmiennej klienta i przekazanie mu uprawnień
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='!', intents=intents)
#@bot.event
#async def on_ready():
#    print(f'Zalogowaliśmy się jako {bot.user}')
#def get_duck_image_url():    
#    url = 'https://random-d.uk/api/random'
#    res = requests.get(url)
#    data = res.json()
#    return data['url']


#@bot.command('duck')
#async def duck(ctx):
#    '''Po wywołaniu polecenia duck program wywołuje funkcję get_duck_image_url'''
#    image_url = get_duck_image_url()
#    await ctx.send(image_url)
#@bot.command()
#async def hello(ctx):
#    await ctx.send(f'Cześć, jestem bot{bot.user}!')
#@bot.command()
#async def heh(ctx, count_heh = 5):
#    await ctx.send("he" * count_heh)
#@bot.command()
#async def mem(ctx):
#    img_name = random.choice(os.listdir('images'))
#    with open(f'images/{img_name}', 'rb') as f:
#        picture = discord.File(f)
#
#    await ctx.send(file=picture)
#@bot.command()
#async def sigma(ctx):
#    with open('images/sigma.gif', 'rb') as f:
#        picture = discord.File(f)
#    await ctx.send(file=picture)
async def on_ready():
    print(f'Zalogowano jako {bot.user.name}')
plastik = ['butelka z plastiku', 'opakowanie z plastiku', 'plastikowa torba', 'butelka']
szklo = ['butelka szklana', 'słoik szklany']
papier = ['karton', 'gazeta', 'opakowanie papierowe']
@bot.command()
async def sortuj(ctx, *, rzecz: str):
    if rzecz.lower() in plastik:
        await ctx.send('Rzecz jest z plastiku. Wrzuć ją do kosza na plastik.')
    elif rzecz.lower() in szklo:
        await ctx.send('Rzecz jest ze szkła. Wrzuć ją do kontenera na szkło.')
    elif rzecz.lower() in papier:
        await ctx.send('Rzecz jest z papieru. Wrzuć ją do kosza na papier.')
    else:
        await ctx.send('Nie jestem pewien, gdzie wrzucić tę rzecz.')
@bot.command()
async def rozkładanie(ctx, przedmiot: str):
    if przedmiot in plastik:
        await ctx.send(f'plastik rozkłada się przez około 450 lat.')
    elif przedmiot in szklo:
        await ctx.send(f'szkło rozkłada się przez około 4000 lat.')
    elif przedmiot in papier:
        await ctx.send(f'papier rozkłada się od nawet kilku tygodni do około pół roku.')
    else:
        await ctx.send(f'nie wiem')
@bot.command()
async def dodaj_smiec(ctx, przedmiot, material):
    if material == 'plastik':
        plastik.append(przedmiot)
        await ctx.send(f'dodano do listy')
    elif material == 'szkło':
        szklo.append(przedmiot)
        await ctx.send(f'dodano do listy')
    elif material == 'papier':
        papier.append(przedmiot)
        await ctx.send(f'dodano do listy')
    else:
        await ctx.send('nie mam takiego materiału')
damage_data = {
    'plastik': 'Wysoka szkodliwość dla środowiska, nie ulega rozkładowi.',
    'szklo': 'Niska szkodliwość, ulega rozkładowi w około 1 milion lat.',
    'papier': 'Średnia szkodliwość, rozkłada się w około 2-5 miesięcy.',
}
@bot.command()
async def szkodliwosc(ctx, przedmiot):
    if przedmiot in plastik:
            await ctx.send('przenosi szkody dla środowiska jest to wysoka szkodliwość dla środowiska, nie ulega rozkładowi.')
    if przedmiot in papier:
            await ctx.send('przenosi szkody dla środowiska jest to średnia szkodliwość, rozkłada się w około 2-5 miesięcy.')
    if przedmiot in szklo:
            await ctx.send('przenosi szkody dla środowiska jest to niska szkodliwość, ulega rozkładowi w około 1 milion lat.')
bot.run(settings['TOKEN'])
