from django.shortcuts import render

from .models import Pairs


# Create your views here.

def pairs(request):

	pairs = Pairs.objects.all()

	for pair in pairs:
		avgPrice1, avgPrice2 = pair.getAveragePrices()
		price1 = pair.ticker1.price()
		price2 = pair.ticker2.price()

		averageSpread = max(avgPrice1, avgPrice2) - min(avgPrice1, avgPrice2)
		currentSpread = max(price1, price2) - min(price1, price2)

		if currentSpread > averageSpread * pair.spreadHigh:
			#buy the security that is low, and sell the high
			if pair.ticker1.currentPositionShares >= 1:
				#sell ticker 1, buy ticker 2
				if price1/avgPrice1 > price2/avgPrice2:
					#sell ticker 1
					#buy ticker 2
					#pass

				else:
					#the percentage over price1 is lower than
					#price 2, which means we should probably 
					#hang onto it
					pass

			elif pair.ticker2.currentPositionShares >= 1:
				#sell ticker 2, buy ticker 1
				if price2/avgPrice2 > price1/avgPrice1:
					#sell ticker2
					#buy ticker1
					#pass

				else:
					#hang out for a bit, we own ticker2, 
					#but the average price2 is lower than 
					#average price1, so hang onto it
                pass

			else:
				#buy the "lower" of the two 

				if price1/avgPrice1 > price2/avgPrice2:
					#buy ticker2
					#do nothing with ticker1
				else:
					#buy ticker1
					#do nothing with ticker2


		if currentSpread < averageSpread * pair.spreadLow:
			#sell the lower and buy the higher
			if pair.ticker1.currentPositionShares >= 1:
				#sell ticker 1, buy ticker 2
				if price1/avgPrice1 > price2/avgPrice2:
					#sell ticker1
					#buy ticker2
					#pass
				else:
					#do nothing

			elif pair.ticker2.currentPositionShares >= 1:
				#sell ticker 2, buy ticker 1
				if price2/avgPrice2 > price1/avgPrice1:
					#sell ticker2
					#buy ticker1
					#pass
				else:
					#do nothing

			else:
				# buy the "higher" of the two
				if price1/avgPrice1 > price2/avgPrice2:
					#buy ticker2

				else:
					#buy ticker1



