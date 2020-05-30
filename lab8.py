import json
import requests
import time
import matplotlib.pyplot as plt 
import numpy as np
from datetime import datetime
import random

d_30_04 = 1588284000000
d_14_05 = 1589493600000
d_28_05 = 1590703200000

def GET_VOLUMES(datefrom, dateto, currency):
    time_now = int((time.time())*1000)
    url = "https://api.bitbay.net/rest/trading/candle/history/"+currency+"-USD/86400"
    querystring = {"from": str(datefrom) , "to": str(dateto)}
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
        top  = moving_average + np.std(np.array(vol))*0.7
        bottom = moving_average - np.std(np.array(vol))*0.7
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
    plt.rcParams['figure.figsize'] = (20, 10)
    plt.style.use('fivethirtyeight')
    fig, ax1 = plt.subplots()
    t = d_30_04
    for i in range(len(vol)):
        x.append(Date(t))
        y.append(vol[i])
        t += 86400000
    for i in range(len(vol)-1):   
        if i == 0:
            colors[0] = 'seagreen'
        if i+1 >= lenght:
            colors[i+1] = 'cornflowerblue'
        else:
            colors[i+1] = "seagreen"
    ax1.set_xticks(np.arange(len(x)))   
    for i, t in enumerate(ax1.get_xticklabels()):
        if (i % int(len(x)/5)) != 0:
            t.set_visible(False)
    plt.ylabel('Height of volume') 
    plt.xlabel('Dates') 
    ax2 = ax1.twinx() 
    ax2.set_yticks([])
    ax3 = ax1.twinx()
    ax3.set_yticks([])
    ax2 = ax2.bar(x,y, color = colors, alpha = 0.4)
    ax1 = ax1.plot(x, Z, color = 'royalblue')
    ax3 = ax3.bar(x, Y, color ='seagreen', alpha = 0.7)
    plt.title('BTC Volume value from '+Date(d_30_04)+' to '+Date(d_28_05))  
    legend = {'Real volume value': 'seagreen', 'Average from 100 simulations':'royalblue', 'One simulation':'cornflowerblue'}         
    labels = list(legend.keys())
    handles = [plt.Rectangle((0,0),0,1, color=legend[label]) for label in labels]
    plt.legend(handles, labels)
        
def Real_data():   
    global Y
    Y = []
    for i in range(len(vol)): 
        Y.append(vol[i])
        
def Sym_data():
    global Z
    Z = []
    for i in range(len(vol)):
        Z.append(vol[i])       

GET_VOLUMES(d_30_04, d_28_05, "BTC")
Real_data()    
GET_VOLUMES(d_30_04, d_14_05, "BTC")
Sym(100)
Sym_data()
GET_VOLUMES(d_30_04, d_14_05, "BTC")
Sym(1)
Graphs()











   