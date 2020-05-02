


#L5
# -*- coding: utf-8 -*-

import requests
import json
import time



def timeloop():
  
    while True:
        profits = []
        
        url_BTC = "https://api.bitbay.net/rest/trading/stats/BTC-USD"
        response = requests.request("GET", url_BTC, headers = {'type': 'json'})
        stats = json.loads(response.text) 
        
        highest = stats["stats"]["h"]
        lowest = stats["stats"]["l"]
        
        profit_BTC = (float(highest) / float(lowest))*100 - 100
        profits.append(['BTC', profit_BTC])
        
        
        
        url_GAME = "https://api.bitbay.net/rest/trading/stats/GAME-USD"
        response = requests.request("GET", url_GAME, headers = {'type': 'json'})
        stats = json.loads(response.text)
         
        highest = stats["stats"]["h"]
        lowest = stats["stats"]["l"]
        
        profit_GAME = (float(highest) / float(lowest))*100 - 100
        profits.append(['GAME', profit_GAME])
        
        
                
        url_ETH = "https://api.bitbay.net/rest/trading/stats/ETH-USD"
        response = requests.request("GET", url_ETH, headers = {'type': 'json'})
        stats = json.loads(response.text) 
        
        highest = stats["stats"]["h"]
        lowest = stats["stats"]["l"]
        
        profit_ETH = (float(highest) / float(lowest))*100 - 100
        profits.append(['ETH', profit_ETH])
        
        
          
        url_NEU = "https://api.bitbay.net/rest/trading/stats/NEU-USD"
        response = requests.request("GET", url_NEU, headers={'type': 'json'})
        stats = json.loads(response.text) 
        
        highest = stats["stats"]["h"]
        lowest = stats["stats"]["l"]
        
        profit_NEU = (float(highest) / float(lowest))*100 - 100
        profits.append(['NEU', profit_NEU])
        
        
        
        url_LTC = "https://api.bitbay.net/rest/trading/stats/LTC-USD"
        response = requests.request("GET", url_LTC, headers={'type': 'json'})
        stats = json.loads(response.text) 
        
        highest = stats["stats"]["h"]
        lowest = stats["stats"]["l"]
        
        profit_LTC = (float(highest) / float(lowest))*100 - 100
        profits.append(['LTC', profit_LTC])
        
        
        
        profits.sort(key = lambda x:x[1],reverse = True)
        for i in range(len(profits)):
            if profits[i][1] >= 0:
                print(profits[i][0],'+', round(profits[i][1], 5), '%')
            else:
                print(profits[i][0], round(profits[i][1], 5), '%')
                

        time.sleep(300)
        

    
timeloop()                    
            

    
