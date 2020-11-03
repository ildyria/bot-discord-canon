import discord
import asyncio
import os.path
import random
import re

async def print_sad(message):
    await message.channel.send(':disappointed_relieved:')
    return 0

def rdm_blob():
    # blobs = [':blobcool:', ':blobaww:',':blobfistbumpR:',':blobmoustache:',':blobsmileopenmouth:',':blobpoliceangry:',':blobhammer:',':fire_engine:', ':googlefire:']
    blobs = [':fire_engine:', ':fire_extinguisher:', ':camera:', ':detective:', ':rage:']
    return random.choice(blobs)


class MyClient(discord.Client):
    
    async def error(self, message, comment):
        default_channel, control_channel = self.get_channels()
        await message.remove_reaction('✅', self.user)
        await message.add_reaction('❌')
        await control_channel.send(comment)
        await print_sad(message)

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('---------------------------------')

    async def sendR5(self,message):
        f = discord.File("ourr5.jpg", filename="ourr5.jpg")
        await message.channel.send(file=f)

    async def my(self, message, obj, printed):
        findme = 'my\s\w?\s?' + obj
        p = re.compile(findme, re.IGNORECASE | re.MULTILINE)
        if p.search(message.content):
            if printed == 'R5' and random.randint(0, 4) == 4:
                self.sendR5(message)
            else:
                await message.channel.send(message.author.mention + ", it's **OUR " + printed + "**! " + rdm_blob())

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        await self.my(message, 'R5', 'R5')
        await self.my(message, 'R6', 'R6')
        await self.my(message, 'C70', 'C70')
        await self.my(message, '70-135', '70-135mm')

if __name__ == "__main__":
    with open('.key', 'r', encoding="utf-8") as file:
        cred_data = file.read().split('\n')
        client = MyClient()
        client.run(cred_data[0])

# give users a link to invite this bot to their server embed.add_field(name="Invite", value="[Invite link](
# https://discord.com/api/oauth2/authorize?client_id=772901093645484086&permissions=126016&scope=bot)")
