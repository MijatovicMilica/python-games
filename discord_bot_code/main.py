import discord

token = "DISCORD_API_KEY"

intents = discord.Intents.default()
intents.message_content=True
client = discord.Client(intents=intents)

@client.event #dekorator za funckije, njime menjamo ponasanje funkcije
async def on_ready():
    print(f"Logged in as{client.user}") #kada ga pokrenemo loguje nam se bot

@client.event
async  def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!poll"):
        question = message.content[len("!poll "):].strip()
        if question:
            poll_message = await message.channel.send(f"Poll: {question}")
            await  poll_message.add_reaction('👍')
            await  poll_message.add_reaction('👎')
        else:
            await message.channel.send("Nisi napisao pitanje")
    if "LOL" in message.content:
        await message.channel.send("Ne smes reci LOL")
        await message.author.kick(reason="Rekao je LOL")

    if message.content == "ping":
        await message.channel.send("pong")

client.run(token)

print ("test")