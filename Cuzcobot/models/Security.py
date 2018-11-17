from django.db import models
from django.db.models import Sum

from Cuzcobot.models import Price, Transaction


class Security(models.Model):
    tickerSymbol = models.CharField(max_length=6, verbose_name='Security Ticker Symbol')
    sharesOwned = models.IntegerField()
    

    @property
    def price(self):
        a = Price.objects.filter(ticker=self).latest('priceDate')
        return a.current

    @property
    def currentPositionDollars(self):
        return Transaction.objects.filter(ticker=self.tickerSymbol).aggregate(Sum('tradeValue'))['tradeValue__Sum']

    @property
    def currentPositionShares(self):
        return Transaction.objects.filter(ticker=self.tickerSymbol).aggregate(Sum('shares'))['shares__Sum']


