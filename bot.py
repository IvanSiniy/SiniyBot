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
class CommandWithCooldown(commands.Command):
    async def prepare(self, message):
        try:
            return await super().prepare(message)
        except commands.CommandOnCooldown:
            await message.channel.send('Подождите 30 секунд прежде чем использовать команду снова!')

@bot.command(cls = CommandWithCooldown)
@commands.cooldown(5, 30, commands.BucketType.user)
async def copy(ctx,*, txt=None):
    if txt==None:
        await ctx.send('''
**Информация о команде:** !copy
Повторю сообщение которое вы написали, при этом удаляя его!
**Пример использования команды:**
`!copy Привет!`
''')
    else:
        await ctx.message.delete()
        await ctx.send(txt)

@bot.command(cls = CommandWithCooldown)
@commands.cooldown(2, 30, commands.BucketType.user)
async def hello(message):
    id = message.author.id
    ping = "<@"+str(id)+">"
    await message.channel.send(":smiley: :wave: Привет ," + ping + '!')


@bot.command(cls = CommandWithCooldown)
@commands.cooldown(3, 30, commands.BucketType.user)
async def say(message, channel : discord.TextChannel, *args,):
    if not channel or not args:
        await message.channel.send("""
**Информация по команде: **!say
Команда используемая для отправки указанного вами сообщения от **моего электронного лица** в указанный вами канал.
**Пример использования команды:**
`!say #канал-для-приветов Привет! `
""")
    else:
        await message.message.delete()
        text = ' '
        for item in args:
            text = text + item + ' '
        await channel.send(text)
@bot.command()
async def help(message):
    embed = discord.Embed(title= 'Siniy Bot', description= 'Cписок доступных **основных** команд:', color=0xeee657)
    embed.add_field(name="**!copy**", value= 'Для получения информации о команде введите !copy', inline=False)
    embed.add_field(name="**!say**", value= 'Для получения информации о команде введите !say ', inline=False)
    embed.add_field(name="**!hello**", value= 'При вызове команды я с вами поздороваюсь :3', inline=False)
    embed.add_field(name="**!moder_help**", value= 'Пока недоступно', inline=False)
    embed.add_field(name="**!ball**", value= 'Для получения информации о команде введите !ball', inline=False)
    embed.add_field(name="**!tryy**", value= 'Для получения информации о команде введите !tryy', inline=False)
    embed.add_field(name="**!roll**", value= 'Для получения информации о команде введите !roll', inline=False)
    embed.add_field(name="**Invite**", value= '[Invite Link]<https://discordapp.com/oauth2/authorize?client_id=696050756947673108&scope=bot&permissions=7232>', inline=False)
    await message.channel.send(embed=embed)

from random import randint
@bot.command(cls = CommandWithCooldown)
@commands.cooldown(10, 30, commands.BucketType.user)
async def cnb(message, yy = None):
    x= randint(1, 3)
    if yy == None or yy!= '1' or yy!= '2' or yy!= '3':
         await message.channel.send("""
**Информация по команде: **!cnb
Это классическая игра "Камень, Ножницы, Бумага!"
Для начала игры выберите одну из цифр: 1 , 2 или 3.
1- Камень, 2-Ножницы , 3-Бумага
**Пример использования команды:**
`!cnb 1`
**Пример ответа:**
Камень vs Бумаги! Ты проиграл!     
""")
    else:
        y= int(yy)
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

from random import randint
@bot.command(cls = CommandWithCooldown)
@commands.cooldown(6, 30, commands.BucketType.user)
async def ball(message,*, soob=None):
    x = randint(1, 10)
    id = message.author.id
    ping = "<@"+str(id)+">"
    if soob==None:
        await message.channel.send("""
**Информация по команде: **!ball
Типичный шарлатанский шарик встряхивая который вы получаете ответ на свой вопрос.
Задавать вопрос нужно так, что бы я мог ответить: Да / Нет
**Пример использования команды:**
`!ball Я котик?`
**Пример ответа:**
**Siniy**, черт возьми! Да! Так оно и есть!:8ball:
""")
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
        await message.channel.send(ping + ', черт возьми! Да! Так оно и есть!:8ball:')


from random import randint
@bot.command(cls = CommandWithCooldown)
@commands.cooldown(4, 30, commands.BucketType.user)
async def tryy(message,*,text=None):
    id = message.author.id
    ping = "<@"+str(id)+">"
    x= randint(1,2)
    if text==None:
        await message.channel.send("""
**Информация по команде: **!tryy
Команда используемая для Role Play моментов в которой вам нужно описать действие, а рандом решит: Удачно или Неудачно
**Пример использования команды:**
`!tryy попытался подняться`
**Пример ответа:** 
**Siniy** попытался подняться | **Неудачно  ** 
""")
    else:
        if x==1:
            await message.channel.send(ping + text+ ' | **Удачно**')
        if x==2:
            await message.channel.send(ping + text + '| **Неудачно**')

from random import randint
@bot.command(cls = CommandWithCooldown)
@commands.cooldown(4, 30, commands.BucketType.user)
async def roll(message, xx=None, yy=None):
    if xx==None or yy==None:
        await message.channel.send("""
**Информация по команде: **!roll
Рандомайзер чисел в диапазоне от x до y
**Пример использования команды:**
`!roll 10 45`
**Пример ответа:**
:game_die: Результат: 34 :game_die:
""")
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
 
