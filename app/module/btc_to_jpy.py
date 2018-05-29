'''
BTCを現金化するときに何円になるか計算するモジュールです
'''
#インポート
import ccxt
from app import module
def btc_to_jpy(btc):
    '''
    BTCの枚数を引数として受け取り、日本円の金額に変換するメソッドです
    '''

    BITBANKORDERBOOK = module.exchanges.bitbank.btc

    bid = BITBANKORDERBOOK['bid'].get('bitbank_id')

    jpy = btc * bid #BTCを日本円の額に変換する bitbank btc/jpy bidを呼び出す。
    return jpy

if __name__ == "__main__": #テスト用
    print(btc_to_jpy(1))
