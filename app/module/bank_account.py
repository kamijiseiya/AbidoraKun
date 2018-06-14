import json
import time
import ccxt

class ACCOUNTINFORMATION:
    """口座情報を取得するクラス"""

    def get_private_api(self):
        """privateapiの情報を返す"""
        bitbanks = ccxt.bitbank({
            'apiKey': 'APIkey',
            'secret': 'シークレットkey'
        })
        return bitbanks

    def get_account_balance(self, getdata):
        """getdataで指定された口座残高を返却する"""
        while True:
            try:
                balance = self.fetch_balance()  # selfから残高を取得
                balancedata = None
                if (getdata == 'ALL'):
                    # 全口座残高情報を返却する
                    print(self)
                    jsonstring = json.dumps(balance, indent=4)
                    print(jsonstring)
                    balancedata = balance
                elif (getdata == 'assets'):
                    # 全資産情報情報を返却する
                    jsonstring = json.dumps(balance['info']['data'].get('assets'), indent=4)
                    print(jsonstring)
                    balancedata = balance['info']['data'].get(getdata)
                elif (getdata == 0 or getdata == 1 or getdata == 3):
                    # getdataの値が0の場合jpy、1の場合btc、3の場合xrpの資産情報を返却する。
                    jsonstring = json.dumps(balance['info']['data']['assets'][getdata], indent=4)
                    print(jsonstring)
                    balancedata = balance['info']['data']['assets'][getdata]
                else:
                    # それ以外の場合Noneを返却する。
                    balancedata = None

                return balancedata
            except ccxt.BaseError:
                print("口座情報を取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

    def get_cryptocurrency_balance(self, cryptocurrency):
        """cryptocurrencyで指定された口座情報を返す"""
        while True:
            try:
                balance = self.fetch_balance()  # selfから残高を取得
                return balance[cryptocurrency]
            except ccxt.BaseError:
                print("口座情報を取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

if __name__ == "__main__":  # テスト用
    print(ACCOUNTINFORMATION.get_account_balance(ACCOUNTINFORMATION.get_private_api(0), 'ALL'))
    print(ACCOUNTINFORMATION.get_account_balance(ACCOUNTINFORMATION.get_private_api(0), 'assets'))
    print(ACCOUNTINFORMATION.get_account_balance(ACCOUNTINFORMATION.get_private_api(0), 0))
    print(ACCOUNTINFORMATION.get_account_balance(ACCOUNTINFORMATION.get_private_api(0), 1))
    print(ACCOUNTINFORMATION.get_account_balance(ACCOUNTINFORMATION.get_private_api(0), 3))
    print(ACCOUNTINFORMATION.get_cryptocurrency_balance(ACCOUNTINFORMATION.get_private_api(0), 'JPY'))
    print(ACCOUNTINFORMATION.get_cryptocurrency_balance(ACCOUNTINFORMATION.get_private_api(0), 'XRP'))
    print(ACCOUNTINFORMATION.get_cryptocurrency_balance(ACCOUNTINFORMATION.get_private_api(0), 'BTC'))
