from django.db import models
from typing import Tuple
from statsmodels.tsa.stattools import coint

class Pair(models.Model):
    ticker1 = models.ForeignKey('Cuzcobot.Security', on_delete=models.PROTECT)
    ticker2 = models.ForeignKey('Cuzcobot.Security', on_delete=models.PROTECT, related_name='secondSecurity')
    window = models.DecimalField(max_digits=4,decimal_places=0)

    @property
    def is_coIntegrated(self):
        return True