# 파이썬 코드로 텔레그램 메시지 보내기
from decouple import config
import requests

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
text = '삼성들어가서 100만원을 100장씩 벌어야지!!!!'

send_message = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message.text)