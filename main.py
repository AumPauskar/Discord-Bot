# importing all the libraries
import discord
import os

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

client.run(os.getenv('DKEY'))