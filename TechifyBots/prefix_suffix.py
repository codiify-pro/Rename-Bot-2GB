from pyrogram import Client, filters, enums
from helper.database import jishubotz


@Client.on_message(filters.private & filters.command('setprefix'))
async def add_prefix(client,message):
    if len(message.command)==1:
        return await message.reply_text("**Give The Prefix**\n\nExample:- `/setprefix @TechifyBots`",quote=True)
    prefix=message.text.split(" ",1)[1]
    m=await message.reply_text("Please Wait ...",quote=True)
    await tb.set_prefix(message.from_user.id,prefix)
    await m.edit("**Prefix Saved Successfully ✅**")

@Client.on_message(filters.private & filters.command('delprefix'))
async def delete_prefix(client,message):
    m=await message.reply_text("Please Wait ...",quote=True)
    prefix=await tb.get_prefix(message.from_user.id)
    if not prefix:
        return await m.edit("**You Don't Have Any Prefix ❌**")
    await tb.set_prefix(message.from_user.id,None)
    await m.edit("**Prefix Deleted Successfully 🗑️**")

@Client.on_message(filters.private & filters.command('seeprefix'))
async def see_prefix(client,message):
    m=await message.reply_text("Please Wait ...",quote=True)
    prefix=await tb.get_prefix(message.from_user.id)
    if prefix:
        await m.edit(f"**Your Prefix :-**\n\n`{prefix}`")
    else:
        await m.edit("**You Don't Have Any Prefix ❌**")

@Client.on_message(filters.private & filters.command('setsuffix'))
async def add_suffix(client,message):
    if len(message.command)==1:
        return await message.reply_text("**Give The Suffix**\n\nExample:- `/setsuffix @TechifyBots`",quote=True)
    suffix=message.text.split(" ",1)[1]
    m=await message.reply_text("Please Wait ...",quote=True)
    await tb.set_suffix(message.from_user.id,suffix)
    await m.edit("**Suffix Saved Successfully ✅**")

@Client.on_message(filters.private & filters.command('delsuffix'))
async def delete_suffix(client,message):
    m=await message.reply_text("Please Wait ...",quote=True)
    suffix=await tb.get_suffix(message.from_user.id)
    if not suffix:
        return await m.edit("**You Don't Have Any Suffix ❌**")
    await tb.set_suffix(message.from_user.id,None)
    await m.edit("**Suffix Deleted Successfully 🗑️**")

@Client.on_message(filters.private & filters.command('seesuffix'))
async def see_suffix(client,message):
    m=await message.reply_text("Please Wait ...",quote=True)
    suffix=await tb.get_suffix(message.from_user.id)
    if suffix:
        await m.edit(f"**Your Suffix :-**\n\n`{suffix}`")
    else:
        await m.edit("**You Don't Have Any Suffix ❌**")
