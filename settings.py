import os
import discord




#These do control start.py values
httext = 742017448814968883
htvc = 741993729681784843
mttext = 742017324168511490
mtvc = 741991346579177536
lttext = 742008565190885420
ltvc = 741993924570382357
generalc = 741991346579177535
crownc = 742358807379968081

embed = discord.Embed(
title ='Help',
color = (0xffe6fe),
description = "\n"
)

embed.add_field(
name = "Rolling",
value = "```roll```",
inline = True
)
embed.add_field(
name = 'Keeping track of the crown',
value = '```bunco```',
inline = True
)
embed.add_field(
name = 'If the head table gets 21',
value = '```ring``` (only works in <#{}> and <#{})>.'.format(generalc,httext),
inline = False
)
embed.add_field(
name = "Voice Channel Controls:",
value = "(works in the #rolling- channel(chat) that is paired with your table Voice- channel)",
inline = False
)
embed.add_field(
name = "Winning(Move up a table)",
value = "```up``` ",
inline = True
)
embed.add_field(
name = "Losing(Moving down a table)",
value = "```down```",
inline = True
)
