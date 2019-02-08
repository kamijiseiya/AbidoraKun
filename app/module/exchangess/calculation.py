import time
import ccxt
import json

class CALCULATION:
    """取引所間の通貨差額を求めるクラス"""

    def difference_xrp_btc(self):
        """取引所間でのxrp差額を求めるメソッド
                    (bitbank,binance,coinex)"""
        while True:
            try:
                bitbanks = ccxt.bitbank()
                bitbank_btc_jpy = bitbanks.fetch_ticker('BTC/JPY')
                bitbank_xrp_jpy = bitbanks.fetch_ticker('XRP/JPY')
                bitbank_xrp_btc_bid = bitbank_xrp_jpy.get("bid") / bitbank_btc_jpy.get("ask")
                bitbank_xrp_btc_ask = bitbank_xrp_jpy.get("ask") / bitbank_btc_jpy.get("bid")

                # binanceからXRP/BTC通貨情報取得
                binances = ccxt.binance()
                binance_xrp_btc = binances.fetch_ticker('XRP/BTC')

                # coinexからXRP/BTC通貨情報取得
                coinex = ccxt.coinex()
                coinex_xrp_btc = coinex.fetch_ticker('XRP/BTC')

                # bitbankとbinance間の差額
                profit_bitbank_binance = binance_xrp_btc.get("bid") - bitbank_xrp_btc_ask
                profit_binance_bitbank = bitbank_xrp_btc_bid - binance_xrp_btc.get("ask")

                # bitbankとcoinex間の差額
                profit_bitbank_coinex = coinex_xrp_btc.get("bid") - bitbank_xrp_btc_ask
                profit_coinex_bitbank = bitbank_xrp_btc_bid - coinex_xrp_btc.get("ask")

                # binanceとcoinex間の差額
                profit_binance_coinex = coinex_xrp_btc.get("bid") - binance_xrp_btc.get("ask")
                profit_coinex_binance = binance_xrp_btc.get("bid") - coinex_xrp_btc.get("ask")

                #'XRPを取引した場合の最大利益(btc):'
                maxvalue = max([profit_bitbank_binance, profit_binance_bitbank, profit_bitbank_coinex,
                                profit_coinex_bitbank, profit_binance_coinex, profit_coinex_binance])
                #'XRPを取引した場合の最低利益(btc):'
                minvalue = min([profit_bitbank_binance, profit_binance_bitbank, profit_bitbank_coinex,
                                profit_coinex_bitbank, profit_binance_coinex, profit_coinex_binance])

                resultarray = {'bitbank_binance': profit_bitbank_binance,
                               'binance_bitbank': profit_binance_bitbank,
                               'bitbank_coinex': profit_bitbank_coinex,
                               'coinex_bitbank': profit_coinex_bitbank,
                               'binance_coinex': profit_binance_coinex,
                               'coinex_binance' : profit_coinex_binance,
                               'max':maxvalue, 'min': minvalue}
                return resultarray
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)

    def difference_btc_xrp(self):
        """取引所間でのBTC差額を求めるメソッド
                    (bitbank,binance,coinex)"""
        while True:
            try:
                bitbanks = ccxt.bitbank()
                bitbank_btc_jpy = bitbanks.fetch_ticker('BTC/JPY')
                bitbank_xrp_jpy = bitbanks.fetch_ticker('XRP/JPY')
                bitbank_btc_xrp_bid = (1 / bitbank_xrp_jpy.get("bid")) / (1 / bitbank_btc_jpy.get("ask"))
                bitbank_btc_xrp_ask = (1 / bitbank_xrp_jpy.get("ask")) / (1 / bitbank_btc_jpy.get("bid"))
                print(bitbank_btc_xrp_ask)
                print(bitbank_btc_xrp_bid)
                # binanceからXRP/BTC通貨情報取得
                binances = ccxt.binance()
                binance_xrp_btc = binances.fetch_ticker('XRP/BTC')
                print(binance_xrp_btc.get("ask"))
                binance_xrp_btc_ask = (1 / binance_xrp_btc.get("ask"))
                print(binance_xrp_btc.get("bid"))
                binance_xrp_btc_bid = (1 / binance_xrp_btc.get("bid"))

                # coinexからXRP/BTC通貨情報取得
                coinex = ccxt.coinex()
                coinex_xrp_btc = coinex.fetch_ticker('XRP/BTC')
                print(coinex_xrp_btc.get("ask"))
                coinex_xrp_btc_ask = (1 / coinex_xrp_btc.get("ask"))
                print(coinex_xrp_btc.get("bid"))
                coinex_xrp_btc_bid = (1 / coinex_xrp_btc.get("bid"))

                # bitbankとbinance間の差額
                profit_bitbank_binance = (binance_xrp_btc_bid - bitbank_btc_xrp_ask) * bitbank_xrp_jpy.get(
                    "bid")
                profit_binance_bitbank = (bitbank_btc_xrp_bid - binance_xrp_btc_ask) * bitbank_xrp_jpy.get(
                    "bid")

                # bitbankとcoinex間の差額
                profit_bitbank_coinex = (coinex_xrp_btc_bid - bitbank_btc_xrp_ask) * bitbank_xrp_jpy.get(
                    "bid")
                profit_coinex_bitbank = (bitbank_btc_xrp_bid - coinex_xrp_btc_ask) * bitbank_xrp_jpy.get(
                    "bid")

                # binanceとcoinex間の差額
                profit_binance_coinex = (coinex_xrp_btc_bid - (binance_xrp_btc_ask)) * bitbank_xrp_jpy.get("bid")
                profit_coinex_binance = (binance_xrp_btc_bid - (coinex_xrp_btc_ask)) * bitbank_xrp_jpy.get("bid")

                resultsample = {'bitbank_binance': profit_bitbank_binance,
                                'binance_bitbank': profit_binance_bitbank,
                                'bitbank_coinex': profit_bitbank_coinex,
                                'coinex_bitbank': profit_coinex_bitbank,
                                'binance_coinex': profit_binance_coinex,
                                'coinex_binance': profit_coinex_binance}
                max_k = max(resultsample, key=resultsample.get)
                print(max_k)
                min_k = min(resultsample, key=resultsample.get)
                print(min_k)

                # 最大利益が出る取引所からいくら購入したのか
                if max_k.startswith('bitbank'):
                    price_buy = bitbank_btc_xrp_ask
                elif max_k.startswith('binans'):
                    price_buy = binance_xrp_btc_ask
                elif max_k.startswith('coinex'):
                    price_buy = coinex_xrp_btc_ask
                else:
                    price_buy = 0

                # 最大利益が出る取引所からいくら売ったのか
                if max_k.endswith('bitbank'):
                    price_sale = bitbank_btc_xrp_bid
                elif max_k.endswith('binans'):
                    price_sale = binance_xrp_btc_bid
                elif max_k.endswith('coinex'):
                        price_sale = coinex_xrp_btc_bid
                else:
                    price_sale = 0

                # 'BTCを取引した場合の最大利益(jpy):'
                maxvalue = max([profit_bitbank_binance, profit_binance_bitbank, profit_bitbank_coinex,
                                profit_coinex_bitbank, profit_binance_coinex, profit_coinex_binance])
                # 'BTCを取引した場合の最低利益(jpy):'
                minvalue = min([profit_bitbank_binance, profit_binance_bitbank, profit_bitbank_coinex,
                                profit_coinex_bitbank, profit_binance_coinex, profit_coinex_binance])

                resultarray = {'bitbank_binance': profit_bitbank_binance,
                               'binance_bitbank': profit_binance_bitbank,
                               'bitbank_coinex': profit_bitbank_coinex,
                               'coinex_bitbank': profit_coinex_bitbank,
                               'binance_coinex': profit_binance_coinex,
                               'coinex_binance': profit_coinex_binance,
                               'max': max_k, 'min': min_k,
                               'maxvalue': maxvalue, 'minvalue': minvalue,
                               'max_buy': price_buy, 'min_sale': price_sale

                               }
                return resultarray
            except ccxt.BaseError:
                print("取引所から取引データを取得できません。")
                print("10秒待機してやり直します")
                time.sleep(10)



if __name__ == "__main__":
    #print(CALCULATION.difference_xrp(""))
    #print("%.13f" % CALCULATION.difference_xrp("")['max'])
    print(CALCULATION.difference_btc_xrp(1))
    print(CALCULATION.difference_btc_xrp(3))