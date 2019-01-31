import json
import ccxt

class CALCULATION:
    """取引所間の通貨差額を求めるクラス"""

    def difference_xrp(self):
        
        bitbanks = ccxt.bitbank()
        bitbank_btc_jpy = bitbanks.fetch_ticker('BTC/JPY')
        bitbank_xrp_jpy = bitbanks.fetch_ticker('XRP/JPY')
        bitbank_xrp_btc_ask = bitbank_xrp_jpy.get("bid") / bitbank_btc_jpy.get("ask")
        bitbank_xrp_btc_bid = bitbank_xrp_jpy.get("ask") / bitbank_btc_jpy.get("bid")
        binances = ccxt.binance()
        binance_xrp_btc = binances.fetch_ticker('XRP/BTC')
        profit_bitbank = bitbank_xrp_btc_ask - binance_xrp_btc.get("bid")
        profit_binance = binance_xrp_btc.get("ask") - bitbank_xrp_btc_bid

        print('XRPをbitbankで買いbinancesに売った場合の利益(btc):')
        print(profit_bitbank)
        print('XRPをbinancesで買いbitbankに売った場合の利益(btc):')
        print(profit_binance)
        return profit_bitbank, profit_binance


if __name__ == "__main__":
    print(CALCULATION.bitbank_binances_xrp(""))