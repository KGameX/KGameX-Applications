import discord
from discord import app_commands
from time import *

bot = discord.Client(intents=discord.Intents.all())
commands = app_commands.CommandTree(bot)
version = '1.0.0'
birth = asctime(gmtime(1730884678))
color = 0x8000ff
creator = '@kgamex_vk'
contributors = []

@bot.event
async def on_ready():
    print(f'\n{bot.user} is connected to the following servers :')
    for server in bot.guilds:
        print(f'- {server.name} (id: {server.id})')
    print(f'Total : {len(bot.guilds)}\n\nSyncing slash commands ... ', end = '')
    await commands.sync()
    print('Ready !')

def write_on_logfile(log):
    logfile = open("../logfile.txt", "a")
    logfile.write(log)
    logfile.close()

# Info
@commands.command(name = 'info', description = 'Shows info about the bot.')
async def info(interaction:discord.Interaction):
    write_on_logfile(f'{bot.user} on {asctime()}, server : {interaction.guild} ({interaction.guild_id}), user : {interaction.user}, command : info\n')

    embedded = discord.Embed(title = f'{bot.user} Info', color = color)
    embedded.add_field(name = 'Born on', value = f'```{birth}```', inline = False)
    embedded.add_field(name = 'Number of guilds', value = f'```{len(bot.guilds)}```', inline = False)
    embedded.add_field(name = 'Version', value = f'```{version}```', inline = False)
    embedded.add_field(name = 'Created by', value = f'```{creator}```', inline = False)

    if len(contributors) > 0:
        str_contributors = '```'
        for contributor in contributors[:len(contributors) - 1]:
            str_contributors += contributor + ', '
        str_contributors += contributors[len(contributors) - 1] + '```'
        embedded.add_field(name = 'Contributors', value = str_contributors, inline = False)

    await interaction.response.send_message(embed = embedded)

# Ping
@commands.command(name = 'ping', description = 'Get the ping of the bot.')
async def ping(interaction:discord.Interaction):
    write_on_logfile(f'{bot.user} on {asctime()}, server : {interaction.guild} ({interaction.guild_id}), user : {interaction.user}, command : ping\n')

    await interaction.response.send_message(f'Pong ! In {round(bot.latency * 1000)}ms')

# Avatar
@commands.command(name = 'avatar', description = 'Shows the avatar of a user in this server.')
async def avatar(interaction:discord.Interaction, member:discord.Member):
    write_on_logfile(f'{bot.user} on {asctime()}, server : {interaction.guild} ({interaction.guild_id}), user : {interaction.user}, command : avatar, args : [member : {member}]\n')
    
    await interaction.response.send_message(member.display_avatar)

with open("token.txt", "r") as token:
    bot.run(token.read())