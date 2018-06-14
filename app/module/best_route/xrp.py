from app.module.exchangess import bitbank, binance

ask_exhange = ''
bid_exhange = ''
ask_price = 0
bid_price = 0
bitbank, bitbank_ask, bitbank_bid = bitbank.BITBANK.currencyinformation('XRP')
binance, binance_ask, binance_bid = binance.BINANCE.xrp(0)


def ask():
    if bitbank_ask > binance_ask:
        ask_price = binance_ask
        ask_exhange = 'binance'
        print(ask_exhange, ask_price, '取引A')
    else:
        ask_price = bitbank_ask
        ask_exhange = 'bitbank'
        print(ask_exhange, ask_price, '取引B')


def bid():
    if bitbank_bid > binance_bid:
        bid_price = bitbank_bid
        bid_exhange = 'bitbank'
        print(bid_exhange, bid_price, '取引A')
    else:
        bid_price = binance_bid
        bid_exhange = 'binance'
        print(bid_exhange, bid_price, '取引B')


if __name__ == "__main__":  # テスト用に追加
    print('最安値' + ask())
    print('最高値' + bid())
