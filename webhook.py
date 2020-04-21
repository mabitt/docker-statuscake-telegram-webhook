import sys
import os
import pycurl
import hashlib
import logging

from flask import Flask, request, abort, jsonify

LOGLEVEL = os.environ.get('LOGLEVEL', 'WARNING').upper()
logging.basicConfig(level=LOGLEVEL)

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')
TELEGRAM_CHAT_ID = os.environ.get('TELEGRAM_CHAT_ID')
bot_url = 'https://api.telegram.org/bot' + TELEGRAM_BOT_TOKEN + '/sendMessage'

SC_API_TOKEN = os.environ.get('SC_API_TOKEN')
logging.info('Autorized Token: %s' % SC_API_TOKEN)

#SC_USER = os.environ('SC_USER')
#SC_APIKEY = os.environ('SC_APIKEY')
#webhook_token_str = '%s%s' % (SC_USER, SC_APIKEY)
#logging.info('Text to Hash: %s' % webhook_token_str)
#webhook_token = hashlib.md5(webhook_token_str.encode())
logging.info('Autorized Token: %s' % webhook_token.hexdigest())

app = Flask(__name__)
turl = pycurl.Curl() 
turl.setopt(turl.URL, bot_url)

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'POST':
        sc_token = request.form.get('Token')
        sc_status = request.form.get('Status')
        sc_statuscode = request.form.get('StatusCode')
        sc_url = request.form.get('URL')
        sc_ip = request.form.get('IP')
        sc_tags = request.form.get('Tags')
        sc_name = request.form.get('Name')
        sc_checkrate = request.form.get('CheckRate')
        logging.info('Received Token: %s' % sc_token)
        sc_text = '%s - %s' % (sc_name, sc_status)
        logging.info('Text: %s' % sc_text)
        if sc_token == SC_API_TOKEN:
            telegram_data = '{"chat_id": "%s" , "text": "%s"}' % (TELEGRAM_CHAT_ID, sc_text)
            turl.setopt(turl.HTTPHEADER, ['Accept: */*',
                                          'Content-Type: application/json'])
            turl.setopt(turl.POSTFIELDS, telegram_data)
            turl.perform()
            logging.info('Telegram Status: %d' % turl.getinfo(turl.RESPONSE_CODE))
            if turl.getinfo(turl.RESPONSE_CODE) == 200:
                return jsonify({'status':'success'}), 200
            else:
                return jsonify({'status':'telegram api error'}), 401
            turl.close()
        else:
            return jsonify({'status':'bad token'}), 401
    else:
        return 'OK', 200

if __name__ == '__main__':
    app.run()

#if __name__ == "__main__":
#    from waitress import serve
#    serve(app, host="0.0.0.0", port=8080)