import discord
from discord.ext import commands
bot = commands.Bot(command_prefix= 'Паштет ' )
import typing
import random
ask1 = ["Да", "Нет", "Безусловно", "Конечно нет"]
pashtet = ["Паштет мурлыкает", "Паштет отгрыз вам руку"]
pashtet1 = ["чо тибе нада?", "шо", "ацтань шалапай" , "мяу нахуй" , "шо блять?" , "ало"]
bot.remove_command('help')

privet = ["Сильвупле", "Хай" , "Привет"]
poka = ["Пока" , "Аривидерчи" , "ачё)" , "bb"]

@bot.command()
async def help(ctx):
	emb = discord.Embed(title= "Информация о коммандах", colour= 0x39d0d6)
	emb.add_field(name= 'help' , value= 'Показывает это сообщение')
	emb.add_field(name= 'add' , value= 'Калькулятор')
	emb.add_field(name= 'ask "вопрос"' , value= 'Задать вопрос')
	emb.add_field(name= 'ban' , value= 'Бан')
	emb.add_field(name= 'mute' , value= 'Мут')
	emb.add_field(name= 'clear "число"' , value = 'Чистка сообщений')
	emb.add_field(name= 'snowball "человек"' , value = 'Кинуть снежок')
	await ctx.send(embed= emb)

@bot.command()
async def погладить(ctx):
	await ctx.send(random.choice(pashtet))

@bot.command()
async def snowball(ctx, user: discord.User):
	await ctx.send("Вы кинули снежок в ебало " +str(user.mention) )	
	await ctx.message.delete()

@bot.command()
async def привет(ctx):	
	await ctx.send(random.choice(privet))

@bot.command()
async def как_дела(ctx):
	await ctx.send("Норм чи шо")

@bot.command()
async def а_что_такое_порнография(ctx):
	await ctx.send("Я обнаружил не разрешённое моей программой слово. Не могу отвечать.")

@bot.command()
async def ау(ctx):
	await ctx.send(random.choice(pashtet1))

@bot.event
async def on_ready():
	print ("Logged")

@bot.command()
async def ты(ctx, arg: str):
	author = ctx.message.author
	await ctx.send(f"{author.mention} сам ты "+ str(arg))

@bot.command()
async def add(ctx, a: int,b: int):
	await ctx.send(a + b)

@bot.command()
async def ask(ctx):
	await ctx.send(random.choice(ask1))

@bot.command()
async def пока(ctx):
	await ctx.send(random.choice(poka))

#moderation commands

@bot.command()
@commands.has_permissions(administrator= True)
async def ban(ctx, members:discord.Member = None , reason = None):
	if members is None:
		await ctx.send("Укажите пользователя")
	else:
		if reason is None:
			await ctx.send (f'{ctx.message.author} Забанил пользователя {members}')
			try:
				await members.send(f'Вас забанили на сервере {ctx.guild.name}')
			finally:
				await ctx.message.delete()
				await ctx.guild.ban(members)
		elif reason is not None:
			await ctx.send (f'{ctx.message.author} Забанил пользователя {members}, по причине {reason}')
			try:
				await members.send(f'Вас забанили на сервере {ctx.guild.name} по причине {reason}')
			finally:
				await ctx.message.delete()
				await ctx.guild.ban(members, reason=reason)
				
@bot.command()
@commands.has_permissions(manage_roles= True)
async def mute(ctx, member: discord.Member = None, reason = None):
	mute_role = discord.utils.get(ctx.message.guild.roles, name = "Muted")
	
	if member is None:
		await ctx.send('Укажите пользователя')
	else:
		if reason is None:
			await ctx.message.delete()
			await ctx.send (f"{ctx.message.author} замутил {member}")
			await member.add_role(mute_role)
		elif reason is not None:
			await ctx.message.delete()
			await ctx.send (f"{ctx.message.author} замутил {member} по причине {reason}")
			await member.add_role(mute_role)

@bot.command()
@commands.has_permissions(manage_messages= True)
async def clear(ctx, amount= 5):
	await ctx.channel.purge(limit=amount)
	print ("Cleared "  +str(amount))

bot.run("NjYwODM1MjQ0MzkxMjY4Mzgy.XkyXsg.gOn0Ew7HOpodLWlgYgalBKNCtvA")

    	
 

	



