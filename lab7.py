import json
import requests
import time
import matplotlib.pyplot as plt 
import numpy as np
from datetime import datetime
import random

print("Which currency do you want to check? \n Available: BTC, ETH, LTC")
input1 = input()
print("Enter unix timestamp in miliseconds of starting date of analysis")
input2 = input()  

def GET_VOLUMES(date, currency):
    time_now = int((time.time())*1000)
    url = "https://api.bitbay.net/rest/trading/candle/history/"+input1+"-USD/86400"
    querystring = {"from": str(date) , "to": str(time_now)}
    response = requests.request("GET", url, params = querystring)
    stats = json.loads(response.text)
    global vol
    vol = []
    for i in range(len(stats['items'])):
        data = stats['items'][i][1]['v']
        vol.append(data)
    vol = [float(i) for i in vol] 
    global lenght
    lenght = len(vol)
  
def Bollinger_Bands():     
    weights = []
    i = 1
    while i <= len(vol):
        weights.append(i)
        i +=1
    temp = 0
    for k in range(len(vol)):
        temp+= vol[k]*weights[k]
        k-=1
    l = lenght
    day = 0
    while l > 0:
        moving_average = temp/sum(weights)  
        top  = moving_average + np.std(np.array(vol))*1.1
        bottom = moving_average - np.std(np.array(vol))*1.1
        if bottom < 0:
            bottom = min(vol)
        weights.append(weights[-1]+1)
        new_day = random.uniform(bottom, top+1)
        temp+= vol[-1] * weights[-1]
        future[day].append(new_day)
        day +=1
        l -= 1
          
def Sym(number):
    global future
    future = []
    ratings = []
    for i in range(lenght):
        future.append([])
        ratings.append([])
    for i in range(number):
        Bollinger_Bands()
    for i in range(len(future)):
        av_day = sum(future[i])/len(future[i])
        vol.append(av_day)
        ratings[i].append(av_day)
        ratings[i].append(np.median(np.array(future[i])))
        ratings[i].append(np.std(np.array(future[i])))
           
def Date(date):
    ts = int(date)/1000
    d = datetime.utcfromtimestamp(ts).strftime('%d-%m-%Y')
    return d
        
def Graphs():    
    x = []
    y = []
    colors = [0] * int(len(vol))
    fig = plt.figure()
    ax = fig.add_axes([0,0,1,1])
    t = int(input2)
    for i in range(len(vol)):
        x.append(Date(t))
        y.append(vol[i])
        t += 86400000
    for i in range(len(vol)-1):   
        if i == 0:
            colors[0] = 'g'
        if vol[i] <= vol[i+1]:
            if i+1 >= lenght:
                colors[i+1] = 'cornflowerblue'
            else:
                colors[i+1] = 'seagreen'
        elif vol[i] > vol[i+1]:
            if i+1 >= lenght:
                colors[i+1] = 'cornflowerblue'
            else:
                colors[i+1] = 'r'
    ax.set_xticks(np.arange(len(x)))   
    for i, t in enumerate(ax.get_xticklabels()):
        if (i % int(len(x)/4)) != 0:
            t.set_visible(False)
    ax = ax.bar(x,y, color=colors)
    plt.xlabel('Dates') 
    plt.ylabel('Height of volume')  
    plt.title('Volume graph from '+Date(input2)+' and future volume height prediction')  
    legend = {'Increase in the past': 'seagreen', 'Decrease in the past':'r', 'Predicted future':'cornflowerblue'}         
    labels = list(legend.keys())
    handles = [plt.Rectangle((0,0),1,1, color=legend[label]) for label in labels]
    plt.legend(handles, labels)
        
GET_VOLUMES(input2, input1)
Sym(10)
Graphs()






   