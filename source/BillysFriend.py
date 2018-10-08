#!/usr/bin/python3

from discord.ext.commands import Bot
from utils import WikiSearch
from utils import FunCalc

PREFIX = (":","/")
TOKEN = ' '

WIKI_LANG = "en"

TLDR ={'lc':"Lists commands.",
        'wi':'Returns Wikipedia description of a subject. (Please use " " for more-than-one-word-long names) '}

with open("../../keys/KeyFile.key", 'r') as f:
    TOKEN = f.read().strip()

#Basic funntions segment
#************************************************

client = Bot(command_prefix=PREFIX)

@client.command(name='areuthere?')
async def areUThere():

    await client.say("Yep, here I am!")


@client.command(name='list_commands',
                description=TLDR['lc'],
                aliases=['lc'])
async def commandHelp():
    msg = 'COMMANDS \n'
    for i in TLDR:
        msg += "\n[{0}]: \n{1}\n".format(i, TLDR[i]) 
    await client.say("```\n"+msg+"\n```")

#Wikipedia API segment
#************************************************

wiki_client = WikiSearch.WikiSearch(1, WIKI_LANG)

@client.command(name='whatis',
                description=TLDR['wi'],
                aliases=['wi'])
async def whatIs(index):
    await client.say(wiki_client.getContent(index))

@client.command(name="wikilang",
                description="Set languaje for the whatis command",
                aliases=['wl'])
async def wikiLang(lang):
    await client.say(wiki_client.changeLang(lang))

#Calculations segment
#************************************************

calc_client = FunCalc.FunCalc()

@client.command(name="calfun",
                description="Calculates mathematic functions from string inputs. (still under development)",
                aliases=['cf'])
async def calFunction(fx):
    await client.say(calc_client.calcFunc(fx))

client.run(TOKEN)
