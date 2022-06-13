from binance_api import Binance
bot = Binance(
    API_KEY='Your key',
    API_SECRET='Your secret key'
)
print('account', bot.account())
