from telethon import TelegramClient, events
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
bot_username = os.getenv("BOT_USERNAME")
users_limit = 10

client = TelegramClient("bot_session", api_id, api_hash).start(bot_token=bot_token)

async def get_members_by_count(event, limit:int = 0):
    """Fetch the total number of members in the group"""
    chat = await event.get_chat()
    participants = await client.get_participants(chat, limit=limit)  # Fetch only the count
    return participants

async def get_all_members_usernames(chat_members):
    """Fetch all members of the group"""
    members = []
    
    for user in chat_members:
        if user.username == bot_username:
            continue  # Skip the bot itself
        if user.username:
            members.append(f"@{user.username}")
        else:
            members.append(f"[{user.first_name}](tg://user?id={user.id})")

    return members

@client.on(events.NewMessage(func=lambda e: e.is_group and ("@all" in e.raw_text or "@mention_all_group_members_bot" in e.raw_text)))
async def mention_all(event):
    """Reply to messages containing '@all' by mentioning all group members with constraints"""
    sender = await event.get_sender()
    total_members = await get_members_by_count(event, limit=users_limit + 2) # plus the bot and the limitation check (1)

    if total_members == users_limit + 2:
        # If count(total_members + robot_user + one exceeded user) exceeds users_limit
        return  # Do nothing if there are more than 10 members

    members = await get_all_members_usernames(total_members)

    if 5 < len(members) <= 10:
        first_batch = " ".join(members[:5])
        second_batch = " ".join(members[5:])

        await event.reply(f"👥 {sender.first_name} tagged everyone:\n\n{first_batch}", parse_mode="md")
        await asyncio.sleep(1)  
        await event.reply(f"👥 Continuing mentions:\n\n{second_batch}", parse_mode="md")
    else:
        mention_text = " ".join(members)
        await event.reply(f"👥 {sender.first_name} tagged everyone:\n\n{mention_text}", parse_mode="md")

print("Bot is running...")
client.run_until_disconnected()
