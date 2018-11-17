
import pandas as pd
from statsmodels.tsa.stattools import coint
from typing import Tuple


# Checks for itnegration between two entities
# Return: bool (are entities cointegrated) float (p_value)
def check_cointegration(v1: list, v2: list) -> Tuple[bool, float]:
	# Date indexed pricing data for stickers
	p_value = coint(v1, v2)[1]
	if p_value < 0.02:
		return True, p_value
	else: 
		return False, p_value



df = pd.read_csv("cointegration.txt")

eth = df["ETH_USD"].tolist()
btc = df["BTC_USD"].tolist()

val = check_cointegration(eth[40:], btc[40:])
#val = check_cointegration(eth, btc)

print("Cointegrated status: ", val[0])
print("p_value: ", val[1])

