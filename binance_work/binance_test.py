from binance_api import Binance
bot = Binance(
    API_KEY='EpOYwkMe6ycDj7iwPpqPXzncZBvJsKe8vV78rZt1yso81ze8cXDsoYkIzNJ9w6uf',
    API_SECRET='bhzh0Apf74eNEmvjzMDsAt6TZfnFywDuaugkthLmVvMtedxHdt3RrAh7RpAYzQEF'
)
print('account', bot.account())