import python_bitbankcc
import requests
import json
import time
import datetime


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
    print('sell:' + value['sell'] + ' buy:' + value['buy'] + ' high:' + value['high'] + ' low:' + value['low'])

    print()

    #毎秒取得
    time.sleep(1)
