import python_bitbankcc#インストールが必要
import requests
import json
import time
import datetime
import numpy as np#インストールが必要
import matplotlib.pyplot as plt#インストールが必要

#http://okuribitoni.hatenablog.com/entry/2018/01/11/211204を参考にした。

sellPriceList = []
listLength = 0
maxlength = 100 #ﾁｬｰﾄx方向最大値です。
frequency = 3 #ﾃﾞｰﾀ取得周期です。
while True:

    #現在の時刻を取得
    print(datetime.datetime.today())

    pub = python_bitbankcc.public()
    value = pub.get_ticker(
        'xrp_jpy' # ペア
    )
    #print(value)

    #現在の売り最安値 (sell)
    #現在の買い最高値 (buy)
    #過去24時間の最高値 (higt)
    #過去24時間の最安値 (low)


    #からそれぞれ'現在の売り最安値 (sell)'を取得します。
    sell = value['sell']


    if listLength<maxlength:

        sellPriceList.append(sell)

    else:
        #list内の要素がmaxlengthを超えたら、
        #先頭の1要素を削除し、最後尾に追加します。
        sellPriceList.pop(0)
        sellPriceList.append(sell)

    #ﾁｬｰﾄ用ﾃﾞｰﾀの作成をします。
    coincheck = np.array(sellPriceList)
    listLength = len(sellPriceList)
    x = np.linspace(0,listLength,listLength)

    #ここからﾁｬｰﾄ作成です
    plt.figure(1)
    plt.plot(x,coincheck, label = 'xrp/jpy(sell)')
    #plt.plot(x,zaif, label = 'xrp/jpyの現在の買い最高値')
    plt.legend()
    plt.pause(.001)
    plt.clf()

    time.sleep(frequency)

    #毎秒取得
    #time.sleep(1)



