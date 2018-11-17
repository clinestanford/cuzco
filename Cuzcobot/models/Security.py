from django.db import models

from Cuzcobot.models import Price

class Security(models.Model):
    tickerSymbol = models.CharField(max_length=6, verbose_name='Security Ticker Symbol')

    @property
    def price(self):
        a = Price.objects.filter(ticker=self).latest('priceDate')
        return a.current
