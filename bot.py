import discord
from discord.ext import commands
from random import randint
import time
import datetime
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
    handle = open("botlog.txt", 'a')
    today = datetime.datetime.today()
    write = today.strftime("[%d/%m/%Y %H:%M]")+' BOT START'+'\n'
    handle.write(write)
    handle.close()

class CommandWithCooldown(commands.Command):
    async def prepare(self, message):
        try:
            return await super().prepare(message)
        except commands.CommandOnCooldown:
            await message.channel.send('Подождите 30 секунд прежде чем использовать команду снова!')


@bot.command(pass_context=True)
async def clear(message , amount=None):
    today = datetime.datetime.today()
    embed = discord.Embed( color=0xeee657, inline = False)
    embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
    if amount == None:
        embed.add_field(name = 'Информация о команде: !clear', value = '''
**Описание:** Удаляет указанное количество сообщений в канале (Не трогая закрепленные)
**Использование:** `!clear [КОЛ-ВО]`
**Пример использования: **`!clear 10`
''')
    else:
        await message.channel.purge(limit=int(amount), check=lambda msg: not msg.pinned)
        embed.add_field(name = 'Выполнение команды', value = 'Было удалено {} сообщений :white_check_mark:'.format(amount))
    await message.channel.send(embed = embed)
    handle = open("botlog.txt", 'a')
    write = today.strftime("[%d/%m/%Y %H:%M] ")+ str(message.author)+ ' used command "clear" in server:'+message.author.guild.name+' ID SERVER:'+str(message.author.guild.id)+'\n'
    handle.write(write)
    handle.close()

