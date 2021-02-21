# весь год урока
from fastapi import FastAPI
import requests
import re

app = FastAPI()

class RequestAPI:
    url = 'https://v6.exchangerate-api.com/v6/afbe87d388a7f9fec78799b7/latest/USD'
    url2 = 'https://v6.exchangerate-api.com/v6/afbe87d388a7f9fec78799b7/pair/EUR/GBP'

    def chengable_pair(self, currency1, currency2):
        c1 = currency1
        c2 = currency2
        url_in = 'https://v6.exchangerate-api.com/v6/afbe87d388a7f9fec78799b7/pair/{}/{}'.format(c1, c2)
        r = requests.get(url_in).json()
        return r['conversion_rate']

    def dinamic_currency(self, currency):
        fresh_request = requests.get(self.url).json()
        return fresh_request['conversion_rates'][currency]

    def dinamic_conversion_pair(self):
        pair_request = requests.get(self.url2).json()
        return pair_request['conversion_rate']

    def get_all(self):
        x = 'USD'
        url7 = 'https://v6.exchangerate-api.com/v6/afbe87d388a7f9fec78799b7/latest/{}'.format(x)
        result = requests.get(url7).json()
        return result

    def get_currency(self):
        result = requests.get(self.url).json()
        return result['conversion_rates']['KZT']


@app.get('/')
def index():
    index_req = RequestAPI()
    return index_req.get_all(), index_req.dinamic_conversion_pair()

@app.get('/{currency}')
def curr(currency):
    curr_req = RequestAPI()
    return 'USD = %s %s' % (curr_req.dinamic_currency(currency), currency)

@app.get('/test')
def pair():
    pair_req = RequestAPI()
    return pair_req.dinamic_conversion_pair()

@app.get('/{currency1}/{currency2}')
def ch_pair_curr(currency1, currency2):
    ch_pair_curr_req = RequestAPI()
    return ch_pair_curr_req.chengable_pair(currency1, currency2)