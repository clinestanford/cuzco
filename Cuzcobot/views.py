from django.shortcuts import render

from .models import Pairs


# Create your views here.

def pairs(request):

	pairs = Pairs.objects.all()

	for pair in pairs:
		avgPrice1, avgPrice2 = pair.getAveragePriceDiff()
		price1 = pair.ticker1.price()
		price2 = pair.ticker2.price()

		averageSpread = max(avgPrice1, avgPrice2) - min(avgPrice1, avgPrice2)
		currentSpread = max(price1, price2) - min(price1, price2)

		if currentSpread > averageSpread * pair.spreadHigh:
			#buy the security that is low, and sell the high
			if pair.ticker1.currentPositionShares >= 1:
				#sell ticker 1, buy ticker 2

			elif pair.ticker2.currentPositionShares >= 1:
				#sell ticker 2, buy ticker 1

			else:
				#buy the "lower" of the two 


		if currentSpread < averageSpread * pair.spreadLow:
			#sell the lower and buy the higher
			if pair.ticker1.currentPositionShares >= 1:
				#sell ticker 1, buy ticker 2

			elif pair.ticker2.currentPositionShares >= 1:
				#sell ticker 2, buy ticker 1

			else:
				# buy the "higher" of the two



