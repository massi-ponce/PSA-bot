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

@client.command()
async def sens(ctx, base: float, member: discord.Member = None):
    member = ctx.author
    name = member.display_name
    icon = member.display_avatar

    embed = discord.Embed(title = f"Starting sensivity: {base}",description = "Iteration 1",colour = discord.Color.random())
    embed.set_author(name = "PSA method", icon_url = "https://cdn.iconscout.com/icon/free/png-256/computer-mouse-1500503-1271148.png")
    embed.set_thumbnail(url = icon)
    embed.add_field(name = "Lower", value = "0.75")
    embed.add_field(name = "Base", value = base, inline = True)
    embed.add_field(name = "Higher", value = "2.25", inline = True)
    embed.set_footer(text = f"for {name}")

    await ctx.send(embed=embed)

client.run(token_bot)