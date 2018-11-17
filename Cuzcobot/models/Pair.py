from typing import Tuple, List
from django.db import models
from statsmodels.tsa.stattools import coint
import numpy as np
import datetime

class Pair(models.Model):
    ticker1 = models.ForeignKey('Cuzcobot.Security', on_delete=models.PROTECT)
    ticker2 = models.ForeignKey('Cuzcobot.Security', on_delete=models.PROTECT, related_name='secondSecurity')
    window = models.DecimalField(max_digits=4, decimal_places=0)
    spreadHigh = models.DecimalField(max_digits=5, decimal_places=4)
    spreadLow = models.DecimalField(max_digits=5, decimal_places=4)

    def checkCointegration(self) -> Tuple[bool, float]:
        data1 = self.retrieveData(self.ticker1)
        data2 = self.retrieveData(self.ticker2)

        p_value = coint(data1, data2)

        if p_value < 0.05:
            return (True, p_value)
        else:
            return (False, p_value)

    # ToDo: return type?
    def retrieveData(self, ticker: str):
        today = datetime.datetime.today()
        delta = datetime.delta(days=self.window)
        oldestDate = today - delta
        data = Prices.objects.filter(ticker=ticker, priceData_gte=oldestData).close
        

    @property
    def isCointegrated(self):
        is_coint_bool, p_value = self.checkCointegration()


    @property
    def getAveragePrices(self) -> Tuple[float, float]:
        today = datetime.datetime.today()
        delta = datetime.delta(days=self.window)
        oldestDate = today - delta
        tick1Avg = Prices.objects.filter(ticker=self.ticker1, priceDate__gte=oldestDate).Aggregate(Avg('close'))["avg__close"]
        tick2Avg = Prices.objects.filter(ticker=self.ticker2, priceDate__gte=oldestDate).Aggregate(Avg('close'))["avg__close"]
    
        return tick1Avg, tick2Avg
