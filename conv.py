# python currency converter

import requests
import sys
import json

API_KEY = ''
api = 'https://freecurrencyapi.net/api/v2/latest?apikey='+str(API_KEY)
response = requests.get(api)

try:
    response.raise_for_status()
except Exception as exc:
    print('Page not found!')
    sys.exit()

currencies = json.loads(response.text)['data']

print('Choose a currency:')
currency = input().upper()

try:
    print('1 USD = '+str(currencies[currency])+' '+currency)
except KeyError as kExc:
    print('Not a valid currency!')
    sys.exit()

print('How much USD would you like to convert?')
amountToConvert = input()

convertedAmount = float(amountToConvert) * float(currencies[currency])

print(str(amountToConvert)+' USD = '+str(convertedAmount)+' '+currency)
