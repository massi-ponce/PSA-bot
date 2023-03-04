import discord
from tokens import token_bot
from discord.ui import Button, View
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print("Bot encendido")

def InitialEmbed(name, icon, iterator, base, lower, higher):
    embed = discord.Embed(title = f"Starting sensivity: {base}",description = f"Iteration {iterator}",colour = discord.Color.random())
    embed.set_author(name = "PSA method", icon_url = "https://cdn.iconscout.com/icon/free/png-256/computer-mouse-1500503-1271148.png")
    embed.set_thumbnail(url = icon)
    embed.add_field(name = "Lower", value = lower)
    embed.add_field(name = "Base", value = base, inline = True)
    embed.add_field(name = "Higher", value = higher, inline = True)
    embed.set_footer(text = f"for {name}")
    return embed

def FinalEmbed(name, icon, base):
    embed = discord.Embed(title = f"Your perfect sensivity: {base}", colour = discord.Color.random())
    embed.set_author(name = "PSA method", icon_url = "https://cdn.iconscout.com/icon/free/png-256/computer-mouse-1500503-1271148.png")
    embed.set_thumbnail(url = icon)
    embed.set_footer(text = f"for {name}")
    return embed

@client.command()
async def sens(ctx, base: float, member: discord.Member = None):
    view = View()
    member = ctx.author
    name = member.display_name
    icon = member.display_avatar

    async def lower_callback(interaction):
        nonlocal message, name, icon, iterator, base, lower, higher, porc_low, porc_high
        iterator += 1
        if(iterator < 6):
            porc_low += 0.1
            porc_high -= 0.1
            base = round((base + lower)/2, 2)
            lower = round(base * porc_low, 2)
            higher = round(base * porc_high, 2)
            await message.edit(embed=InitialEmbed(name, icon, iterator, base, lower, higher))
            lower_button.callback = lower_callback
            higher_button.callback = higher_callback
        if(iterator == 6):
            porc_low = round(porc_low)-0.05
            porc_high = round(porc_high)+0.05
            base = round((base + lower)/2, 2)
            lower = round(base * porc_low, 2)
            higher = round(base * porc_high, 2)
            await message.edit(embed=InitialEmbed(name, icon, iterator, base, lower, higher))
            lower_button.callback = lower_callback
            higher_button.callback = higher_callback
        if(iterator == 7):
            base = round((base + lower)/2, 2)
            await message.edit(embed=FinalEmbed(name, icon, base))

    async def higher_callback(interaction):
        nonlocal message, name, icon, iterator, base, lower, higher, porc_low, porc_high
        iterator += 1
        if(iterator < 6):
            porc_low += 0.1
            porc_high -= 0.1
            base = round((base + higher)/2, 2)
            lower = round(base * porc_low, 2)
            higher = round(base * porc_high, 2)
            await message.edit(embed=InitialEmbed(name, icon, iterator, base, lower, higher))
            lower_button.callback = lower_callback
            higher_button.callback = higher_callback
        if(iterator == 6):
            porc_low = round(porc_low)-0.05
            porc_high = round(porc_high)+0.05
            base = round((base + higher)/2, 2)
            lower = round(base * porc_low, 2)
            higher = round(base * porc_high, 2)
            await message.edit(embed=InitialEmbed(name, icon, iterator, base, lower, higher))
            lower_button.callback = lower_callback
            higher_button.callback = higher_callback
        if(iterator == 7):
            base = round((base + higher)/2, 2)
            await message.edit(embed=FinalEmbed(name, icon, base))

    porc_low = 0.5
    porc_high = 1.5
    iterator = 1
    lower = round(base * porc_low, 2)
    higher = round(base * porc_high, 2)

    lower_button = Button(label = "Lower", style = discord.ButtonStyle.secondary)
    higher_button = Button(label = "Higher", style = discord.ButtonStyle.secondary)
    view.add_item(lower_button)
    view.add_item(higher_button)
    
    lower_button.callback = lower_callback
    higher_button.callback = higher_callback

    message = await ctx.send(embed=InitialEmbed(name, icon, iterator, base, lower, higher), view=view)

client.run(token_bot)