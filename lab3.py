# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:47:59 2020

@author: User
"""

import requests

def bitbay_data():
    url = 'https://bitbay.net/API/Public/BTC/orderbook.json'
    response = requests.get(url)
    return response.json()

orders_bitbay = bitbay_data()

asks = orders_bitbay['asks']
bids = orders_bitbay['bids']

def show_data():
    print('5 offers from bitbay\n')
    print('sale price:','\n','[exchange rate in USD],[ammount od Bitcoin]','\n')
    i = 5
    j = 5
    while i >= 0:
        print(asks[i],'\n')
        i -= 1    
    print('buy price:','\n','[exchange rate in USD],[ammount od Bitcoin]','\n')
    while j >= 0:
        print(bids[j],'\n')
        j -= 1
show_data()
    
def bitbay_ticker():
    url = 'https://bitbay.net/API/Public/BTC/ticker.json'
    response = requests.get(url)
    return response.json()
    
def blockchain_ticker():
    url = 'https://blockchain.info/ticker'
    response = requests.get(url)
    return response.json()


bitbay_ticker = bitbay_ticker()   
blockchain_ticker = blockchain_ticker()

sell_blockchain = blockchain_ticker['USD']['sell']
buy_blockchain = blockchain_ticker['USD']['buy']

buy_bitbay = bitbay_ticker['ask']
sell_bitbay = bitbay_ticker['bid']

if buy_blockchain < buy_bitbay:
    print('You should buy Bitcoin from Blockchain for',buy_blockchain,'USD instead of Bitbay for',buy_bitbay,'USD')
else:
    print('You should buy Bitcoin from Bitbay for',buy_bitbay,'USD istead od Blockchain for',buy_blockchain,'USD')

if sell_blockchain > sell_bitbay:
    print('You should sell Bitcoin on Blockchain for',sell_blockchain,'USD instead of Bitbay for',sell_bitbay,'USD' )
else:
    print('You should sell Bitcoin on Bitbay for',sell_bitbay,'USD instead of Blockchain for',sell_blockchain,'USD')
