from django.db import models
from statsmodels.tsa.stattools import coint


import numpy as np

class Pair(models.Model):
	ticker1 = models.CharField(max_length=8)
	ticker2 = models.CharField(max_length=8)
	window = models.DecimalField(max_digits=4)

	#checks if the two pairs are still cointegrated for the last window frame
	def check_cointegration(self, v1: list, v2: list) -> Tuple[bool, float]:
		# Date indexed pricing data for stickers
		p_value = coint(v1, v2)[1]
		if p_value < 0.05:
			return (True, p_value)
		else: 
			return (False, p_value)


	def get_data(self, name):
		#need to use the self.window value to return the right amount of data
		

		return 

	@property
	def is_cointegrated(self):
		data1 = get_data(self.ticker1)
		data2 = get_data(self.ticker2)

		is_coint_bool, p_value = self.check_cointegration(data1, data2)

		return is_coint_bool


