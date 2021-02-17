# telegram-photo-bot
The telegram-photo-bot is a bot that sends random images from a folder to a channel or chat.

The motivation is to schedule the script to run, for example, daily to send you some of your favorite family photos.
## Installation

Install via git.
```bash
git clone https://github.com/coldbrewdev/telegram-photo-bot
```

## Configuration

The telegram-photo-bot requires:
1. A telegram bot
1. A folder of images
1. A domain that hosts that folder online

A sample config.py file is provided. 

The bot runs directly on the Telegram HTTP API, no supporting modules are needed.

To retrieve image metadata, the PIL module is required. We recommend installing via the Pillow fork:
```bash
pip install Pillow
```

## Example Workflow
Here is an example of how the bot would operate using the sample-config.py configuration.
1. The script scans the local photos/ folder for jpeg, jpg, and png files. 
It provides a warning if you are running low, and quits if you have run out.
1. The script selects a random photo, and compiles the URL at your domain + the image filename.
1. The script calls the telegram bot via the HTTP API using the bot API Key, and the chat_ID provided.
1. If the JSON response from the API is not ok, the bot sends an error to the admin.
1. The script retrieves the date of photo and sends it to the channel via the telegram API.
1. The script logs the file as sent in a txt file.
1. The script deletes the file from the folder. 
   (This line is easy to comment out if you don't mind recycling photos.)
