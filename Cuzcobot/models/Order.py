from django.db import models

ASSETCLASSES = [
    ("equity", "E"),
    ("option", "O"),
    ("future", "F"),
    ("commodity", "C")
]

ORDERTYPES = [
    ("Market Order", "MKT"),
    ("Limit Order", "LMT"),
    ("Stop Order", "STP"),
    ("Stop Limit Order", "SLT")

]

TIMEINFORCE = [
    ("Day", 'D'),
    ("Good Till Canceled", "G"),
    ("At Market Open", 'O'),
    ("Immediate or Cancel Partial", 'I'),
    ("Immediate or Cancel Full", 'F')
]

DIRECTIONS =[
    ("Buy", "B"),
    ("Sell", "S")
]

ORDERSTATUS = [
    ("New", 'NEW'),
    ("Partial Fill", 'PAR'),
    ("Filled", 'FIL'),
    ("Done For Day", 'DFD'),
    ("Canceled", 'CAN'),
    ("Expired", "EXP"),
    ("Accepted", "ACP"),
    ("Pending At Exchange", "PAE"),
    ("Pending Cancelation", 'PC'),
    ("Stopped", 'STP'),
    ("Rejected", 'RCT'),
    ("Suspended", 'SUS'),
    ("Calculated", 'CAL')
]

class Order(models.Model):
    orderID = models.CharField(max_length=200, primary_key=True)
    creationDate = models.DateTimeField(auto_now_add=True)
    submissionDate = models.DateTimeField(auto_now_add=True)
    expirationDate = models.DateTimeField(blank=True, null=True)
    cancelationDate = models.DateTimeField(blank=True, null=True)
    failedDate = models.DateTimeField(blank=True, null=True)
    ticker = models.ForeignKey('Cuzcobot.Security', models.PROTECT)
    exchange = models.CharField(max_length=15)
    assetClass = models.CharField(choices=ASSETCLASSES, max_length=1)
    shares = models.IntegerField()
    filledShares = models.IntegerField()
    orderType = models.CharField(choices=ORDERTYPES, max_length=3)
    orderDirection = models.CharField(choices=DIRECTIONS, max_length=1)
    timeInForce = models.CharField(choices=TIMEINFORCE, max_length=1)
    limitPrice = models.DecimalField(max_digits=15, decimal_places=2)
    stopPrice = models.DecimalField(max_digits=15, decimal_places=2)
    filledAvgPrice = models.DecimalField(max_digits=15, decimal_places=2)
    orderStatus = models.CharField(choices=ORDERSTATUS, max_length=3)

    @property
    def availableToCancel(self):
        if self.orderStatus == 'FIL':
            return False
        elif self.orderStatus == 'CAN':
            return False
        elif self.orderStatus == 'EXP':
            return False
        else:
            return True
