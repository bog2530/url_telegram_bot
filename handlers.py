import json

from config import application
from utils import download_file, open_file, save_db


def hello_user(update, context):
    user = update.message.from_user
    update.message.reply_text(
        'Hi {}'.format(user['first_name']),
        )


def download_docs(update, context):
    docs = update.message.document
    print(docs['mime_type'])
    if docs['mime_type'] in application:
        user_id = update.message.from_user['id']
        exel_file = context.bot.getFile(
            update.message.document.file_id)
        file = download_file(exel_file, user_id)
        example_url = open_file(file)
        if example_url == 0:
            update.message.reply_text('Wrong record format')
        elif example_url == -1:
            update.message.reply_text('No values')
        elif example_url == -2:
            update.message.reply_text('There are zero values')
        else:
            save_db(example_url)
            update.message.reply_text(json.dumps(example_url, indent=3))
    else:
        update.message.reply_text('Incorrect format')
