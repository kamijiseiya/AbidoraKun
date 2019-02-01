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

            print('XRPをbitbankで買いbinancesに売った場合の利益(btc):')
            print(profit_bitbank_binance)
            print('XRPをbinancesで買いbitbankに売った場合の利益(btc):')
            print(profit_binance_bitbank)
            print('XRPをbitbankで買いcoinexに売った場合の利益(btc)')
            print(profit_bitbank_coinex)
            print('XRPをcoinexで買いbitbankに売った場合の利益(btc)')
            print(profit_coinex_bitbank)
            print('XRPをbinanceで買いcoinexに売った場合の利益(btc)')
            print(profit_binance_coinex)
            print('XRPをcoinexで買いbinanceに売った場合の利益(btc)')
            print(profit_coinex_binance)
            print('XRPを取引した場合の最大利益(btc):')
            print(max([profit_bitbank_binance, profit_binance_bitbank, profit_bitbank_coinex,
                       profit_coinex_bitbank, profit_binance_coinex, profit_coinex_binance]))
            print('XRPを取引した場合の最低利益(btc):')
            print(min([profit_bitbank_binance, profit_binance_bitbank, profit_bitbank_coinex,
                       profit_coinex_bitbank, profit_binance_coinex, profit_coinex_binance]))

            return profit_bitbank_binance, profit_binance_bitbank, profit_bitbank_coinex, \
                   profit_coinex_bitbank, profit_binance_coinex, profit_coinex_binance
        except ccxt.BaseError:
            print("取引所から取引データを取得できません。")
            print("10秒待機してやり直します")
            time.sleep(10)



if __name__ == "__main__":
    print(CALCULATION.difference_xrp(""))