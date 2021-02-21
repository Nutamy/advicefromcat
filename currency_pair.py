# весь год урока
from fastapi import FastAPI
import requests

app = FastAPI()

class RequestAPI:
    url = 'https://v6.exchangerate-api.com/v6/afbe87d388a7f9fec78799b7/latest/USD'
    url2 = 'https://v6.exchangerate-api.com/v6/afbe87d388a7f9fec78799b7/pair/EUR/GBP'

    def get_all(self):
        result = requests.get(self.url).json()
        return result

    # функция для ввода двух валют и получения коэффициент конвертации между ними
    def chengable_pair(self, currency1, currency2):
        c1 = currency1
        c2 = currency2
        url_in = 'https://v6.exchangerate-api.com/v6/afbe87d388a7f9fec78799b7/pair/{}/{}'.format(c1, c2)
        r = requests.get(url_in).json()
        return r['conversion_rate']

    # Цункция для ввода одной валюты
    def dinamic_currency(self, currency):
        fresh_request = requests.get(self.url).json()
        return fresh_request['conversion_rates'][currency]


@app.get('/')
def index():
    index_req = RequestAPI()
    return 'Type currency in url line to get conversion rates  example: EUR/GBP'

@app.get('/{currency}')
def curr(currency):
    curr_req = RequestAPI()
    return 'USD = %s %s' % (curr_req.dinamic_currency(currency), currency)

@app.get('/{currency1}/{currency2}')
def ch_pair_curr(currency1, currency2):
    ch_pair_curr_req = RequestAPI()
    return '{} and {} have {} conversion rate'.format(currency1, currency2, ch_pair_curr_req.chengable_pair(currency1, currency2))