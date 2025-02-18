# **📢 Telegram @all Mention Bot**
A **Telegram bot** built with `Telethon` that listens for messages **containing "@all"** in a group chat and replies by mentioning all group members while following certain constraints.

---

## 🚀 **Features**
✅ **Listens for messages containing "@all"** in group chats.  
✅ **Mentions all group members with constraints** to avoid excessive mentions.  
✅ **Handles different group sizes:**
   - **More than 10 members** → ❌ **Does nothing**.
   - **Between 5 and 10 members** → ✅ **Replies with two messages** (first message mentions 5 members, second mentions the rest).
   - **Less than 5 members** → ✅ **Replies with a single message mentioning all**.  
✅ Uses **@username** if available, otherwise a **clickable mention** with their first name.  
✅ Uses **async operations** for efficiency.  

---

## 📌 **Requirements**
Make sure you have the following installed before running the bot:

- **Python 3.8+**
- **A Telegram Bot API token**
- **Telethon library**
- **A Telegram bot with admin rights** (to fetch members)

---

## 🔧 **Installation & Setup**
### **1️⃣ Clone the repository**
```bash
git clone https://github.com/yourusername/telegram-mention-bot.git
cd telegram-mention-bot
```

### **2️⃣ Install dependencies**
```bash
pip install -r requirements.txt
```
_(Make sure `Telethon` and `python-dotenv` are installed.)_

### **3️⃣ Create a `.env` file**
Inside the project folder, create a `.env` file and add your Telegram bot credentials:

```
API_ID=your_api_id
API_HASH=your_api_hash
BOT_TOKEN=your_bot_token
```

Replace `your_api_id`, `your_api_hash`, and `your_bot_token` with your actual credentials.

### **4️⃣ Run the bot**
Start the bot with:

```bash
python bot.py
```

---

## 🔹 **How It Works**
1️⃣ The bot listens for **any message containing "@all"** in a group chat.  
2️⃣ It retrieves **all group members**.  
3️⃣ Based on the **number of members**, it decides how to respond:
   - **More than 10 members** → The bot does **NOTHING**.  
   - **Between 5 and 10 members** → The bot sends **two separate messages**, each mentioning a portion of the group.  
   - **Less than 5 members** → The bot **mentions everyone in a single message**.  
4️⃣ The bot replies with the **mention format**:
   - If a user has a **username** → `@username`
   - Otherwise → `[FirstName](tg://user?id=12345)`

---

## ⚠️ **Important Notes**
🔹 **Bot must have admin rights** to fetch group members.  
🔹 Large groups (over 10 members) **will not be tagged** due to Telegram restrictions.  
🔹 Avoid excessive mentions to prevent **rate limits**.  

---

## 🎯 **Example Usage**
💬 **User message:**  
```
Hey everyone, let's discuss the meeting @all
```

🤖 **Bot reply (if 7 members exist):**  
```
👥 John tagged everyone:

@alice @bob [Charlie](tg://user?id=123456789) @david @emily
```
_(Second message follows)_
```
👥 Continuing mentions:

@frank @george
```

---

## 🔮 **Future Enhancements**
For future improvements, we can add:
✅ **Custom mention groups:** Each group can **define its important members**, and a custom command (e.g., `@vip`) can be used to tag only those users.  
✅ **Mention limits per hour:** To **prevent spam**, the bot can limit how often "@all" can be used.  
✅ **Admin-configurable settings:** Group admins can adjust **mention limits** and **tagging rules**.  

---

## 🤖 **Credits**
Developed using **Python + Telethon**. Feel free to **fork, modify, and contribute**!  
