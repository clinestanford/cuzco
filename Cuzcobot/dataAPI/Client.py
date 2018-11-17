import alpaca_trade_api as tradeapi
import os

api = tradeapi.REST(os.environ['APCA_PAPER_PUBLIC'], os.environ['APCA_PAPER_PRIVATE'])
account = api.get_account()