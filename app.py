from pyrogram import Client
from pyrogram import filters
import sys, traceback
from datetime import datetime
from googletrans import Translator

# ~~~~~~ CONFIG ~~~~~~~~ #
ACCOUNT = "my_app"
PHONE_NR = "+123456789"

# API ID and Hash from https://my.telegram.org/auth?to=apps
API_ID = 1234567
API_HASH = "API_HASH"

# Channel IDs...
INPUT__official = ID
INPUT__testchannel = ID
OUTPUT__MT_FORWARD_CHAT_ID = ID
# ~~~~~~~~~~~~~~~~~~~~~~ #

try:
    # 初始化 Pyrogram 客戶端
    app = Client(
        ACCOUNT,
        phone_number=PHONE_NR,
        api_id=API_ID,
        api_hash=API_HASH
    )

    # 初始化翻譯器
    translator = Translator()

    # 設置過濾器
    f = filters.chat(INPUT__official) | filters.chat(INPUT__testchannel)

    @app.on_message(f)
    async def my_handler(client, message):
        try:
            print(message)

            # 檢查發送者類型
            if message.from_user:  # 如果是個人用戶
                username = message.from_user.username
                if not username:
                    print("No username found. Skipping message.")
                    return

                # 篩選特定 username
                allowed_usernames = {"yiu99999", "maxonamission1"}
                if username not in allowed_usernames:
                    print(f"Username {username} is not allowed. Skipping message.")
                    return

            elif message.sender_chat:  # 如果是頻道或群組
                sender_title = message.sender_chat.title
                print(f"Message is from a channel/group: {sender_title}. Processing message.")

            else:
                print("Unknown sender type. Skipping message.")
                return

            # 檢查是否有媒體與文字
            translated_caption = None
            if message.caption:  # 如果有文字標題
                # 翻譯文字為中文
                translated_caption = translator.translate(message.caption, src='en', dest='zh-cn').text

            if message.media:  # 如果消息包含媒體
                await message.copy(
                    chat_id=OUTPUT__MT_FORWARD_CHAT_ID,
                    caption=translated_caption or message.caption or ""  # 如果翻譯失敗則使用原文
                )
            else:  # 如果是純文字消息
                translated_text = translator.translate(message.text, src='en', dest='zh-cn').text
                await client.send_message(
                    chat_id=OUTPUT__MT_FORWARD_CHAT_ID,
                    text=translated_text
                )

        except Exception as e:
            print(f"Error handling message: {e}")
            traceback.print_exc()

    # 啟動應用
    app.run()

except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
