from pyrogram import Client, filters 
from helper.database import jishubotz
import asyncio

@Client.on_message(filters.private & filters.command('viewthumb'))
async def viewthumb(client,message):
    thumb=await tb.get_thumbnail(message.from_user.id)
    if thumb:
        sent_msg=await client.send_photo(chat_id=message.chat.id,photo=thumb)
    else:
        sent_msg=await message.reply_text("❌ **𝖸𝗈𝗎 𝖣𝗈𝗇'𝗍 𝖧𝖺𝗏𝖾 𝖠𝗇𝗒 𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅**",quote=True)
    await asyncio.sleep(30)
    await sent_msg.delete()
    await message.delete()

@Client.on_message(filters.private & filters.command('delthumb'))
async def removethumb(client,message):
    await tb.set_thumbnail(message.from_user.id,file_id=None)
    await message.reply_text("🗑️ **𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅 𝖣𝖾𝗅𝖾𝗍𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒**",quote=True)

@Client.on_message(filters.private & filters.photo)
async def addthumbs(client,message):
    mkn=await message.reply_text("⏳ **𝖯𝗅𝖾𝖺𝗌𝖾 𝖶𝖺𝗂𝗍...**",quote=True)
    await tb.set_thumbnail(message.from_user.id,file_id=message.photo.file_id)
    await mkn.edit("✅ **𝖳𝗁𝗎𝗆𝖻𝗇𝖺𝗂𝗅 𝖲𝖺𝗏𝖾𝖽 𝖲𝗎𝖼𝖼𝖾𝗌𝗌𝖿𝗎𝗅𝗅𝗒**")
    await asyncio.sleep(30)
    await message.delete()
    await mkn.delete()
