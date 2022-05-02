# importing all the libraries
import discord
import os
import cal as ca
import dictionary
import weather_plugin
import crypto_plugin as crypto

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
		tmp = ca.SendTime()
		await message.channel.send(tmp)
		print('Current time:', tmp)

	if message.content.startswith('!date'):
		tmp = ca.SendDate()
		await message.channel.send(tmp)
		print('Current date:', tmp)

	if message.content.startswith('!word'):
		tmp = dictionary.Word()
		await message.channel.send(tmp)
		print('Sent word:', tmp)

	if message.content.startswith('!sentence'):
		tmp = dictionary.Sentence()
		await message.channel.send(tmp)
		print('Sent sentence:', tmp)

	if message.content.startswith('!longsentence'):
		tmp = dictionary.LongSentence()
		await message.channel.send(tmp)
		print('Sent long sentence:', tmp)

	if message.content.startswith('!weather'):
		tmp = weather_plugin.SendMessage()
		await message.channel.send(tmp)
		print('Sent weather:', tmp)

	if message.content.startswith('$help'):
		file = open('command-texts/crypto-help.txt', 'r')
		msg = file.read()
		print(msg)
		await message.channel.send(msg)
		file.close()
		print('Crypto help command succesfully executed')

	if message.content.startswith('$btc'):
		tmp = crypto.sendbtc()
		await message.channel.send(tmp)
		print('Sent digital assets(btc):', tmp)

	if message.content.startswith('$eth'):
		tmp = crypto.sendeth()
		await message.channel.send(tmp)
		print('Sent digital assets(eth):', tmp)

	if message.content.startswith('$xmr'):
		tmp = crypto.sendxmr()
		await message.channel.send(tmp)
		print('Sent digital assets(xmr/monero):', tmp)

	if message.content.startswith('$doge'):
		tmp = crypto.senddoge()
		await message.channel.send(tmp)
		print('Sent digital assets(doge):', tmp)

# save the discord api key in the env variables as DKEY
client.run(os.getenv('DKEY'))
