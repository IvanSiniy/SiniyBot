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
async def copy(message, *, arg):
    await message.channel.send(arg)

@bot.command()
async def hello(message):
    await message.channel.send(":smiley: :wave: Привет!")

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
async def help(message):
    embed = discord.Embed(title= 'Siniy Bot', description= 'Ботик - Котик\nCписок доступных **основных** команд:', color=0xeee657)
    embed.add_field(name="**!cnb_info**", value= 'Получение информации по игре Камень, Ножницы, Бумага!', inline=False)
    embed.add_field(name="**!copy**", value= 'Повторить ваше сообщение', inline=False)
    embed.add_field(name="**!say**", value= 'Написать сообщение в #канал  "Tекст" ', inline=False)
    embed.add_field(name="**!hello**", value= 'Поздороватся с Ботом', inline=False)
    embed.add_field(name="**!moder_help**", value= 'Пока недоступно', inline=False)
    embed.add_field(name="**Invite**", value= '[Invite Link]<https://discordapp.com/oauth2/authorize?client_id=696050756947673108&scope=bot&permissions=7232>', inline=False)
    await message.channel.send(embed=embed)
@bot.command()
async def cnb_info(message):
  await message.channel.send("Для начала игры напиши: \n!cnb (1-3)\n1- Камень, 2-Ножницы , 3-Бумага")

from random import randint
@bot.command()
async def cnb(message, y:int):
 x= randint(1, 3)
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
    await message.channel.send("Введите число от одного то трёх!")

#----------------------------------------------------------------#
# moderation command
import typing
@bot.command()
async def ban(message, members: commands.Greedy[discord.Member],
                   delete_days: typing.Optional[int] = 0, *,
                   reason: str):
    for member in members:
        await member.ban(delete_message_days=delete_days, reason=reason)
        await message.channel.send('Пользователь был забанен')
bot.run(TOKEN)     
 
