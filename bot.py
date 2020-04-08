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
async def copy(ctx,*, txt=None):
    if txt==None:
        await ctx.send('Введите сообщение которое бот должен повторить!')
    else:
        await ctx.message.delete()
        await ctx.send(txt)

@bot.command()
async def hello(message):
    id = message.author.id
    ping = "<@"+str(id)+">"
    await message.channel.send(":smiley: :wave: Привет," + ping + '!')

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
    embed.add_field(name="**!cnb_info**", value= 'Получение информации по игре "Камень, Ножницы, Бумага!"', inline=False)
    embed.add_field(name="**!copy**", value= 'Повторить ваше сообщение', inline=False)
    embed.add_field(name="**!say**", value= 'Написать сообщение в #канал  "Tекст" ', inline=False)
    embed.add_field(name="**!hello**", value= 'Поздороватся с Ботом', inline=False)
    embed.add_field(name="**!moder_help**", value= 'Пока недоступно', inline=False)
    embed.add_field(name="**!ball**", value= 'Задать боту вопрос, ответом на который будет да/нет', inline=False)
    embed.add_field(name="**!tryy**", value= 'Написать действие которые будет выполнено (**Удачно | Неудачно**)', inline=False)
    embed.add_field(name="**!roll**", value= 'Рандомайзер чисел от x до y', inline=False)
    embed.add_field(name="**Invite**", value= '[Invite Link]<https://discordapp.com/oauth2/authorize?client_id=696050756947673108&scope=bot&permissions=7232>', inline=False)
    await message.channel.send(embed=embed)
@bot.command()
async def cnb_info(message):
    await message.channel.send("""Для начала игры напиши:
!cnb (1-3)
1- Камень, 2-Ножницы , 3-Бумага""")

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

from random import randint
@bot.command()
async def ball(message,*, soob=None):
    x = randint(1, 10)
    id = message.author.id
    ping = "<@"+str(id)+">"
    if soob==None:
        await message.channel.send(ping+', напишите свой вопрос!:8ball:')
    elif x==1:
        await  message.channel.send(ping + ', абсолютно верно:8ball:')
    elif x==2:
        await  message.channel.send(ping + ', судя по моей информации, нет:8ball:')
    elif x==3:
        await message.channel.send(ping + ', я не уверен, спросите еще раз:8ball:')
    elif x==4:
        await message.channel.send(ping + ', в базе данных произошла ошибка, повторите вопрос:8ball:')
    elif x==5:
        await message.channel.send(ping + ', скорее да, чем нет:8ball:')
    elif x==6:
        await message.channel.send(ping + ', ну вообще да, но как бы нет:8ball:')
    elif x==7:
        await message.channel.send(ping + ', в теории да, на практике еще не известно:8ball:')
    elif x==8:
        await message.channel.send(ping + ', полностью уверен что нет:8ball:')
    elif x==9:
        await message.channel.send(ping + ', у вас все в порядке?С такими вопросами вам в дурку:8ball:')
    elif x==10:
        await message.channel.send(ping + ', даже не знаю что ответить, да или нет:8ball:')


from random import randint
@bot.command()
async def tryy(message,arg):
    id = message.author.id
    ping = "<@"+str(id)+">"
    x= randint(1,2)
    if x==1:
        await message.channel.send(ping +', ' + arg + ' | **Удачно**')
    if x==2:
        await message.channel.send(ping +', ' + arg + '| **Неудачно**')

from random import randint
@bot.command()
async def roll(message, xx=None, yy=None):
    if xx==None or yy==None:
        await message.channel.send(':game_die: Введите два числа! :game_die:')
    else:
        x=int(xx)
        y=int(yy)
        r=randint(x,y)
        res= str(r)
        await message.channel.send(':game_die: Результат: '+res+' :game_die:')
#----------------------------------------------------------------#
# moderation command
import typing
@bot.command()
async def ban_nach(message, members: commands.Greedy[discord.Member],
                delete_days: typing.Optional[int] = 0,*,
                reason=None):
    if reason == None:
        await message.channel.send('Укажите причину!')
    else:
        for member in members:
            await member.ban(delete_message_days=delete_days, reason=reason)
            await message.channel.send('Пользователь был забанен по причине: '+reason)
bot.run(TOKEN)     
 
