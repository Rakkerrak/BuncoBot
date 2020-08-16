import os
import random

import discord

import settings
import token.py

token = settings.token

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!\n')


@client.event
async def on_message(message):

    #all channel ids stored in settings folder
    httext = settings.httext
    htvc = settings.htvc
    mttext = settings.mttext
    mtvc = settings.mtvc
    lttext = settings.lttext
    ltvc = settings.ltvc
    generalc = settings.generalc
    crownc = settings.crownc

    # bot does not self-reply
    if message.author == client.user:
        return

    # gneral ping.
    elif 'ping' == message.content.lower():
        await message.channel.send('pong!')


    # handles rolling. outputs a list of int. formats in message
    elif 'roll' == message.content.lower():

        def roll(int):
            list = []
            x = 1
            while x <= int:
                num = random.randint(1,6)
                x += 1
                list.append(num)
            return list

        result = roll(3)
        await message.channel.send("{} rolled:  ".format(message.author.mention) + "!   ".join(str(x) for x in result) + "!")


    # send a message to all text chats in channels that head table has made it to 21. can only be activated from head table and general text
    elif 'ring' == message.content.lower():
        if message.channel.id == httext or message.channel.id == generalc:
            channels = [httext, mttext, lttext]
            await message.channel.send("Ringing the bell!")
            for i in channels:
                current = client.get_channel(i)
                await current.send('Ring! Ring! Ring!  The head table got 21!')


    #member voice chat automoving by request of the member.
    elif 'up' == message.content.lower():
        try:
            if message.channel.id == mttext:
                await message.author.edit(voice_channel = client.get_channel(htvc))
                await client.get_channel(httext).send('{} you have been moved over here!'.format(message.author.mention))
            elif message.channel.id == lttext:
                await message.author.edit(voice_channel = client.get_channel(mtvc))
                await client.get_channel(mttext).send("{} you have been moved over here!".format(message.author.mention))
            else:
                await message.channel.send("{} you can't be moved from here!  This command only works in <#{}> and <#{}>. ".format(message.author.mention, mttext, lttext))
        except:
            await message.channel.send("{}Please enter a Voice- channel first!".format(message.author.mention))

    elif 'down' == message.content.lower():
        try:
            if message.channel.id == httext:
                await message.author.edit(voice_channel = client.get_channel(mtvc))
                await client.get_channel(mttext).send('{} you have been moved over here!'.format(message.author.mention))
            elif message.channel.id == mttext:
                await message.author.edit(voice_channel = client.get_channel(ltvc))
                await client.get_channel(lttext).send('{} you have been moved over here!'.format(message.author.mention))
            else:
                await message.channel.send("{} you can't be moved from here!  This command only works in <#{}> and <#{}>. ".format(message.author.mention, httext, mttext))
        except:
            await message.channel.send("{}Please enter a Voice- channel first!".format(message.author.mention))


    #posts a message in the crown channel to keep track of who has the crown. also shoots a crown gif to the user
    elif 'bunco' == message.content.lower() or 'bunco!' == message.content.lower():
        await client.get_channel(crownc).send('{} has the crown!'.format(message.author.mention))
        await message.channel.send("Crowning {}!".format(message.author))
        await message.channel.send(file=discord.File('source.gif'))


    elif 'help' == message.content.lower():
        await message.channel.send(embed = settings.embed)








client.run(token)
