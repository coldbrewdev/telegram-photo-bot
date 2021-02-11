bot_key = '123456789:AABBCC1234NNBBVV'
channel = '-1001234567'  # configuration assumes channel, but any chat_ID will do
admin_id = '987654321'  # could just set as channel if you want error messages to go there
hosted_url = 'https://www.myfancywebsite.com/photos/'  # web folder where photo will be found
local_directory = 'photos/'  # directory to scan for photos and remove photo from at end

# Optional - Use absolute path to set your local directory, mind your slashes
import os

script_directory = os.path.dirname(os.path.abspath(__file__))
local_directory = script_directory + '/' + local_directory
