import ccxt#インストールが必要
import time
import datetime
import numpy as np#インストールが必要
import matplotlib.pyplot as plt#インストールが必要

#http://okuribitoni.hatenablog.com/entry/2018/01/11/211204を参考にした。

sellPriceList = []
listLength = 0
maxlength = 100 #ﾁｬｰﾄx方向最大値です。
frequency = 1 #ﾃﾞｰﾀ取得周期です。
exchange_list = ['bitbank',]#使用する取引所

ask_exchange = ''
ask_price = 99999999
bid_exchange = ''
bid_price = 99999999

for exchange_id in exchange_list:


    while True:
        exchange = eval('ccxt.' + exchange_id + '()')
        orderbook = exchange.fetch_order_book(symbol='XRP/JPY')  # symbol: 通貨ペア 例(XRP/JPYは1リップルは日本円でいくらになるか。)
        #bid = orderbook['bids'][0][0] if len(orderbook['bids']) > 0 else None  # 買い注文=bids
        #print(bid)
        ask = orderbook['asks'][0][0] if len(orderbook['asks']) > 0 else None  # 売り注文=asks
        print(ask)

        #現在の時刻を取得
        print(datetime.datetime.today())


        if listLength<maxlength:
            sellPriceList.append(ask)
        else:
            #list内の要素がmaxlengthを超えたら、
            #先頭の1要素を削除し、最後尾に追加します。
            sellPriceList.pop(0)
            sellPriceList.append(ask)
        #ﾁｬｰﾄ用ﾃﾞｰﾀの作成をします。
        coincheck = np.array(sellPriceList)
        listLength = len(sellPriceList)
        x = np.linspace(0,listLength,listLength)
        #ここからﾁｬｰﾄ作成です
        plt.figure(1)
        plt.plot(x,coincheck, label = 'bitbank(xrp/jpy)')
        #plt.plot(x,zaif, label = 'xrp/jpyの現在の買い最高値')
        plt.legend()
        plt.pause(.001)
        plt.clf()
        time.sleep(frequency)



