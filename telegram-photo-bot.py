import requests
import urllib.parse
import datetime as dt
import os
import random
from PIL import Image
import config


"""Bot to Send Photos to A Channel"""

headers = {
    'User-Agent': 'Mozilla/5.0'
}


def get_date_taken(path):
    x = Image.open(path).getexif()[36867]
    y = dt.datetime.strptime(x, '%Y:%m:%d %H:%M:%S')
    z = dt.datetime.strftime(y, '%B %e, %Y')
    return z


def files_by_format(path, formats):
    y = os.listdir(path)
    file_list = [x for x in y if x.endswith(formats)]
    return file_list


def send_message(bot, chat, message):
    parse = urllib.parse.quote_plus(message)
    response = requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(bot, chat, parse))
    return response


def send_photo(bot, chat, url):
    response = requests.get("https://api.telegram.org/bot{}/sendPhoto?chat_id={}&photo={}".format(bot, chat, url))
    return response


def main():
    hosted_url = config.hosted_url
    directory = config.local_directory
    bot = config.bot_key
    admin = config.admin_id
    channel = config.channel
    image_files = files_by_format(directory, ('.jpeg', '.png', '.jpg'))
    if len(image_files) in [1, 2, 5, 10]:
        message = 'There are ' + str(len(image_files)) + ' photos left in Photo Poster (including today\'s photo).'
        send_message(bot, admin, message)
    if not image_files:
        send_message(bot, admin, 'Photo Poster is out of photos.')
        send_message(bot, channel, 'Photo Poster is out of photos. Contact the administrator.')
        raise SystemExit
    file = random.choice(image_files)
    img_url = hosted_url + file
    r = send_photo(bot, channel, img_url)
    if not r.json()['ok']:
        send_message(bot, admin, 'Telegram returned an error on Photo Poster.')
        raise SystemExit
    send_message(bot, channel, get_date_taken(directory + file))
    t = str(dt.datetime.now())
    with open(directory + 'log_sent_photos.txt', 'a') as log:
        log.write(file + ' ' + t + '\n')
    if not config.recycle:
        os.remove(directory + file)


if __name__ == '__main__':
    main()
