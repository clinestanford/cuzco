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
		currentSpread = max(price1, price2) - min(price1 - price2)

		if currentSpread > averageSpread * pair.spreadHigh :
			#buy the security that is low, and sell the high

		if currentSpread < averageSpread * pair.spreadLow :
			#sell the lower and buy the higher



