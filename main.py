# To start APP print in terminal: uvicorn main:app 
# 42 минута видео 
# ссылка: 
# https://us02web.zoom.us/rec/play/aFJARXD3QPoCtyOBtO3JJrToKCdfhTCqQjeFHsKXv9u9q19c11yuyIECqEPPg7uSB1YJuYjZa7qOyhnV.ZuYRBPDhPajuQXvq?continueMode=true&_x_zm_rtaid=__w6UuLjR0W9OtXYi6i5CQ.1611994976641.a37456740e2448d3a05bb05a38643505&_x_zm_rhtaid=946
# api.openweathermap.org/data/2.5/weather?q={almaty}&appid={8b682e300f8818e7cc6238b05b3fc814} 
# to delet conection with git: sudo rm -R .git

from typing import Optional
from fastapi import FastAPI, Request
import requests
from fastapi.templating import Jinja2Templates
from random import randint

app = FastAPI()
templates = Jinja2Templates(directory='templates')

class RequestAPI:
    url = 'https://api.quotable.io/random'
    def get_all(self):
        result = requests.get(self.url).json()
        return result
    
    def get_quote(self):
        result = requests.get(self.url).json()

        return result['content']
    
    def get_text(self, name):
        return '%s, hi! I want to say you: %s' % (name, self.get_quote())

@app.get('/')
def index(request: Request):
    my_request = RequestAPI()
    advise = my_request.get_quote()
    y = randint(1,9)
    x = randint(1,9)
    return templates.TemplateResponse('index.html', {
        'request': request,
        'name': 'Alina',
        'advise': advise,
        'x': x,
        'y': y
        })

@app.get("/names")
def names_one(name):
    my_request = RequestAPI()
    return my_request.get_quote()

@app.get("/names/{name}")
def names_one(name):
    my_request = RequestAPI()
    name = name.capitalize()
    return my_request.get_text(name), '\n', my_request.get_all()
