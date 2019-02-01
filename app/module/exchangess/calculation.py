import time
import ccxt

class CALCULATION:
    """取引所間の通貨差額を求めるクラス"""

    def difference_xrp(self):
        """取引所間でのxrp差額を求めるメソッド
                    (bitbank,binance,coinex)"""
        # bitbankのXRP/BTCのaskとbidを算出
        try:
            bitbanks = ccxt.bitbank()
            bitbank_btc_jpy = bitbanks.fetch_ticker('BTC/JPY')
            bitbank_xrp_jpy = bitbanks.fetch_ticker('XRP/JPY')
            bitbank_xrp_btc_ask = bitbank_xrp_jpy.get("bid") / bitbank_btc_jpy.get("ask")
            bitbank_xrp_btc_bid = bitbank_xrp_jpy.get("ask") / bitbank_btc_jpy.get("bid")

            # binanceからXRP/BTC通貨情報取得
            binances = ccxt.binance()
            binance_xrp_btc = binances.fetch_ticker('XRP/BTC')

            # coinexからXRP/BTC通貨情報取得
            coinex = ccxt.coinex()
            coinex_xrp_btc = coinex.fetch_ticker('XRP/BTC')
            print(coinex_xrp_btc.get("bid"))
            print(coinex_xrp_btc.get("ask"))

            # bitbankとbinance間の差額
            profit_bitbank_binance = bitbank_xrp_btc_ask - binance_xrp_btc.get("bid")
            profit_binance_bitbank = binance_xrp_btc.get("ask") - bitbank_xrp_btc_bid

            # bitbankとcoinex間の差額
            profit_bitbank_coinex = bitbank_xrp_btc_ask - coinex_xrp_btc.get("bid")
            profit_coinex_bitbank = coinex_xrp_btc.get("ask") - bitbank_xrp_btc_bid

            # binanceとcoinex間の差額
            profit_binance_coinex = binance_xrp_btc.get("ask") - coinex_xrp_btc.get("bid")
            profit_coinex_binance = coinex_xrp_btc.get("ask") - binance_xrp_btc.get("bid")

            print('XRPを取引した場合の最大利益(btc):')
            maxvalue = max([profit_bitbank_binance, profit_binance_bitbank, profit_bitbank_coinex,
                 profit_coinex_bitbank, profit_binance_coinex, profit_coinex_binance])
            print(maxvalue)
            print('XRPを取引した場合の最低利益(btc):')
            minvalue = min([profit_bitbank_binance, profit_binance_bitbank, profit_bitbank_coinex,
                       profit_coinex_bitbank, profit_binance_coinex, profit_coinex_binance])
            print(minvalue)

            resultarray = {'bitbank_binance': profit_bitbank_binance, 'binance_bitbank': profit_binance_bitbank,
                           'bitbank_coinex': profit_bitbank_coinex, 'coinex_bitbank': profit_coinex_bitbank,
                           'binance_coinex': profit_binance_coinex, 'coinex_binance' : profit_coinex_binance,
                           'max':maxvalue, 'min': minvalue}
            return resultarray
        except ccxt.BaseError:
            print("取引所から取引データを取得できません。")
            print("10秒待機してやり直します")
            time.sleep(10)



if __name__ == "__main__":
    print(CALCULATION.difference_xrp(""))
    print(CALCULATION.difference_xrp("")['max'])