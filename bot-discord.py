import discord
import asyncio
import os.path
import random

async def print_sad(message):
    await message.channel.send(':disappointed_relieved:')
    return 0

def rdm_blob():
    blobs = [':blobcool:', ':blobaww:',':blobfistbumpR:',':blobmoustache:',':blobsmileopenmouth:',':blobpoliceangry:',':blobhammer:',':fire_engine:', ':googlefire']
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

    def checkR5(self,message):
        return (message.content.find("my r5") >= 0) or (message.content.find("my R5") >= 0)

    async def ourR5(self,message):
        await message.channel.send(message.author.mention + ", it's **OUR R5**! " + rdm_blob())

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        if self.checkR5(message):
            await self.ourR5(message)

if __name__ == "__main__":
    with open('.key', 'r', encoding="utf-8") as file:
        cred_data = file.read().split('\n')
        # print(cred_data[0])
        client = MyClient()
        client.run(cred_data[0])

# print(message.author)
# print(message.author.mention)
# print(message.author.id)
# print(self.config.users)

# id_user = st[2]
# user = discord.utils.get(message.channel.members, name = 'ildyria', discriminator = 7128)
# await message.channel.send(id_user)

# give users a link to invite this bot to their server embed.add_field(name="Invite", value="[Invite link](
# https://discordapp.com/api/oauth2/authorize?client_id=456847303479787520&permissions=256064&scope=bot)")
