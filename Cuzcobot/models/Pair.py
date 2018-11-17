from django.db import models

class Pair(models.Model):
    ticker1 = models.CharField(max_length=8)
    ticker2 = models.CharField(max_length=8)
    window = models.DecimalField(max_digits=4)

    @property
    def is_coIntegrated(self):
        return True