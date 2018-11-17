from django.db import models
from django.db.models import Sum

from urllib import parse
import requests

from Cuzcobot.models import Price, Transaction


class Security(models.Model):
    tickerSymbol = models.CharField(max_length=6, verbose_name='Security Ticker Symbol')
    sharesOwned = models.IntegerField()

    def __str__(self):
        return str(self.tickerSymbol)
    

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

    @property
    def marketPrice(self):
        urlRequest = 'https://api.iextrading.com/1.0/stock/' + self.tickerSymbol + '/price'
        parse.quote_plus(urlRequest)
        price = requests.get(url=urlRequest).json()['price']
        return price



Security.objects.all().values()


