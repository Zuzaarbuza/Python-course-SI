# -*- coding: utf-8 -*-
"""
Created on Fri Apr 17 11:12:53 2020

@author: zunot
"""


#L4
# -*- coding: utf-8 -*-

import requests
import json
import time

def timeloop():
    while True:
        r_bitbay = requests.get("https://bitbay.net/API/Public/BTC/ticker.json")
        bitbay_buy = r_bitbay.json()["ask"]
        bitbay_sell = r_bitbay.json()["bid"]

        r_blockchain = requests.get('https://blockchain.info/ticker')
        blockchain_sell = r_blockchain.json()["USD"]["sell"]
        blockchain_buy = r_blockchain.json()["USD"]["buy"]

        r_bitfinex = requests.get("https://api.bitfinex.com/v1/pubticker/btcusd")
        bitfinex_buy = float(r_bitfinex.json()["ask"])
        bitfinex_sell = float(r_bitfinex.json()["bid"])

        r_bitstamp = requests.get("https://www.bitstamp.net/api/ticker/")
        bitstamp_buy = float(r_bitstamp.json()["high"])
        bitstamp_sell = float(r_bitstamp.json()["low"])

        bitbay_taker_fee = 0.0027
        blockchain_taker_fee = 0.0024
        bitfinex_taker_fee = 0.002
        bitstamp_taker_fee = 0.0025

        bids_list = [bitbay_sell, blockchain_sell, bitfinex_sell, bitstamp_sell]
        asks_list = [bitbay_buy, blockchain_buy, bitfinex_buy, bitstamp_buy]
        markets = ['Bitbay', 'Blockchain', 'Bitfinex', 'Bitstamp']
        comission = [bitbay_taker_fee, blockchain_taker_fee, bitfinex_taker_fee, bitstamp_taker_fee]

        wallet = 10000
        print('You have : ', wallet, 'USD in your wallet')

        for i in range(len(asks_list)):
            for j in range(len(bids_list)):
                if i != j:
                    if asks_list[i] < bids_list[j]:

                        print('Buy 1BTC from', markets[i],'for',asks_list[i], 'and sell on', markets[j],'for',bids_list[j], 'with profit of ',round(bids_list[j] - bids_list[i], 2),'USD')

                        bids_list[j] += (bids_list[j] * comission[j])
                        asks_list[i] += (asks_list[i] * comission[i])

                        profit = (bids_list[j] - asks_list[i])
                        print('With tacker fee you earn', round(profit, 2),'USD')

                        wallet += profit
                        print('Now you have', round(wallet, 2), ' USD in your wallet')
        time.sleep(7)
    
timeloop()                    
            



    
