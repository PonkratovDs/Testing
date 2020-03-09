from flask import Flask
import requests
import json
#from flask_sslify import SSLify

#app = Flask(__name__)
#sslify = SSLify(app)


TOKEN = '1137407455:AAGxUDa2uiYaDlljJ8_6Vztk98JLrY7DA54'
URL = 'https://api.telegram.org/bot' + TOKEN + '/'


def write_json(data, filename='answer.json'):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def get_updates():
    url = URL + 'getUpdates'
    r = requests.get(url)
    #write_json(r.json())
    return r.json()

def send_message(chat_id, text='text'):
    url = URL + 'sendMessage'
    answer = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, json=answer)
    return r.json()


'''@app.route('/')
def index():
    return '<h1>Hello bot</h1>'''

def main():
    #r = requests.get(URL + 'getMe')
    #write_json(r.json())
    r = get_updates()
    #chat_id = r['result'][-1]['message']['chat']['id']
    #send_message(chat_id)
    print(r)

if __name__ == '__main__':
    main()
    #app.run()