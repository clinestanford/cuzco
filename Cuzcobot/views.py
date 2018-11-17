from django.shortcuts import render

from .models import Pairs, ApplicationUser


# Create your views here.

def pairs(request):

	user = request.user

	buy = []
	sell = []

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
				if price1/avgPrice1 > price2/avgPrice2:
					#sell ticker 1
					#buy ticker 2
					#pass
					buy.append(pair.ticker2)
					sell.append(pair.ticker1)

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
					buy.append(pair.ticker1)
					sell.append(pair.ticker2)

				else:
					#hang out for a bit, we own ticker2, 
					#but the average price2 is lower than 
					#average price1, so hang onto it

			else:
				#buy the "lower" of the two 

				if price1/avgPrice1 > price2/avgPrice2:
					#buy ticker2
					#do nothing with ticker1
					buy.append(pair.ticker2)
				else:
					#buy ticker1
					#do nothing with ticker2
					buy.append(pair.ticker1)


		if currentSpread < averageSpread * pair.spreadLow:
			#sell the lower and buy the higher
			if pair.ticker1.currentPositionShares >= 1:
				#sell ticker 1, buy ticker 2
				if price1/avgPrice1 > price2/avgPrice2:
					#sell ticker1
					#buy ticker2
					#pass
					buy.append(pair.ticker2)
					sell.append(pair.ticker1)
				else:
					#do nothing

			elif pair.ticker2.currentPositionShares >= 1:
				#sell ticker 2, buy ticker 1
				if price2/avgPrice2 > price1/avgPrice1:
					#sell ticker2
					#buy ticker1
					#pass
					buy.append(pair.ticker1)
					sell.append(pair.ticker2)
				else:
					#do nothing

			else:
				# buy the "higher" of the two
				if price1/avgPrice1 > price2/avgPrice2:
					#buy ticker2
					buy.append(pair.ticker2)

				else:
					#buy ticker1
					buy.append(pair.ticker1)

	int i

	 
	#sell sec.tickerSymbol
	for sec in sell:

		

	cash = user.getBuyingPower()

	#if you want to mitigate risk, you can change the 
	#10 below to whatever portion you want. You may not want
	#to enter a position with more/less than 10% of buying power
	allocatedPercent = cash / 10


	#buy sec.tickerSymbol
	for sec in buy:
		price = sec.price()
		sharesToBuy = tenth // price
		if sharesToBuy >= 1:
			#buy sharesToBuy of sec.tickerSymbol


