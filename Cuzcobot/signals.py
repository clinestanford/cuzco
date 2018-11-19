from Cuzcobot.models import Order
from Cuzcobot.dataAPI.Client import api
import time, logging

def executeOrder(sender, instance:Order, created, **kwargs):
    if created:
        try:
            # logger.info(f'submit(sell/buy): {order}')
            tempOrder = api.submit_order(instance.ticker.tickerSymbol, instance.shares, instance.getOrderDirection(), instance.orderType, time_in_force=instance.getTimeInForce())
            count = 30
            while count > 0:
                pending = api.list_orders()
                if len(pending) == 0:
                    instance.orderStatus = 'FIL'
                    instance.exchange = tempOrder['exchange']
                    instance.save()
                # logger.info(f'{len(pending)} Order in progress')
                time.sleep(1)
                count -= 1
        except Exception as e:
            logging.error(e)