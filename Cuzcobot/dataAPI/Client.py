import alpaca_trade_api as tradeapi
import os

api = tradeapi.REST(os.environ.get('APCA_PAPER_PUBLIC', 'AKCZ31SOGBRUUWIYKPWS'), os.environ.get('APCA_PAPER_PRIVATE','In9f9Xh3FB1jwkCnmcTqDqN/3qr30hqOsj8Ju2XT'))
account = api.get_account()