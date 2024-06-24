import discord

# La variable intents almacena los privilegios del bot
intents = discord.Intents.default()
# Activar el privilegio de lectura de mensajes
intents.message_content = True
# Crear un bot en la variable cliente y transferirle los privilegios
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$hello'):
        await message.channel.send("https://img.wattpad.com/d18115e0ac209c95b1aed84440afec3f97d54038/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f776174747061642d6d656469612d736572766963652f53746f7279496d6167652f7a515a6454444c32373135766e773d3d2d3430363039313737312e313462613537643165623161383334343636393133393539383130342e6a7067?s=fit&w=720&h=720")
    else:
        await message.channel.send(message.content)

client.run("TU TOKEN DE BOT")
