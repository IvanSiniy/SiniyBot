import discord
from discord.ext import commands
TOKEN = 'Njk2MDUwNzU2OTQ3NjczMTA4.Xom9sw.xr1VsHitF9TBSV3CWaQQc5DohT4'
prefix = '!'
bot = commands.Bot(command_prefix= prefix)
bot.remove_command('help')
@bot.event
async def on_ready():
    print('------')
    print('Вы зашли как:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.command()
async def copy(ctx, *, arg):
    await ctx.send(arg)

@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(a+b)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(a*b)

@bot.command()
async def hello(ctx):
    await ctx.send(":smiley: :wave: Привет!")

@bot.command()
async def say(ctx, channel : discord.TextChannel, *args):
    await ctx.message.delete()
    if not args:
        await ctx.send('Необходимо ввести текст сообщения')
        return
    text = ' '
    for item in args:
        text = text + item + ' '
    await channel.send(text)
@bot.command()
async def callsiniy(message):
 await message.channel.send("<@309299318337044483>")
@bot.command()
async def help(message):
 await message.channel.send("Список доступных команд: \n**cnb_info** - получение информации по игре Камень, Ножницы, Бумага!\n**help** - список команд\n**copy** - повторить ваше сообщение\n**add** - cчитает сумму из двух чисел\n**multiply** - умножает два числа\n**say** - написать сообщение в #канал -место текста- \n**hello** - поздоровается с тобой")
import typing

@bot.command()
async def ban(ctx, members: commands.Greedy[discord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)
        await ctx.send('Пользователь был забанен')

import random
@bot.command()
async def cnb(message, y: int):
 x= random.randint(1, 3)
 #lose
 if x == 1 and y == 2:
     await message.channel.send("Ножцницы vs Камня! Ты проиграл!")
 elif x == 2 and y == 3:
     await message.channel.send("Бумага vs Ножниц! Ты проиграл!")
 elif x == 3 and y == 1:
     await message.channel.send("Камень vs Бумаги! Ты проиграл!")
 #won
 elif x == 2 and y == 1:
     await message.channel.send("Камень vs Ножниц! Ты победил!")
 elif x == 3 and y == 2:
     await message.channel.send("Ножницы vs Бумаги! Ты победил!")
 elif x == 1 and y == 3:
     await message.channel.send("Бумага vs Камня! Ты победил!")
 #draw
 elif x == 1 and y == 1:
    await message.channel.send("Камень vs Камня! Ничья!")
 elif x == 2 and y == 2:
    await message.channel.send("Ножницы vs Ножниц! Ничья!")
 elif x == 3 and y == 3:
    await message.channel.send("Бумага vs Бумаги! Ничья!")
 else:
    await message.channel.send("Шо?")
@bot.command()
async def cnb_info(message):
  await message.channel.send("Для начала игры напиши: !cnb (1-3)\n1- Камень, 2-Ножницы , 3-Бумага")
bot.run(TOKEN)     
 
