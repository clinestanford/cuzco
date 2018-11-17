import alpaca_trade_api as tradeapi

import requests
import matplotlib.pyplot as plt
import numpy as np
import alpaca_trade_api as tradeapi
import json
import _json
import logging

#Alpacas' Live APi domain is 'https://api.alpaca.markets'
#Alpacas' paper trading api domain is 'https://paper-api.alpaca.markets'

api = tradeapi.REST('AKHJ8PWF3ZFFY80RTHSZ','NWfbVkeAbR95F/2hWaMJWmx/GRk9xf8U2BVOBNEB')
account = api.get_account()


    
    #Below Are functions Dealing with Accounts

def getAccountCash():
    print('api.get_account().cash')
    return api.get_account().cash #string<number>

def getAccountComplete():
    print('api.get_account()')
    return api.get_account #JSON OBJECT

def getAccountPower():
    print('api.get_account().buying_power')
    return api.get_account().buying_power #string<number>

def getAccountPortValue():
    print('api.get_account().portfolio_value')
    return api.get_account().portfolio_value #string<number>

def getAccountStatus():
    print('api.get_account().status')
    return api.get_account().status #string<account_status>




    #Below Are Functions Dealing with orders

#def trade(
#
#def executeOrder(symbol, qty, side, type, time_in_force, limit_price, stop_price, client_order_id):
#    
#    trade(get_orders(api, price_map, position_size=100, max_positions = 5, wait):
#
#


#Function will retrieve a list of orders on the account. Filter by query paramaters
def getOrderList(status, limit, after, until, direction):
    return api.get_order(status, limit, after, until, direction)


#
# get an order object based on order ID
#
#@params:
#order_id - the id of the order
def getOrder(order_id):
    order_data = {'(api.get_order(order_id)'}
    print(order_data)
    return order_data


#
#create and execute single order
#
#@params:
#symbol - REQUIRED - symbol or asset ID to identify the asset to trade
#qty - REQUIRED - number of shares to trade
#type - REQUIRED - market, limit, stop, or stop limit order
#time_in_force - REQUIRED - day, gtc, opg, ioc, fok
#limit_price - REQUIRED IF LIMIT - set limit price
#stop_price - REQUIRED IF STOP OR STOP LIMIT - set stop limit price
#client_order_id - if no paramater is passed this will autogenerate. 
def executeOrder(symbol, qty, side, type, time_in_force, limit_price, stop_price, client_order_id = ''):
    try:
        logger.info(f'submit(sell/buy): {order}')
        tempOrder = api.submit_order(symbol, qty, side, type, time_in_force, limit_price, stop_price, client_order_id)
    except Exception as e:
        logger.error(e)
    count = wait
    while count > 0:
        pending = api.list_orders()
        if len(pending) == 0:
            logger.info(f'Buy order complete')
            return tempOrder
        logger.info(f'{len(pending)} Order in progress')
        time.sleep(1)
        count -=1

    if (count == 0 & len(pending != 0)):
        logger.info(f'Order failed to execute')        
    

#
#executes a list of sell and buy orders at market
#
#@params:
#orders - a JSON/List object of order objects
def executeOrders(orders, wait=30):
    #proccess sell orders first
    sells = [o for o in orders if o['side'] =='sell']
    for order in sells:
        try:
           logger.info(f'submit(sell): {order}')
           api.submit_order(
               symbol = order['symbol'],
               qty = order['qty'],
               side = 'sell',
               type = 'market',
               time_in_force='day',
           )

        except Exception as e:
            logger.error(e)
    count = wait
    while count > 0:
        pending = api.list_orders()
        if len(pending) == 0:
            logger.info(f'all sell orders done')
            break
        logger.info(f'{len(pending)} sell orders still selling')
        time.sleep(1)
        count -= 1

    #
    #Proccess Buy Orders
    #
    buys = [o for o in orders if object['side'] == 'buy']
    for order in buys:
        try:
            logger.info(f'submit(buy): {order}')
            api.submit_order(
                symbol=order['symbol'],
                qty=order['qty'],
                side='buy',
                type='market',
                time_in_force='day',
            )
        except Exception as e:
            logger.error(e)
    count = wait
    while count >0:
        pending = api.list_orders()
        if len(pending) == 0:
            logger.info(f'all buy orders done')
            break
        logger.info(f'{len(pending)} still buying orders')
        time.sleep(1)
        count -=1


def main():
    account = api.get_account()
    api.list_positions()
    print(api.get_account().cash)
