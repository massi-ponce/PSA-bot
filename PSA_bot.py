import discord
from tokens import token_bot
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print("Bot encendido")

@client.command()
async def sens(ctx):
    base = float(input("Starting sensivity: "))
    porc_low = 0.5
    porc_high = 1.5
    iterator = 0
    while(iterator < 5):
        lower = round(base * porc_low,2)
        higher = round(base * porc_high,2)
        print("\nLower Base Higher\n"+str(lower)+" "+str(base)+" "+str(higher))
        resp = int(input("\n1) Lower\n2) Higher\n"))
        if(resp == 1):
            base = round((base + lower)/2,2)
        if(resp == 2):
            base = round((base + higher)/2,2)
        porc_low += 0.1
        porc_high -= 0.1
        iterator +=1
    porc_low = round(porc_low)-0.05
    porc_high = round(porc_high)+0.05
    lower = round(base * porc_low,2)
    higher = round(base * porc_high,2)
    print("\nLower Base Higher\n"+str(lower)+" "+str(base)+" "+str(higher))
    resp = int(input("\n1) Lower\n2) Higher\n"))
    if(resp == 1):
        base = round((base + lower)/2,2)
        print("Perfect Sensitivity: "+str(base))
    if(resp == 2):
        base = round((base + higher)/2,2)
        print("Perfect Sensitivity: "+str(base))

client.run(token_bot)