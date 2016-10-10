import os
import discord
from discord.ext import commands

#TODO 
#Bot will be run with a redirect url argument, optional arguments as to which rules.ini presets it should be added to
#It will download the url into pak folder, replacing current pak if necessary
#It will find information about the newest pak using listmaps.sh script
#It will use that information to create a new line in Game.ini with required information if one does not exist already, or update current one
#It will then continuously(at a low performance impact rate, sleep in between) poll processes until the only instance remaining is lobby, at which point it will restart the server
#If rules preset arguments given, will add the map to relevent rules.ini presets
#It will then inform other hubs to update this pak also, perhaps just by giving them the same update command with url argument and same rules.ini arguments to just run the script again on those hubs
#  This could be done via sending a text base message from one hub to the other

bot = commands.Bot(command_prefix='!', description='If you don\'t know what this does, then why are you here?')

class common:
    def __init__(self):
        self.accepted_roles = ['tester', 'admin']
        self.server_channel = None

COMMON = common()

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command(pass_context=True)
async def enable(ctx):
    roles = [a.name.lower() for a in ctx.message.author.roles]
    if set(roles).intersection(COMMON.accepted_roles):
        COMMON.server_channel = ctx.message.channel
        await bot.say(COMMON.server_channel.name+' is the new server administration channel')
    else:
        await bot.say('You do not have permission to use that command')

@bot.command(pass_context=True)
async def addmap(ctx, url):
    print(COMMON.server_channel)
    if not COMMON.server_channel or ctx.message.channel.id != COMMON.server_channel.id:
        print('wrong channel')
        return
    if not url.startswith('http') or url[-4:] != '.pak':
        bot.say('That is an invalid url')
        return
    os.system('wget '+url)
    await bot.say('Retreiving '+url)
    ini_update()

def ini_update(pak):
    pass

bot.run('MjM1MTE1OTM2MzcyMjI4MDk2.Ct14Vw.I4PpK1ftpv-otpDUcV-ex0bhrok')