@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(5, 30, commands.BucketType.user)
async def user(message, user: discord.Member = None):
    if user == None:
        user = message.author
    embed = discord.Embed( color=0xeee657, inline = False)
    embed.add_field(name = 'ID Пользователя',value='{}'.format(user.id), inline=False)
    embed.add_field(name = 'Присоединился к серверу',value='{}'.format(user.joined_at.__format__('%d/%m/%Y %H:%M')), inline=False)
    embed.add_field(name = 'Создан аккаунт в дискорд',value='{}'.format(user.created_at.__format__('%d/%m/%Y %H:%M')), inline=False)
    embed.add_field(name = 'Самая высокая роль',value='{}'.format(user.top_role.mention), inline=False)
    roles = []
    for x in user.roles:
        roles.append(x.name)
    roles.reverse()
    embed.add_field(name = 'Роли[{}]'.format(len(user.roles)),value='{}'.format(", ".join(map(str, roles))), inline=False)
    embed.set_author(name = user, icon_url = user.avatar_url)
    embed.set_thumbnail(url = user.avatar_url)
    today = datetime.datetime.today()
    embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
    await message.channel.send(embed = embed)
    handle = open("botlog.txt", 'a')
    write = today.strftime("[%d/%m/%Y %H:%M] ")+ str(message.author)+ ' used command "user" in server:'+message.author.guild.name+' ID SERVER:'+str(message.author.guild.id)+'\n'
    handle.write(write)
    handle.close()


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(5, 30, commands.BucketType.user)
async def server(message, guild : discord.Guild = None):
    guild = message.author.guild
    embed = discord.Embed( color=0xeee657, inline = False)
    embed.add_field(name = 'ID Сервера',value='{}'.format(guild.id), inline=False)
    embed.add_field(name = 'Владелец',value='<@{}>'.format(guild.owner_id), inline=False)
    embed.add_field(name = 'Сервер создан',value='{}'.format(guild.created_at.__format__('%d/%m/%Y %H:%M')), inline=False)
    embed.add_field(name = 'Категории и каналы',value='Категорий: {}\nКаналов: {} ({} текстовых | {} голосовых)'.format(len(guild.categories),len(guild.channels)-len(guild.categories),len(guild.text_channels),len(guild.voice_channels)), inline=False)
    embed.add_field(name = 'Количество участников',value='{}'.format(len(guild.members)), inline=False)
    embed.add_field(name = 'Количество ролей',value='{}'.format(len(guild.roles)), inline=False)
    embed.set_author(name = guild.name, icon_url = guild.icon_url)
    embed.set_thumbnail(url = guild.icon_url)
    today = datetime.datetime.today()
    embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
    await message.channel.send(embed = embed)
    handle = open("botlog.txt", 'a')
    write = today.strftime("[%d/%m/%Y %H:%M] ")+ str(message.author)+ ' used command "guild" in server:'+message.author.guild.name+' ID SERVER:'+str(message.author.guild.id)+'\n'
    handle.write(write)
    handle.close()


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(5, 30, commands.BucketType.user)
async def role(message, role: discord.Role = None):
    today = datetime.datetime.today()
    if role == None:
        embed = discord.Embed( color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
        embed.add_field(name = 'Информация о команде: !role', value = '''
**Описание:** Выдает информацию о роли
**Использование:** `!role [РОЛЬ]`
**Пример использования: **`!role @МояРоль`
''')
    else:
        embed = discord.Embed(description = '{}'.format(role.mention) , color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        embed.add_field(name = 'ID',value='{}'.format(role.id), inline=False)
        embed.add_field(name = 'Дата создания',value='{}'.format(role.created_at.__format__('%d/%m/%Y %H:%M')), inline=False)
        embed.add_field(name = 'Позиция',value='{}/{}'.format(len(message.author.guild.roles)-role.position, len(message.author.guild.roles)), inline=False)
        embed.add_field(name = 'Количество людей имеющих роль',value='{}'.format(len(role.members)), inline=False)
        embed.add_field(name = 'Цвет',value='{}'.format(role.colour), inline=False)
    await message.channel.send(embed = embed)
    handle = open("botlog.txt", 'a')
    write = today.strftime("[%d/%m/%Y %H:%M] ")+ str(message.author)+ ' used command "role" in server:'+message.author.guild.name+' ID SERVER:'+str(message.author.guild.id)+'\n'
    handle.write(write)
    handle.close()

@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(5, 30, commands.BucketType.user)
async def invite(message):
    await message.channel.send('Ссылка на приглашение: <https://discordapp.com/oauth2/authorize?client_id=696050756947673108&scope=bot&permissions=7232>')
    handle = open("botlog.txt", 'a')
    today = datetime.datetime.today()
    write = today.strftime("[%d/%m/%Y %H:%M] ")+ str(message.author)+ ' used command "invite" in server:'+message.author.guild.name+' ID SERVER:'+str(message.author.guild.id)+'\n'
    handle.write(write)
    handle.close()


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(5, 30, commands.BucketType.user)
async def copy(message,*, txt=None):
    today = datetime.datetime.today()
    if txt==None:
        embed = discord.Embed(title= 'Команда: !copy', description= """
**Описание:** Повторю сообщение которое вы написали, при этом удаляя его!
**Кулдаун:** 5 сообщений за 30 секунд
**Использование:** `!сopy [ТЕКСТ]`
**Пример использования: **`!copy Привет!`""", color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
        await message.channel.send(embed = embed)
    else:
        await message.message.delete()
        await message.channel.send(txt)
    handle = open("botlog.txt", 'a')
    write = today.strftime("[%d/%m/%Y %H:%M] ")+ str(message.author)+ ' used command "copy" in server:'+message.author.guild.name+' ID SERVER:'+str(message.author.guild.id)+'\n'
    handle.write(write)
    handle.close()


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(2, 30, commands.BucketType.user)
async def hello(message):
    await message.channel.send(":smiley: :wave: Привет ," + '{}'.format(message.author.mention) + '!')


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(3, 30, commands.BucketType.user)
async def say(message, channel : discord.TextChannel, *args,):
    today = datetime.datetime.today()
    if not channel or not args:
        embed = discord.Embed(title= 'Команда: !say', description= "**Описание:** Отправляет указанное вами сообщение в указанный вами канал\n**Кулдаун:** 3 сообщений за 30 секунд\n**Использование:** `!say #канал [TEКСТ]`\n**Пример использования:** `!say #канал-для-приветов Привет!`", color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
        await message.channel.send(embed = embed)
    else:
        await message.message.delete()
        text = ' '
        for item in args:
            text = text + item + ' '
        await channel.send(text)
    handle = open("botlog.txt", 'a')
    write = today.strftime("[%d/%m/%Y %H:%M] ")+ str(message.author)+ ' used command "say" in server:'+message.author.guild.name+' ID SERVER:'+str(message.author.guild.id)+'\n'
    handle.write(write)
    handle.close()


@bot.command(cls = CommandWithCooldown, pass_context = True)
async def help(message):
    embed = discord.Embed(title= 'Cписок доступный команд:', description= '''
*Для получения детальной информации о команде введите:* `!КОМАНДА`
`!user` - Информация о пользователе
`!server` - Информация о сервере
`!role` - Информация о роли
`!clear` - Чистильщик сообщений
`!copy` - Отправка вашего сообщения в текущий канал
`!say` - Отправка вашего сообщения в  указанный канал
`!ball` - Магический шар предсказаний и судьбы
`!roll` - Кубик :3
''', color=0xeee657)
    today = datetime.datetime.today()
    embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
    await message.channel.send(embed=embed)


@bot.command(cls = CommandWithCooldown)
@commands.cooldown(10, 30, commands.BucketType.user)
async def cnb(message, yy = None):
    x= randint(1, 3)
    embed = discord.Embed(color=0xeee657, inline = False)
    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
    today = datetime.datetime.today()
    embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
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
**Использование:** `!cnb (1-3)`
**Пример использования:** `!cnb 1`''')
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
        embed = discord.Embed(title= 'Команда: !ball', description= "**Описание:** Типичный шарлатанский шарик встряхивая который вы получаете ответ на свой вопрос.\nЗадавать вопрос нужно так, что бы я мог ответить: Да / Нет\n**Кулдаун:** 6 сообщений за 30 секунд\n**Использование:** `!ball [TEКСТ]`\n**Пример использования:** `!ball Я котик?`", color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        today = datetime.datetime.today()
        embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
        await message.channel.send(embed = embed)
    else:
        await message.channel.send('{}'.format(message.author.mention) + str(spisok[x]))


@bot.command(cls = CommandWithCooldown, pass_context = True)
@commands.cooldown(4, 30, commands.BucketType.user)
async def roll(message, yy=None):
    embed = discord.Embed(color=0xeee657, inline = False)
    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
    today = datetime.datetime.today()
    embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
    if yy==None:
        embed.add_field(name = 'Команда: !roll', value = """
**Описание:** Рандомайзер чисел в диапазоне от 1 до х
**Кулдаун:** 4 сообщения за 30 секунд
**Использование:** `!roll [число]`
**Пример использования**: `!roll 45`
""")
    else:
        y=int(yy)
        r=randint(1,y)
        embed.add_field(name = 'Результат:', value = ':game_die: {}'.format(r)+' :game_die:')
    await message.channel.send(embed = embed)

bot.run(TOKEN)     
 




    