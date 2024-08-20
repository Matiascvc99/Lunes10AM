
import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  channel = client.get_channel(1275150789106471045)
  await channel.send("Lunes")


client.run("")

exit()