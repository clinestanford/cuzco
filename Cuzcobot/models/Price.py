from django.db import models

class Price(models.Model):
    ticker = models.ForeignKey('Cuzcobot.Security', on_delete=models.PROTECT)
    priceDate = models.DateTimeField(auto_now_add=True)
    open = models.DecimalField(max_digits=16, decimal_places=3)
    current = models.DecimalField(max_digits=16, decimal_places=3, blank=True, null=True)
    close = models.DecimalField(max_digits=16, decimal_places=3)
    high = models.DecimalField(max_digits=16, decimal_places=3)
    low = models.DecimalField(max_digits=16, decimal_places=3)
    volume = models.BigIntegerField()

