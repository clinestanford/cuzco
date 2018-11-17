from django.db import models

class Financials(models.Model):
    ticker = models.ForeignKey('Cuzcobot.Security', models.PROTECT)
    reportDate = models.DateTimeField()
    grossProfit = models.BigIntegerField()
    costOfRevenue = models.BigIntegerField()
    operatingRevenue = models.BigIntegerField()
    totalRevenue = models.BigIntegerField()
    operatingIncome = models.BigIntegerField()
    netIncome = models.BigIntegerField()
    researchDevelopment = models.BigIntegerField()
    operatingExpense = models.BigIntegerField()
    currentAssets = models.BigIntegerField()
    totalAssets = models.BigIntegerField()
    totalLiabilities = models.BigIntegerField()
    currentCash = models.BigIntegerField()
    currentDebt = models.BigIntegerField()
    totalCash = models.BigIntegerField()
    totalDebt = models.BigIntegerField()
    shareholderEquity = models.BigIntegerField()
    cashChange = models.BigIntegerField()
    cashFlow = models.BigIntegerField()
    operatingGainsLosses = models.BigIntegerField()

    def getCurrentRatio(self):
        return self.totalAssets * 100 / self.totalLiabilities

    def getProfitability(self) -> float:
        return self.netIncome * 100 / self.costOfRevenue

    def getReportDate(self):
        return self.reportDate

    def getGrossProfit(self) -> int:
        return self.grossProfit

    def getTotalCash(self):
        return self.totalCash

    def getTotalDebt(self):
        return self.totalDebt