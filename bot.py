import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
import random
from random import randint
import time
import datetime
TOKEN = 'ODA5MzY5MTA1MjA3MTMyMjEw.YCUFuA._geaVjCe-KUPhXfHHUUOOgigAec'
prefix = 's!'
bot = commands.Bot(command_prefix= prefix)
bot.remove_command('help')
@bot.event
async def on_ready():
    print('------')
    print('Вы зашли как:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send('Вы можете использовать команду через {} секунд'.format(round(error.retry_after, 2)))
    if isinstance(error, MissingPermissions):
        await ctx.send('У вас недостаточно прав!')

@bot.command(pass_context=True)
@has_permissions(manage_messages = True)
async def clear(message , amount=None):
    today = datetime.datetime.today()
    embed = discord.Embed( color=0xeee657, inline = False)
    embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
    if amount == None:
        embed.add_field(name = 'Информация о команде: clear', 
        value = '**Описание:** Удаляет указанное количество сообщений в канале (Не трогая закрепленные)\n**Использование:** `s!clear [КОЛ-ВО]`\n**Пример использования: **`s!clear 10`')
    else:
        await message.channel.purge(limit=int(amount), check=lambda msg: not msg.pinned)
        embed.add_field(name = 'Выполнение команды', value = 'Было удалено {} сообщений :white_check_mark:'.format(amount))
    await message.channel.send(embed = embed)

@bot.command(pass_context = True)
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
    
@bot.command(pass_context = True)
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
    
@bot.command(pass_context = True)
@commands.cooldown(5, 30, commands.BucketType.user)
async def role(message, role: discord.Role = None):
    today = datetime.datetime.today()
    if role == None:
        embed = discord.Embed( color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
        embed.add_field(name = 'Информация о команде: role', 
        value = '**Описание:** Выдает информацию о роли\n**Использование:** `s!role [РОЛЬ]`\n**Пример использования: **`s!role @МояРоль`')
    else:
        embed = discord.Embed(description = '{}'.format(role.mention) , color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        embed.add_field(name = 'ID',value='{}'.format(role.id), inline=False)
        embed.add_field(name = 'Дата создания',value='{}'.format(role.created_at.__format__('%d/%m/%Y %H:%M')), inline=False)
        embed.add_field(name = 'Позиция',value='{}/{}'.format(len(message.author.guild.roles)-role.position, len(message.author.guild.roles)), inline=False)
        embed.add_field(name = 'Количество людей имеющих роль',value='{}'.format(len(role.members)), inline=False)
        embed.add_field(name = 'Цвет',value='{}'.format(role.colour), inline=False)
    await message.channel.send(embed = embed)
    
@bot.command(pass_context = True)
@commands.cooldown(5, 30, commands.BucketType.user)
async def invite(message):
    await message.channel.send('Ссылка на приглашение: <https://discord.com/oauth2/authorize?client_id=809369105207132210&scope=bot&permissions=2683698256>')
    
@bot.command(pass_context = True)
@commands.cooldown(5, 30, commands.BucketType.user)
async def copy(message,*, txt=None):
    today = datetime.datetime.today()
    if txt==None:
        embed = discord.Embed(title= 'Команда: copy', 
        description= "**Описание:** Повторю сообщение которое вы написали, при этом удаляя егоs!\n**Кулдаун:** 5 сообщений за 30 секунд\n**Использование:** `s!сopy [ТЕКСТ]`\n**Пример использования: **`s!copy Приветs!`",
        color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
        await message.channel.send(embed = embed)
    else:
        await message.message.delete()
        await message.channel.send(txt)

@bot.command(pass_context = True)
@commands.cooldown(3, 30, commands.BucketType.user)
async def say(message, channel : discord.TextChannel, *args,):
    today = datetime.datetime.today()
    if not channel or not args:
        embed = discord.Embed(title= 'Команда: say', description= "**Описание:** Отправляет указанное вами сообщение в указанный вами канал\n**Кулдаун:** 3 сообщений за 30 секунд\n**Использование:** `s!say #канал [TEКСТ]`\n**Пример использования:** `s!say #канал-для-приветов Приветs!`", color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
        await message.channel.send(embed = embed)
    else:
        await message.message.delete()
        text = ' '
        for item in args:
            text = text + item + ' '
        await channel.send(text)

@bot.command(pass_context = True)
async def help(message):
    embed = discord.Embed(title= 'Cписок доступный команд:', description= '''
*Для получения детальной информации о команде введите:* `s!КОМАНДА`
`user` - Информация о пользователе
`server` - Информация о сервере
`role` - Информация о роли
`clear` - Чистильщик сообщений
`copy` - Отправка вашего сообщения в текущий канал
`say` - Отправка вашего сообщения в  указанный канал
`ball` - Магический шар предсказаний и судьбы
`roll` - Кубик :3
`gun` - Информация о доступе к системе стрельбы
''', color=0xeee657)
    today = datetime.datetime.today()
    embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
    await message.channel.send(embed=embed)

@bot.command(pass_context = True)
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
            embed.add_field(name='Результат игры:', value = 'Ножницы vs Камняs!\n Ты проигралs!')
        elif x == 2 and y == 3:
            embed.add_field(name='Результат игры:', value = 'Бумага vs Ножницs!\nТы проигралs!')
        elif x == 3 and y == 1:
            embed.add_field(name='Результат игры:', value = 'Камень vs Бумагиs!\nТы проигралs!')
    #won
        elif x == 2 and y == 1:
            embed.add_field(name='Результат игры:', value = 'Камень vs Ножницs!\nТы победилs!')
        elif x == 3 and y == 2:
            embed.add_field(name='Результат игры:', value = 'Ножницы vs Бумагиs!\nТы победилs!')
        elif x == 1 and y == 3:
            embed.add_field(name='Результат игры:', value = 'Бумага vs Камняs!\nТы победилs!')
    #draw
        elif x == 1 and y == 1:
            embed.add_field(name='Результат игры:', value = 'Камень vs Камняs!\nНичьяs!')
        elif x == 2 and y == 2:
            embed.add_field(name='Результат игры:', value = 'Ножницы vs Ножницs!\nНичьяs!')
        elif x == 3 and y == 3:
            embed.add_field(name='Результат игры:', value = 'Бумага vs Бумагиs!\nНичьяs!')
    else:
        embed.add_field(name = 'Команда: cnb',
        value = '**Описание:** Классическая игра "Камень, Ножницы, Бумагаs!"\n**Кулдаун:** 10 сообщений за 30 секунд\n**Использование:** `s!cnb (1-3)`\n**Пример использования:** `s!cnb 1`')
    await message.channel.send(embed = embed)

@bot.command(pass_context = True)
@commands.cooldown(6, 30, commands.BucketType.user)
async def ball(message,*, soob=None):
    spisok = [', абсолютно верно:8ball:', ', судя по моей информации, нет:8ball:', ', я не уверен, спросите еще раз:8ball:',
    ', в базе данных произошла ошибка, повторите вопрос:8ball:', ', скорее да, чем нет:8ball:',
    ', ну вообще да, но как бы нет:8ball:', ', в базе данных произошла ошибка, повторите вопрос:8ball:',
    ', в теории да, на практике еще не известно:8ball:', ', полностью уверен что нет:8ball:', ', у вас все в порядке?С такими вопросами вам в дурку:8ball:',
    ', черт возьмиs! Даs! Так оно и естьs!:8ball:']
    l = len(spisok)
    x = randint(0, l-1)
    if soob==None:
        embed = discord.Embed(title= 'Команда: ball', description= "**Описание:** Типичный шарлатанский шарик встряхивая который вы получаете ответ на свой вопрос.\nЗадавать вопрос нужно так, что бы я мог ответить: Да / Нет\n**Кулдаун:** 6 сообщений за 30 секунд\n**Использование:** `s!ball [TEКСТ]`\n**Пример использования:** `s!ball Я котик?`", color=0xeee657, inline = False)
        embed.set_author(name = message.author, icon_url = message.author.avatar_url)
        today = datetime.datetime.today()
        embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
        await message.channel.send(embed = embed)
    else:
        await message.channel.send('{}'.format(message.author.mention) + str(spisok[x]))

@bot.command(pass_context = True)
@commands.cooldown(4, 30, commands.BucketType.user)
async def roll(message, yy=None):
    embed = discord.Embed(color=0xeee657, inline = False)
    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
    today = datetime.datetime.today()
    embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
    if yy==None:
        embed.add_field(name = 'Команда: roll', 
        value = "**Описание:** Рандомайзер чисел в диапазоне от x до y или же выбирают случайную фразу из перечисленных вами\n**Кулдаун:** 4 сообщения за 30 секунд\n**Использование:** `s!roll [число] [число]`\n`s!roll [фраза] [фраза]`\n**Пример использования**: `s!roll 45`")
    else:
        rand = message.content.split()
        if int(rand[0])==rand[0]:
            x,y = int(rand[0]),int(rand[1])
            r=randint(x,y)
        else:
            r = random.choice(rand)
        embed.add_field(name = 'Результат:', value = ':game_die: {}'.format(r)+' :game_die:')
    await message.channel.send(embed = embed)

@bot.command(pass_context = True)
@commands.cooldown(1, 15, commands.BucketType.user)
async def gun(ctx, yy=None):
    message = ctx.message
    embed = discord.Embed(color=0xeee657, inline = False)
    embed.set_author(name = message.author, icon_url = message.author.avatar_url)
    today = datetime.datetime.today()
    embed.set_footer(text = 'BotSiniy© | {}'.format(today.strftime("%H:%M %d/%m/%Y")))
    embed.add_field(name = 'Команда: gun', 
    value = "**Описание:**\nДля использования оружия используйте команды `shot` и `granate`, для лечения используйте `heal` \nДоступно оружие только пользователям с ролями:\n `Военный`, `Гвардия`,`Легальное оружие`,`Нелегальное оружие`\n Доступно лечение только с ролями:\n`Аптечка`,`Врач` ")
    await message.channel.send(embed = embed)

@bot.command(pass_context = True)
@commands.cooldown(1, 30, commands.BucketType.user)
async def granate(ctx, member: discord.Member=None):
    is_do = False
    granata = discord.utils.get(ctx.author.guild.roles, id=863804890810941451)
    dead = discord.utils.get(ctx.author.guild.roles, id=863391384690098198)
    hard_blood = discord.utils.get(ctx.author.guild.roles, id=863391396303601724)
    easy_blood = discord.utils.get(ctx.author.guild.roles, id=863391413193801757)
    bron = ''
    armor = discord.utils.get(member.guild.roles, id=863784578883518484)
    if member == None:
        await ctx.message.channel.send('Граната не задела даже муравья.')
    else:
        for role in ctx.message.author.roles:
            if role==granata:
                mention = member.mention
                veroyatnost = randint(1,10)
                telo = ['левую ногу','левую руку','правую ногу','правую ногу','живот','плече','грудь']
                if veroyatnost<3:
                    res = 'В {} кинули гранату! Шанс был мал, но вышли целым.'.format(mention)
                elif veroyatnost>=3 and veroyatnost<=4: 
                    if armor in member.roles:
                        await member.remove_roles(armor)
                        res = 'В {} кинули гранату, к счатью он был достаточно далеко и бронежилет спас от осколков..'.format(mention)
                    else:
                        await member.add_roles(easy_blood)
                        res = 'В {} кинули гранату! Легкое ранение, как для гранаты, осколками задело {} '.format(mention,random.choice(telo))
                elif veroyatnost>4 and veroyatnost<=7:
                    await member.add_roles(hard_blood)
                    if armor in member.roles:
                        await member.remove_roles(armor)
                        bron = 'и бронежилет не спаc...'
                    res = 'В {} кинули гранату! Вы слышите бум! Граната нанесла удар в {}, вы ощущаете теплую кровь, или же, не ощущаете {}'.format(mention,random.choice(telo),bron)
                elif veroyatnost>7 and veroyatnost<=10:
                    await member.add_roles(dead)
                    if armor in member.roles:
                        bron = 'и бронежилет не спаc, даже от него одни кусочки...'
                        await member.remove_roles(armor)
                    res = 'В {} кинули гранату! Отличный шанс выучить анатомию, все части тела разлетелись в разные стороны {}'.format(mention,bron)
                await ctx.message.author.remove_roles(granata)
                await ctx.message.channel.send(res)
                is_do = True
                break
        if is_do==False:
            await ctx.message.channel.send('Тебе нечего кидать!')
    
@bot.command(pass_context = True)
@commands.cooldown(1, 15, commands.BucketType.user) 
async def shot(ctx, member: discord.Member=None):
    is_do=False
    armor = discord.utils.get(member.guild.roles, id=863784578883518484)
    dead = discord.utils.get(ctx.author.guild.roles, id=863391384690098198)
    hard_blood = discord.utils.get(ctx.author.guild.roles, id=863391396303601724)
    easy_blood = discord.utils.get(ctx.author.guild.roles, id=863391413193801757)
    role_gun = [860981372977938432,798256602775552050,861362945920466948,861363030449192980]
    if member == None:
        await ctx.message.channel.send('Выстрел в воздух,бедная птичка.')
    else:
        for role in ctx.message.author.roles:
            if role.id in role_gun:
                mention = member.mention
                veroyatnost = randint(1,10)
                telo = ['левую ногу','левую руку','правую ногу','правую ногу','живот','плече','грудь']
                if veroyatnost>6 and veroyatnost<=10:
                    res = 'В {} выстрелили! К счастью пуля не попала в цель.'.format(mention)
                elif armor in member.roles:
                    res = 'В {} стреляли! К счастью на нем был бронежилет, который больше непригоден...'.format(mention)
                    await member.remove_roles(armor)
                else:
                    if veroyatnost<3:
                        await member.add_roles(dead)
                        res = 'В {} выстрелили! Рана смертельная, поздравляю, вы умерли.'.format(mention)
                    elif veroyatnost>=3 and veroyatnost<=4 :
                        await member.add_roles(hard_blood)
                        res = 'В {} выстрелили! Ловкое попадание. Тяжелая рана. Выстрел в {}. Боль. '.format(mention,random.choice(telo))
                    elif veroyatnost>4 and veroyatnost <=6:
                        await member.add_roles(easy_blood)
                        res = 'В {} выстрелили! Чудом уклонившись он(а) получил(а) легкое рание в {}'.format(mention,random.choice(telo))
                await ctx.message.channel.send(res)
                is_do = True
                break
        if is_do==False:
            await ctx.message.channel.send('Тебе не из чего стрелять!')

@bot.command(pass_context = True)
@commands.cooldown(1, 60, commands.BucketType.user) 
async def heal(ctx, member: discord.Member=None):
    is_do=False
    dead = discord.utils.get(ctx.author.guild.roles, id=863391384690098198)
    hard_blood = discord.utils.get(ctx.author.guild.roles, id=863391396303601724)
    easy_blood = discord.utils.get(ctx.author.guild.roles, id=863391413193801757)
    medic = discord.utils.get(ctx.author.guild.roles, id=863419030253731900)
    aptechka = discord.utils.get(ctx.author.guild.roles, id=863419086721384468)
    if member == None:
        await ctx.message.channel.send('Воздух стал немного здоровее...')
    else:
        if medic in ctx.message.author.roles or aptechka in ctx.message.author.roles:
            mention = member.mention
            if easy_blood in member.roles:
                await member.remove_roles(easy_blood)
                res = '{} теперь здоров как бык!'.format(mention)
            if hard_blood in member.roles:
                await member.remove_roles(hard_blood)
                await member.add_roles(easy_blood)
                res = '{} теперь хотя бы похож на человека, ранение стало легким... '.format(mention)
            if dead in member.roles:
                res = '{} уже мертв..Бесполезно...'.format(mention)
            await ctx.message.channel.send(res)
            is_do = True
        
        if medic in ctx.message.author.roles:
            pass
        elif aptechka in ctx.message.author.roles:
            await ctx.message.author.remove_roles(aptechka)
            await ctx.message.channel.send('Аптечка использована....')
        if is_do==False:
            await ctx.message.channel.send('Ты не можешь это сделать...')

@bot.command(pass_context = True)
@commands.cooldown(1, 1, commands.BucketType.user) 
async def grole(ctx, member: discord.Member=None, role=None):
    admin = discord.utils.get(ctx.author.guild.roles, id=797499199628247040)
    if admin in ctx.message.author.roles:
            name = []
            for x in member.guild.roles:
                name.append(x.name)
            similary_perc = [dice_cofic(role,s) for s in name]
            most_sililar = similary_perc.index(max(similary_perc))
            await member.add_roles(member.guild.roles[most_sililar])
            await ctx.message.channel.send('Дело сделано...')
    else:
        ctx.message.channel.send('Ишь чего захотел! Прав у тебя нету, я запрещаю..')

def dice_cofic(a,b):
    a_bigrams = set(a)
    b_bigrams = set(b)
    overlap = len(a_bigrams & b_bigrams)
    return overlap * 2.0/(len(a_bigrams) + len(b_bigrams))
    
@bot.command(pass_context = True)
@commands.cooldown(1, 1, commands.BucketType.user) 
async def rrole(ctx, member: discord.Member=None, role = None):
    admin = discord.utils.get(ctx.author.guild.roles, id=797499199628247040)
    if admin in ctx.message.author.roles:
            name = []
            for x in member.guild.roles:
                name.append(x.name)
            similary_perc = [dice_cofic(role,s) for s in name]
            most_sililar = similary_perc.index(max(similary_perc))
            await member.remove_roles(member.guild.roles[most_sililar])
            await ctx.message.channel.send('Дело сделано...')
    else:
        ctx.message.channel.send('Ишь чего захотел! Прав у тебя нету, я запрещаю..')

@bot.command(pass_context = True)
@commands.cooldown(1, 1, commands.BucketType.user) 
async def par_instr(ctx):
    voen = discord.utils.get(ctx.author.guild.roles, id=860981372977938432)
    if voen in ctx.message.author.roles:
        await ctx.message.channel.send('Значит так бойцы! Я - ваш роботизированный инструктор по прыжкам с парашютом!')
        time.sleep(3)
        await ctx.message.channel.send('Я проведу вам короткий инструктаж! Первое - после конца инструктажа одеть парашют(`*одел парашют*`)')
        time.sleep(3)
        await ctx.message.channel.send('Второе - Стартуем по очереди.((`*прыгнул*`))')
        time.sleep(3)
        await ctx.message.channel.send('Третье - не забыть его открыть. Очень не советую забыть *звуки механического смеха*((`*открыл парашют*`)')
        time.sleep(3)
        await ctx.message.channel.send('((Не забываем отыгрывать рп))')
    else:
        await ctx.message.channel.send('Ты даже не военный!')

@bot.command(pass_context = True)
@commands.cooldown(1, 1, commands.BucketType.user) 
async def army(ctx):
    voen = discord.utils.get(ctx.author.guild.roles, id=860981372977938432)
    if voen in ctx.message.author.roles:
        await ctx.message.channel.send('Значит так бойцы! Я - ваш роботизированный помощник по упрощению жизни!')
        time.sleep(3)
        await ctx.message.channel.send('Я проведу вам короткий свод моих умений! Первое - я могу раздавать вам снаряжение для тренировок(`*одел тренировочное снаряжение*`)')
        time.sleep(3)
        await ctx.message.channel.send('Второе - Выступаю инструктором для прыжков с парашютом((`s!par_instr`))')
        time.sleep(3)
        await ctx.message.channel.send('((Забираю роли мертвого и ранений `*закончил тренировку*`')
        time.sleep(3)
        await ctx.message.channel.send('Загрузка обновлений... Данная строка на данный момент пуста.. На этом все.')
    else:
        await ctx.message.channel.send('Ты даже не военный!')

@bot.event
async def on_message(message):
    #Парашют блок
    if message.content.startswith('*одел') or message.content.startswith('*открыл') or message.content.startswith('*прыгнул') or message.content.startswith('*закончил'):
        if message.content.startswith("*одел парашют*") or message.content.startswith("*одела парашют*") :
            if discord.utils.get(message.author.guild.roles, id=860981372977938432) in message.author.roles:
                await message.author.add_roles(discord.utils.get(message.author.guild.roles, id=863784592212230204))
                await message.channel.send('{}, держи боец!'.format(message.author.mention))
            else:
                await message.channel.send('Я могу выдать парашют только военному!')
        if message.content.startswith("*прыгнул*") or message.content.startswith("*прыгнула"):
            if discord.utils.get(message.author.guild.roles, id=863784592212230204) in message.author.roles:
                await message.channel.send('*через микрофон в ухе*:\n {}, открывай парашют на высоте около 600 метров,сейчас мы примерно на высоте...ПИП- Провожу расчёт! {} метров!'.format(message.author.mention,randint(900,1100)))
                time.sleep(8)
                await message.channel.send('*через микрофон в ухе*:\n{}, - {} м.! '.format(message.author.mention,randint(700,800)))
                time.sleep(8)
                await message.channel.send('*через микрофон в ухе*:\n {}, {} м.! Открывай парашют!'.format(message.author.mention,randint(500,650)))
            else:
                await message.channel.send('Куда без парашюта? *механическая рука поймала прыгнувшего {}*'.format(message.author.mention))
        if message.content.startswith("*открыл парашют*") or message.content.startswith("*закончила тренировку*"):
            if discord.utils.get(message.author.guild.roles, id=863784592212230204) in message.author.roles:
                await message.author.remove_roles(discord.utils.get(message.author.guild.roles, id=863784592212230204))
                dead = randint(1,40)
                if dead == 1:
                    await message.channel.send('*через микрофон в ухе:*\n{}, ой ой ой! Парашют не открылся! Хорошо что у вас есть запасной, советую его открыть.').format(message.author.mention)
                else:
                    await message.channel.send('*через микрофон в ухе:*\n{}, осталось медленно спускаться....'.format(message.author.mention))
            else:
                await message.channel.send('Было бы что открывать...Парашюта то нет.')
        if message.content.startswith("*закончил тренировку*") or message.content.startswith("*одела тренировочное снаряжение*") :
            if discord.utils.get(message.author.guild.roles, id=860981372977938432) in message.author.roles:
                await message.author.remove_roles(discord.utils.get(message.author.guild.roles, id=863391384690098198))
                await message.author.remove_roles(discord.utils.get(message.author.guild.roles, id=863391396303601724))
                await message.author.remove_roles(discord.utils.get(message.author.guild.roles, id=863391413193801757))
            else:
                await message.channel.send('Ты не военный!')
        if message.content.startswith("*одел тренировочное снаряжение*") or message.content.startswith("*одела тренировочное снаряжение*") :
            if discord.utils.get(message.author.guild.roles, id=860981372977938432) in message.author.roles:
                await message.author.add_roles(discord.utils.get(message.author.guild.roles, id=863804890810941451))
                await message.author.add_roles(discord.utils.get(message.author.guild.roles, id=863784578883518484))
                await message.channel.send('{}, держи боец! Бронежилет, граната, автомат'.format(message.author.mention))
            else:
                await message.channel.send('Я могу выдать трен.снаряжение только военному!')
    #end block
    else:
        await bot.process_commands(message)

bot.run(TOKEN)


