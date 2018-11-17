from typing import Tuple

from django.db import models
from statsmodels.tsa.stattools import coint


class Pair(models.Model):
    ticker1 = models.ForeignKey('Cuzcobot.Security', on_delete=models.PROTECT)
    ticker2 = models.ForeignKey('Cuzcobot.Security', on_delete=models.PROTECT, related_name='secondSecurity')
    window = models.DecimalField(max_digits=4, decimal_places=0)

    def check_cointegration(self, v1: list, v2: list) -> Tuple[bool, float]:
        p_value = coint(v1, v2)
        if p_value < 0.05:
            return (True, p_value)
        else:
            return (False, p_value)

    def get_data(self, name):
        pass

    @property
    def is_cointegrated(self):
        data1 = self.get_data(self.ticker1)
        data2 = self.get_data(self.ticker2)

        is_coint_bool, p_value = self.check_cointegration(data1, data2)

        return is_coint_bool
