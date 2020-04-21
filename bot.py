import discord
from discord.ext import commands
from random import randint
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
async def command_not_found(message):
    await message.channel.send('Команда не найдена! Введите !help для просмотра списка команд')

class CommandWithCooldown(commands.Command):
    async def prepare(self, message):
        try:
            return await super().prepare(message)
        except commands.CommandOnCooldown:
            await message.channel.send('Подождите 30 секунд прежде чем использовать команду снова!')


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(5, 30, commands.BucketType.user)
async def info(message, user = discord.User):
    embed = discord.Embed(title= '', description= '', color=0xeee657, inline = False)
    embed.add_field(name = "**!copy**", value= 'Для получения информации о команде введите !copy', inline=False)
    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
    await message.channel.send(embed = embed)


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(5, 30, commands.BucketType.user)
async def copy(ctx,*, txt=None):
    if txt==None:
        embed = discord.Embed(title= 'Команда: !copy', description= """
**Описание:** Повторю сообщение которое вы написали, при этом удаляя его!
**Кулдаун:** 5 сообщений за 30 секунд
**Использование:** !сopy [ТЕКСТ]
**Пример использования: **!copy Привет!""", color=0xeee657, inline = False)
        embed.set_author(name = ctx.author, icon_url = ctx.author.avatar_url)
        await ctx.channel.send(embed = embed)
    else:
        await ctx.message.delete()
        await ctx.channel.send(txt)


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(2, 30, commands.BucketType.user)
async def hello(message):
    await message.channel.send(":smiley: :wave: Привет ," + '{}'.format(message.author.mention) + '!')


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(3, 30, commands.BucketType.user)
async def say(message, channel : discord.TextChannel, *args,):
    if not channel or not args:
        embed = discord.Embed(title= 'Команда: !say', description= "**Описание:** Отправляет указанное вами сообщение в указанный вами канал\n**Кулдаун:** 3 сообщений за 30 секунд\n**Использование:** !say #канал [TEКСТ]\n**Пример использования:** !say #канал-для-приветов Привет!", color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)
    else:
        await message.message.delete()
        text = ' '
        for item in args:
            text = text + item + ' '
        await channel.send(text)
@bot.command(cls = CommandWithCooldown, pass_context = True)
async def help(message):
    embed = discord.Embed(title= 'Siniy Bot', description= 'Cписок доступных **основных** команд:', color=0xeee657)
    embed.add_field(name="!copy", value= 'Для получения информации о команде введите !copy', inline=False)
    embed.add_field(name="!say", value= 'Для получения информации о команде введите !say ', inline=False)
    embed.add_field(name="!hello", value= 'При вызове команды я с вами поздороваюсь :3', inline=False)
    embed.add_field(name="!moder_help", value= 'Пока недоступно', inline=False)
    embed.add_field(name="!ball", value= 'Для получения информации о команде введите !ball', inline=False)
    embed.add_field(name="!roll", value= 'Для получения информации о команде введите !roll', inline=False)
    embed.add_field(name="Invite", value= '[Invite Link]\nhttps://discordapp.com/oauth2/authorize?client_id=696050756947673108&scope=bot&permissions=7232', inline=False)
    await message.channel.send(embed=embed)


@bot.command(cls = CommandWithCooldown)
@commands.cooldown(10, 30, commands.BucketType.user)
async def cnb(message, yy = None):
    x= randint(1, 3)
    embed = discord.Embed(title= '', description= "", color=0xeee657, inline = False)
    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
    if yy != None and yy == '1' or yy == '2' or yy == '3':
        y= int(yy)
    #lose
        if x == 1 and y == 2:
            embed.add_field(name='Результат игры:', value = 'Ножницы vs Камня!\n Ты проиграл!')
        elif x == 2 and y == 3:
            embed.add_field(name='Результат игры:', value = 'Бумага vs Ножниц!\nТы проиграл!')
        elif x == 3 and y == 1:
            embed.add_field(name='Результат игры:', value = 'Камень vs Бумаги!\nТы проиграл!')
    #won
        elif x == 2 and y == 1:
            embed.add_field(name='Результат игры:', value = 'Камень vs Ножниц!\nТы победил!')
        elif x == 3 and y == 2:
            embed.add_field(name='Результат игры:', value = 'Ножницы vs Бумаги!\nТы победил!')
        elif x == 1 and y == 3:
            embed.add_field(name='Результат игры:', value = 'Бумага vs Камня!\nТы победил!')
    #draw
        elif x == 1 and y == 1:
            embed.add_field(name='Результат игры:', value = 'Камень vs Камня!\nНичья!')
        elif x == 2 and y == 2:
            embed.add_field(name='Результат игры:', value = 'Ножницы vs Ножниц!\nНичья!')
        elif x == 3 and y == 3:
            embed.add_field(name='Результат игры:', value = 'Бумага vs Бумаги!\nНичья!')
    else:
        embed.add_field(name = 'Команда: !cnb', value = '''
**Описание:** Классическая игра "Камень, Ножницы, Бумага!"
**Кулдаун:** 10 сообщений за 30 секунд
**Использование:** !cnb (1-3)
**Пример использования:** !cnb 1''')
    await message.channel.send(embed = embed)


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(6, 30, commands.BucketType.user)
async def ball(message,*, soob=None):
    spisok = [', абсолютно верно:8ball:', ', судя по моей информации, нет:8ball:', ', я не уверен, спросите еще раз:8ball:',
    ', в базе данных произошла ошибка, повторите вопрос:8ball:', ', скорее да, чем нет:8ball:',
    ', ну вообще да, но как бы нет:8ball:', ', в базе данных произошла ошибка, повторите вопрос:8ball:',
    ', в теории да, на практике еще не известно:8ball:', ', полностью уверен что нет:8ball:', ', у вас все в порядке?С такими вопросами вам в дурку:8ball:',
    ', черт возьми! Да! Так оно и есть!:8ball:']
    l = len(spisok)
    x = randint(0, l-1)
    if soob==None:
        embed = discord.Embed(title= 'Команда: !ball', description= "**Описание:** Типичный шарлатанский шарик встряхивая который вы получаете ответ на свой вопрос.\nЗадавать вопрос нужно так, что бы я мог ответить: Да / Нет\n**Кулдаун:** 6 сообщений за 30 секунд\n**Использование:** !ball [TEКСТ]\n**Пример использования:** !ball Я котик?", color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        await message.channel.send(embed = embed)
    else:
        await message.channel.send('{}'.format(message.author.mention) + str(spisok[x]))


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(4, 30, commands.BucketType.user)
async def roll(message, yy=None):
    embed = discord.Embed(title= '', description= "", color=0xeee657, inline = False)
    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
    if yy==None:
        embed.add_field(name = 'Команда: !roll', value = """
**Описание:** Рандомайзер чисел в диапазоне от 1 до х
**Кулдаун:** 4 сообщения за 30 секунд
**Использование:** !roll [число]
**Пример использования**: !roll 45
""")
    else:
        y=int(yy)
        r=randint(1,y)
        embed.add_field(name = 'Результат:', value = ':game_die: {}'.format(r)+' :game_die:')
    await message.channel.send(embed = embed)
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
 
