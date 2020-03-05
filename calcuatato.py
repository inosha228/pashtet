import discord
from discord.ext import commands
bot = commands.Bot(command_prefix= 'Паштет ' )
import typing
import random
import os
bot.remove_command('help')

@bot.event
async def on_ready():
	print ("Logged")
	await bot.change_presence(activity=discord.Game(name="фантик"))

@bot.command()
async def help(ctx):
	emb = discord.Embed(title= "Информация о коммандах", description= "Префикс - Паштет (советовательно все команды писать в "")", colour= 0x39d0d6)
	emb.add_field(name= 'help' , value= 'Показывает это сообщение')
	emb.add_field(name= 'add' , value= 'Калькулятор')
	emb.add_field(name= 'ask "вопрос"' , value= 'Задать вопрос')
	emb.add_field(name= 'ban' , value= 'Бан')
	emb.add_field(name= 'mute' , value= 'Мут')
	emb.add_field(name= 'clear "число"' , value = 'Чистка сообщений')
	emb.add_field(name= 'snowball "человек"' , value = 'Кинуть снежок')
	emb.add_field(name= 'coinflip' , value= 'Орёл или Решка')
	await ctx.send(embed= emb)

@bot.command()
async def coinflip(ctx):
	coinflip = ["Орёл" , "Решка"]
	await ctx.send(random.choice(coinflip))

@bot.command()
async def погладить(ctx):
	pashtet = ["Паштет мурлыкает", "Паштет отгрыз вам руку"]
	await ctx.send(random.choice(pashtet))

@bot.command()
async def snowball(ctx, user: discord.User):
	await ctx.send("Вы кинули снежок в ебало " +str(user.mention) )
	await ctx.message.delete()

@bot.command()
async def привет(ctx):
	privet = ["Хай" , "Привет" , "Здрасте"]
	await ctx.send(random.choice(privet))

@bot.command()
async def как_дела(ctx):
	await ctx.send("Норм чи шо")

@bot.command()
async def а_что_такое_порнография(ctx):
	await ctx.send("Я обнаружил не разрешённое моей программой слово. Не могу отвечать.")

@bot.command()
async def ау(ctx):
	pashtet1 = ["чо тибе нада?", "шо", "ацтань шалапай" , "мяу нахуй" , "шо блять?" , "ало"]
	await ctx.send(random.choice(pashtet1))

@bot.command()
async def ты(ctx, arg):
	author = ctx.message.author
	await ctx.send(f"{author.mention} сам ты " + arg)

@bot.command()
async def add(ctx, a: int, ch ,b: int):
	if ch == '+':
		await ctx.send(a + b)
	elif ch == '-':
		await ctx.send(a - b)
	elif ch == '*':
		await ctx.send(a * b)
	elif ch == '/':
		await ctx.send (a / b)
	else:
		await ctx.send('Ты вёл ниверные даные')

@bot.command()
async def ask(ctx):
	ask1 = ["Да", "Нет", "Безусловно", "Конечно нет"]
	await ctx.send(random.choice(ask1))

@bot.command()
async def пока(ctx):
	poka = ["Пока" , "Аривидерчи" , "ачё)" , "bb"]
	await ctx.send(random.choice(poka))

#moderation commands

@bot.command()
@commands.has_permissions(manage_roles= True)
async def ban(ctx, members:discord.Member = None , reason = None):
	logs = bot.get_channel(656186967460937728)
	if members is None:
		await ctx.send("Укажите пользователя" , delete_after = 10 )
	else:
		if reason is None:
			emb = discord.Embed(title = "Бан", description = f'{ctx.message.author} забанил {members}', colour = 0x39d0d6)
			try:
				await members.send(f'Вас забанили на сервере {ctx.guild.name}')
			finally:
				await ctx.guild.ban(members)
				await logs.send(embed = emb)
				await ctx.send(embed = emb)
		elif reason is not None:
			emb = discord.Embed(title = "Бан", description = f'{ctx.message.author} забанил {members}, по причине {reason}')

			try:
				await members.send(f'Вас забанили на сервере {ctx.guild.name} по причине {reason}', colour = 0x39d0d6)
			finally:
				await ctx.guild.ban(members, reason=reason)
				await logs.send(embed = emb)
				await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions(manage_roles= True)
async def mute(ctx, member: discord.Member = None, reason = None):
	logs = bot.get_channel(656186967460937728)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = "Muted")
	await ctx.message.delete()

	if member is None:
		await ctx.send('Укажите пользователя', delete_after = 10)
	else:
		if reason is None:
			emb = discord.Embed(title = 'Мут', description = f'{ctx.message.author} замутил {member}' , colour = 0x39d0d6)
			await logs.send(embed = emb)
			await member.add_roles(mute_role)
			await ctx.send(embed = emb)
		elif reason is not None:
			emb = discord.Embed(title = 'Мут', description = f'{ctx.message.author} замутил {member} по причине {reason}' , colour = 0x39d0d6)
			await logs.send(embed = emb)
			await member.add_roles(mute_role)
			await ctx.send(embed = emb)

@bot.command()
@commands.has_permissions(manage_roles= True)
async def unmute(ctx, member: discord.Member = None,):
	logs = bot.get_channel(656186967460937728)
	mute_role = discord.utils.get(ctx.message.guild.roles, name = "Muted")
	await ctx.message.delete()

	if member is None:
		await ctx.send('Укажите пользователя' , delete_after = 10)
	else:
			emb = discord.Embed(title = 'Мут', description = f'{ctx.message.author} размутил {member}' , colour = 0x39d0d6)
			await logs.send(embed = emb)
			await ctx.send(embed = emb)
			await member.remove_roles(mute_role)

@bot.command()
@commands.has_permissions(manage_messages= True)
async def clear(ctx, amount= 5):
	await ctx.channel.purge(limit=amount)
	await ctx.send(f'Отчисено {amount}')


token = os.environ.get('run')

    	
 

	



