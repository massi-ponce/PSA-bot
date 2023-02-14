import discord
from tokens import token_bot
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print("Bot encendido")

def MyEmbed(name, icon, iterator, base, lower, higher):
    embed = discord.Embed(title = f"Starting sensivity: {base}",description = f"Iteration {iterator}",colour = discord.Color.random())
    embed.set_author(name = "PSA method", icon_url = "https://cdn.iconscout.com/icon/free/png-256/computer-mouse-1500503-1271148.png")
    embed.set_thumbnail(url = icon)
    embed.add_field(name = "Lower", value = lower)
    embed.add_field(name = "Base", value = base, inline = True)
    embed.add_field(name = "Higher", value = higher, inline = True)
    embed.set_footer(text = f"for {name}")
    return embed

@client.command()
async def sens(ctx, base: float, member: discord.Member = None):
    member = ctx.author
    name = member.display_name
    icon = member.display_avatar

    porc_low = 0.5
    porc_high = 1.5
    iterator = 1
    
    lower = round(base * porc_low, 2)
    higher = round(base * porc_high, 2)

    embed = MyEmbed(name, icon, iterator, base, lower, higher)

    await ctx.send(embed=embed)

client.run(token_bot)