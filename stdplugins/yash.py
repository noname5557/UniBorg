"""Emoji

Available Commands:

.yash """

from telethon import events

import asyncio





@borg.on(events.NewMessage(pattern=r"\.(.*)", outgoing=True))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1
    

    animation_ttl = range(0, 75)

    input_str = event.pattern_match.group(1)

    if input_str == "yash":

        await event.edit(input_str)

        animation_chars = [

            "y",
            "ya",
            "yas",
            "yash",
            "yashh",    
            "yashhh",
            "yashhhh",
            "yashhhhh",
            "yashhhhhh",
            "yashhhhhhh",
            "yashhhhhhhh",
            "yashhhhhhhhh",    
            "yashhhhhhhhhh",
        ]

        for i in animation_ttl:


            await event.edit(animation_chars[i % 75])
