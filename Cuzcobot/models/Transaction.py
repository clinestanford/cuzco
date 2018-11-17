from django.db import models

TRADESTATUS = [
    ("In-Transit", 'IT'),
    ("Executed", 'E'),
    ("Failed", 'F')
]

class Transaction(models.Model):
    transactionDate = models.DateTimeField(auto_now_add=True)
    ticker = models.ForeignKey('Cuzcobot.Security', models.PROTECT)
    # shares that are negative are short
    shares = models.IntegerField()
    pricePerShare = models.DecimalField(max_digits=16, decimal_places=2)
    tradeStatus = models.CharField(choices=TRADESTATUS, max_length=1)

    @property
    def tradeValue(self):
        a = self.shares * self.pricePerShare
        return float("{0:.2f}".format(a))
