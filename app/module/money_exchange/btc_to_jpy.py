"""BTCを日本円に変換するモジュール"""


# インポート
from app.module.exchangess import bitbank


def btc_to_jpy(btc):
    """BTCの枚数を引数として受け取り、日本円の金額に変換するメソッドです"""
    bitbankorderbook = bitbank.BITBANK.currencyinformation('BTC')
    bid = bitbankorderbook['bid'].get('bitbank')
    jpy = btc * bid  # BTCを日本円の額に変換する bitbank btc/jpy bidを呼び出す。
    return jpy

if __name__ == "__main__":  # テスト用
    print(btc_to_jpy(1))
