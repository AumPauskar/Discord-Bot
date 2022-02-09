# importing all the libraries
import discord
import os
import calendar as ca

client = discord.Client()

# spits out a message in the terminal when the bot is ready
@client.event
async def on_ready():
	print('We have loged in as {0.user}'.format(client))


# the chatbot part
@client.event
async def on_message(message):
	# disables the possiblity that the bot will reply to itself
	if message.author == client.user:
		return

	if message.content.startswith('!hello'):
		await message.channel.send('Hello World!')
		print('Message sent | Hello World')

	if message.content.startswith('!help'):
		file = open('command-texts/help.txt', 'r')
		msg = file.read()
		print(msg)
		await message.channel.send(msg)
		file.close()
		print('Help command succesfully executed')

	if message.content.startswith('!facts'):
		file = open('command-texts/facts.txt', 'r')
		msg = file.read()
		await message.channel.send(msg)
		file.close()
		print('Amazing fact shared')

	if message.content.startswith('!invite'):
		await message.channel.send('https://discord.gg/yhjbXcd4')
		print('Invite link sent successfully')

	if message.content.startswith('!admin'):
		file = open('command-texts/admin.txt', 'r')
		msg = file.read()
		await message.channel.send(msg)
		file.close()
		print('Admin link sent successfully')

	if message.content.startswith('!time'):
		await message.channel.send(ca.SendTime)
		print('Current time:', ca.SendTime)

	if message.content.startswith('!date'):
		await message.channel.send(ca.SendDate)
		print('Current date:', ca.SendDate)

# save the discord api key in the env variables as DKEY
client.run(os.getenv('DKEY'))
