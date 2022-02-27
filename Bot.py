import time
from telethon.sync import TelegramClient, events

api_id = 18722357
api_hash = "ff6dffa8f6caf7eb6c82210e7855eb09"
client = TelegramClient('kia', api_id, api_hash) 
client.start()
async def handler(event):
    chat = await event.get_chat()
    sender =await event.get_sender()
    chat_id = event.chat_id
    sender_id = event.sender_id
@client.on(events.NewMessage(incoming=True, pattern=r'\.save'))
async def handler(event):
    if event.is_reply:
        replied = await event.get_reply_message()
        sender = replied.sender
        await client.download_profile_photo(sender)
        await event.respond('Saved your photo {}'.format(sender.username))
@client.on(events.NewMessage(incoming=True))

async def my_event_handler(event):
    if event.raw_text == "edit":
        await event.edit("Message Edited!")
    elif event.raw_text == "سلام":
        await event.reply("دلام عجیجم")
    elif event.raw_text == "بای":
        await event.reply("بابای اوجملم")
    elif event.raw_text == "delete":
        await event.delete()
    if 'hello' in event.raw_text:
       await event.reply('hi!')
client.run_until_disconnected()
