"""BTCを日本円に変換するモジュール"""

# インポート
from app.module.exchangess import bitbank

exhanges, ask, bid = bitbank.BITBANK.currencyinformation('BTC')


def btc_to_jpy(btc: float) -> float:
    try:
        """BTCの枚数を引数として受け取り、日本円の金額に変換するメソッドです"""
        jpy = btc * bid  # BTCを日本円の額に変換する bitbank btc/jpy bidを呼び出す。
        print(type(btc), type(bid), type(jpy))
        print(jpy)
        return round(jpy, 3)
    except TypeError:
        return print('変換の処理に問題が発生しました')

if __name__ == "__main__":  # テスト用
    print(type(btc_to_jpy(1)))
