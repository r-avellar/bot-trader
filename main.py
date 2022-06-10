from binance.client import Client
from binance.enums import *
from binance.exceptions import BinanceAPIException

from secrets import api_secret, api_key, api_key_test, secret_key_test
api = Client(api_key, api_secret)
#api = Client(api_key_test, secret_key_test, testnet=True)
info = api.get_account()
print(info)


print("################################## ANTES ###########################################")
lista_ativos = info["balances"]

# for ativo in lista_ativos:
#     if float(ativo["free"]) > 0:
#         print(ativo)

# ordem de venda
# order_sell = api.create_order(
#     symbol='BNBBTC',
#     side=SIDE_SELL,
#     type=ORDER_TYPE_MARKET,
#     quantity=1)

#ordem de compra
# order_buy = api.create_order(
#     symbol='ETHBTC',
#     side=SIDE_BUY,
#     type=ORDER_TYPE_MARKET,
#     quantity=1)

#print(order_buy)

print("################################## DEPOIS ###########################################")
# for ativo in lista_ativos:
#     if float(ativo["free"]) > 0:
#         print(ativo)

#ordens executadas e trades
# print(api.get_all_orders(symbol='BNBBTC'))
# print(api.get_my_trades(symbol='BNBBTC'))

#referencias de par de moedas
# print(api.get_symbol_info('BNBBTC'))

#cotações em tempo real
transactions = api.get_recent_trades(symbol="ADABUSD", limit=1)
print(transactions)