import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='ub!')
with open("token.data") as tokenf:
token = tokenf.readline()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

 @client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Im feeling bad today":
        await client.send_message(message.channel, "Dont worry cheer up! :rainbow:") 
        
 @client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "Hello":
        await client.send_message(message.channel, "Hi welcome back! :rainbow:")
        
  @client.event
async def on_ready():
    print("IM Here!")
    await client.change_presence(game=discord.Game(name="$=ub!help for commands| bot by techtimefor| Im chilling"))
   
@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(V1+V2)

@bot.command()
async def multiply(ctx, a: int, b: int):
    await ctx.send(V1*V2)

@bot.command()
async def greet(ctx):
    await ctx.send(":smiley: :wave: Hello I'm Usefull Bot techtimefor made me, :joy:!")

@bot.command()
async def gif(ctx):
    await ctx.send("https://raw.githubusercontent.com/techtimefor/Usefulbot/master/niceload.gif?token=AMH7J6BKHQPWFIE42QFEVC2467ABY")

@bot.command()
async def info(ctx):
    embed = discord.Embed(title="nice bot", description="Nicest bot there is ever.", color=0xeee657)

    # give info about you here
    embed.add_field(name="Maker", value="<techtimefor:android: v-1.0 beta>")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="How much people use me", value=f"{len(bot.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite me to your server", value="[Invite link](<https://discordapp.com/api/oauth2/authorize?client_id=585810180072275976&permissions=8&scope=bot>)")

    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Useful Bot", description="I do a lot techtimefor made me :joy: :", color=0xeee657)

    embed.add_field(name="ub!add X Y", value="Gives the addition of **V1** and **V2**, inline=False)
    embed.add_field(name="ub!multiply X Y", value="Gives the multiplication of **V1** and **V"**", inline=False)
    embed.add_field(name="ub!greet", value="Gives a nice greet message", inline=False)
    embed.add_field(name="ub!gif", value="Get a good gif.", inline=False)
    embed.add_field(name="ub!info", value="Gives a little info about the bot", inline=False)
    embed.add_field(name="ub!help", value="Gives this message", inline=False)

    await ctx.send(embed=embed)

