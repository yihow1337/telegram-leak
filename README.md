# Telegram Bot with Pyrogram and Google Translate

This repository contains a Python script for a Telegram bot built using the Pyrogram library. The bot listens to specific channels or users, translates messages from English to Chinese (Simplified) using Google Translate, and forwards them to another specified Telegram channel.

---

## Features
- Filters messages based on specific input channels and usernames.
- Translates text or captions from English to Chinese (Simplified).
- Forwards translated messages (with media or plain text) to a specified output channel.
- Handles exceptions gracefully and logs errors for debugging.

---

## Prerequisites

### Libraries
- **Pyrogram**: Telegram API library for Python.
- **Googletrans**: Google Translate API for Python.

Install the required libraries with the following command:
```bash
pip install pyrogram googletrans==4.0.0-rc1
```

### Telegram API Credentials
1. Create a Telegram application via [Telegram API](https://my.telegram.org/auth?to=apps).
2. Obtain the `API_ID` and `API_HASH` values.
3. Ensure you have access to the channels you want to listen to and the output channel where messages will be forwarded.

---

## Configuration

Update the script with the following variables:

```python
# Configurations
ACCOUNT = "my_app"  # Telegram client session name
PHONE_NR = "+123456789"  # Your Telegram phone number

API_ID = 1234567  # Replace with your Telegram API ID
API_HASH = "API_HASH"  # Replace with your Telegram API Hash

# Replace the following with actual channel IDs
INPUT__official = ID  # ID of the first input channel
INPUT__testchannel = ID  # ID of the second input channel
OUTPUT__MT_FORWARD_CHAT_ID = ID  # ID of the output channel
```

Replace `ID` with the respective channel IDs. You can get these by using Telegram bots or libraries to extract chat IDs.

---

## How to Run

1. Ensure you have Python installed (>= 3.7).
2. Install the required libraries.
3. Update the script with your Telegram API credentials and channel IDs.
4. Run the script:
   ```bash
   python script_name.py
   ```

---

## Functionality Overview

### Initialization
- Initializes a Pyrogram Client using the provided API credentials.
- Sets up a Google Translate instance for translating text.
- Configures filters to listen to messages from specific channels.

### Message Handling
- Listens for messages from allowed input channels.
- Filters messages by username (if applicable).
- Translates text or captions from English to Chinese (Simplified).
- Forwards messages with the translated content to the output channel.

### Error Handling
- Logs errors and exceptions for easier debugging.

---

## Notes
- The Google Translate API used here (`googletrans`) is unofficial and may not work consistently. Consider switching to an official translation API if required.
- Ensure the bot has the necessary permissions to read messages and forward them in the respective channels.
- To get the `chat_id` of a channel, use Telegram bot APIs or other Pyrogram utilities.

---

## Example

If a user `@yiu99999` sends a message "Hello world!" to `INPUT__official`:
- The bot translates it to "你好，世界！".
- Forwards the translated text to `OUTPUT__MT_FORWARD_CHAT_ID`.

If the message contains media with a caption "Check this out":
- The bot translates the caption.
- Forwards the media with the translated caption to `OUTPUT__MT_FORWARD_CHAT_ID`.

---

## Troubleshooting
- **Session Expired/Error**: Ensure the `ACCOUNT` and `PHONE_NR` are correct and authenticated.
- **Message Not Forwarded**: Check the bot’s permissions in the respective channels.
- **Translation Issues**: Verify the `googletrans` library is correctly installed and functional.

---

## License
This project is open-source and available under the MIT License.
