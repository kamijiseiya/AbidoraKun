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


    def get_info(key):
        """口座残高の情報を返却する"""

        while True:
            try:
                balance = key.fetch_balance()  # keyから残高を取得
                print(key)
                jsonstring = json.dumps(balance, indent=4)
                print(jsonstring)
                return balance
            except ccxt.BaseError:
                print("口座情報を取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

    def get_data_assets(key):
        """資産情報を返却する"""

        while True:
            try:
                balance = key.fetch_balance()  # keyから残高を取得
                print(key)
                jsonstring = json.dumps(balance, indent=4)
                print(jsonstring)
                return balance['info']['data'].get('assets')
            except ccxt.BaseError:
                print("口座情報を取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

    def get_data_asserts_jpy(key):
        """JPYの資産情報を返却する"""

        while True:
            try:
                balance = key.fetch_balance()  # keyから残高を取得
                print(key)
                return balance['info']['data']['assets'][0]
            except ccxt.BaseError:
                print("口座情報を取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

    def get_data_asserts_btc(key):
        """BTCの資産情報を返却する"""

        while True:
            try:
                balance = key.fetch_balance()  # keyから残高を取得
                print(key)
                return balance['info']['data']['assets'][1]
            except ccxt.BaseError:
                print("口座情報を取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

    def get_data_asserts_xrp(key):
        """BTCの資産情報を返却する"""

        while True:
            try:
                balance = key.fetch_balance()  # keyから残高を取得
                print(key)
                return balance['info']['data']['assets'][3]
            except ccxt.BaseError:
                print("口座情報を取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)


    def get_jpy(key):
        """JPY(日本円)の口座情報を返す"""
        while True:
            try:
                balance = key.fetch_balance()  # keyから残高を取得
                return balance['JPY']
            except ccxt.BaseError:
                print("口座情報を取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

    def get_btc(key):
        """BTC(ビットコイン)の口座情報を返す"""
        while True:
            try:
                balance = key.fetch_balance()  # keyから残高を取得
                return balance['BTC']
            except ccxt.BaseError:
                print("口座情報を取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)


    def get_xrp(key):
        """XRP(リップル)の口座情報を返す"""
        while True:
            try:
                balance = key.fetch_balance()  # keyから残高を取得
                return balance['XRP']
            except ccxt.BaseError:
                print("口座情報を取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)


if __name__ == "__main__":  # テスト用
    print(ACCOUNTINFORMATION.get_info(ACCOUNTINFORMATION.get_private_api(0)))
    print(ACCOUNTINFORMATION.get_data_assets(ACCOUNTINFORMATION.get_private_api(0)))
    print(ACCOUNTINFORMATION.get_data_asserts_jpy(ACCOUNTINFORMATION.get_private_api(0)))
    print(ACCOUNTINFORMATION.get_data_asserts_btc(ACCOUNTINFORMATION.get_private_api(0)))
    print(ACCOUNTINFORMATION.get_data_asserts_xrp(ACCOUNTINFORMATION.get_private_api(0)))
    print(ACCOUNTINFORMATION.get_jpy(ACCOUNTINFORMATION.get_private_api(0)))
    print(ACCOUNTINFORMATION.get_btc(ACCOUNTINFORMATION.get_private_api(0)))
    print(ACCOUNTINFORMATION.get_xrp(ACCOUNTINFORMATION.get_private_api(0)))