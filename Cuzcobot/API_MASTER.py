import alpaca_trade_api as tradeapi
import os
import requests
import json
import _json
import logging as logger
import http
import urllib.parse
import time


#Alpacas' Live APi domain is 'https://api.alpaca.markets'
#Alpacas' paper trading api domain is 'https://paper-api.alpaca.markets'

#Declare the deafualt api as the paper trading account by editing enviorment variable in aplaca_trade_api
os.environ["APCA_API_BASE_URL"] = "https://paper-api.alpaca.markets"
api = tradeapi.REST('AKCZ31SOGBRUUWIYKPWS','In9f9Xh3FB1jwkCnmcTqDqN/3qr30hqOsj8Ju2XT')
account = api.get_account()


#switch between 
def switchToRealTrading(choice):
    global api
    if choice == True:
        os.environ["APCA_API_BASE_URL"] = "https://api.alpaca.markets"
        api=tradeapi.REST('AKHJ8PWF3ZFFY80RTHSZ','NWfbVkeAbR95F/2hWaMJWmx/GRk9xf8U2BVOBNEB')
    if choice == False:
        os.environ["APCA_API_BASE_URL"] = "https://paper-api.alpaca.markets"
        api = tradeapi.REST('AKCZ31SOGBRUUWIYKPWS','In9f9Xh3FB1jwkCnmcTqDqN/3qr30hqOsj8Ju2XT')



    #Below Are functions Dealing with Accounts

def getAccountCash():
    print('api.get_account().cash')
    return api.get_account().cash #string<number>

def getAccountComplete():
    print('api.get_account()')
    return api.get_account #JSON OBJECT

def getAccountPower():
    print('api.get_account().buying_power')
    return api.get_account().buying_power #string<number>

def getAccountPortValue():
    print('api.get_account().portfolio_value')
    return api.get_account().portfolio_value #string<number>

def getAccountStatus():
    print('api.get_account().status')
    return api.get_account().status #string<account_status>




    #Below Are Functions Dealing with orders


#Function will retrieve a list of orders on the account. Filter by query paramaters
def getOrderList(status = 'open', limit = '50', direction = 'desc'):
    return api.get_order(status, limit, direction)



# get an order object based on order ID
#
#@params:
#order_id - the id of the order
def getOrder(order_id):
    order_data = {'(api.get_order(order_id)'}
    print(order_data)
    return order_data


#create and execute single order
#
#@params:
#symbol - REQUIRED - symbol or asset ID to identify the asset to trade
#qty - REQUIRED - number of shares to trade
#sid - 
#type - REQUIRED - market, limit, stop, or stop limit order
#time_in_force - REQUIRED - day, gtc, opg, ioc, fok
#limit_price - REQUIRED IF LIMIT - set limit price
#stop_price - REQUIRED IF STOP OR STOP LIMIT - set stop limit price
#client_order_id - if no paramater is passed this will autogenerate. 
def executeOrder(symbol, qty, side, type, limit_price = 'None', stop_price = 'None', timeInForce = 'day', client_order_id = ''):
    try:
        #logger.info(f'submit(sell/buy): {order}')
        tempOrder = api.submit_order(symbol, qty, side, type, time_in_force= 'day')
    except Exception as e:
        logger.error(e)
    count = 30
    while count > 0:
        pending = api.list_orders()
        if len(pending) == 0:
            logger.info(f'Buy order complete')
        #logger.info(f'{len(pending)} Order in progress')
        time.sleep(1)
        count -=1

    if (count == 0 & len(pending != 0)):
        logger.info(f'Order failed to execute')        
    

#
#executes a list of sell and buy orders at market
#
#@params:
#orders - a JSON/List object of order objects
def executeOrders(orders, wait=30):
    #proccess sell orders first
    sells = [o for o in orders if o['side'] =='sell']
    for order in sells:
        try:
           logger.info(f'submit(sell): {order}')
           api.submit_order(
               symbol = order['symbol'],
               qty = order['qty'],
               side = 'sell',
               type = 'market',
               time_in_force='day',
           )

        except Exception as e:
            logger.error(e)
    count = wait
    while count > 0:
        pending = api.list_orders()
        if len(pending) == 0:
            logger.info(f'all sell orders done')
            break
        logger.info(f'{len(pending)} sell orders still selling')
        time.sleep(1)
        count -= 1

    #
    #Proccess Buy Orders
    #
    buys = [o for o in orders if object['side'] == 'buy']
    for order in buys:
        try:
            logger.info(f'submit(buy): {order}')
            api.submit_order(
                symbol=order['symbol'],
                qty=order['qty'],
                side='buy',
                type='market',
                time_in_force='day',
            )
        except Exception as e:
            logger.error(e)
    count = wait
    while count >0:
        pending = api.list_orders()
        if len(pending) == 0:
            logger.info(f'all buy orders done')
            break
        logger.info(f'{len(pending)} still buying orders')
        time.sleep(1)
        count -=1


#
#POSITION FUNCTIONS
#
def getOpenPositions():
    return api.get_positions()
def getAnOpenPosition(ticker):
    return api.get_position(ticker)

#
#ASSET FUNCTIONS
#
def getAssets():
    return api.get_assets()
def getAsset(ticker):
    return api.get_asset(ticker)


#beginingBatchReq = 'https://api.iextrading.com/1.0/stock/market/batch?symbols='
#first100 = 'MMM,ABT,ABBV,ABMD,ACN,ATVI,ADBE,AMD,AAP,AES,AET,AMG,AFL,A,APD,AKAM,ALK,ALB,ARE,ALXN,ALGN,ALLE,AGN,ADS,LNT,ALL,GOOGL,GOOG,MO,AMZN,AEE,AAL,AEP,AXP,AIG,AMT,AWK,AMP,ABC,AME,AMGN,APH,APC,ADI,ANSS,ANTM,AON,AOS,APA,AIV,AAPL,AMAT,APTV,ADM,ARNC,ANET,AJG,AIZ,T,ADSK,ADP,AZO,AVB,AVY,BHGE,BLL,BAC,BK,BAX,BBT,BDX,BRK-B,BBY,BIIB,BLK,HRB,BA,BKNG,BWA,BXP,BSX,BHF,BMY,AVGO,BR,BF-B,CHRW,COG,CDNS,CPB,COF,CAH,KMX,CCL,CAT,CBOE,CBRE,CBS,CELG&'
#second100 = 'CNC,CNP,CTL,CERN,CF,SCHW,CHTR,CVX,CMG,CB,CHD,CI,XEC,CINF,CTAS,CSCO,C,CFG,CTXS,CLX,CME,CMS,KO,CTSH,CL,CMCSA,CMA,CAG,CXO,COP,ED,STZ,COO,CPRT,GLW,COST,COTY,CCI,CSX,CMI,CVS,DHI,DHR,DRI,DVA,DE,DAL,XRAY,DVN,DLR,DFS,DISCA,DISCK,DISH,DG,DLTR,D,DOV,DWDP,DTE,DRE,DUK,DXC,ETFC,EMN,ETN,EBAY,ECL,EIX,EW,EA,EMR,ETR,EOG,EFX,EQIX,EQR,ESS,EL,EVRG,ES,RE,EXC,EXPE,EXPD,ESRX,EXR,XOM,FFIV,FB,FAST,FRT,FDX,FIS,FITB,FE,FISV,FLT,FLIR,FLS&'
#third100 = 'FLR,FMC,FL,F,FTNT,FTV,FBHS,BEN,FCX,GPS,GRMN,IT,GD,GE,GIS,GM,GPC,GILD,GPN,GS,GT,GWW,HAL,HBI,HOG,HRS,HIG,HAS,HCA,HCP,HP,HSIC,HSY,HES,HPE,HLT,HFC,HOLX,HD,HON,HRL,HST,HPQ,HUM,HBAN,HII,IDXX,INFO,ITW,ILMN,IR,INTC,ICE,IBM,INCY,IP,IPG,IFF,INTU,ISRG,IVZ,IPGP,IQV,IRM,JKHY,JEC,JBHT,JEF,SJM,JNJ,JCI,JPM,JNPR,KSU,K,KEY,KEYS,KMB,KIM,KMI,KLAC,KSS,KHC,KR,LB,LLL,LH,LRCX,LEG,LEN,LLY,LNC,LIN,LKQ,LMT,L,LOW,LYB,MTB,MAC&'
#fourth100 = 'M,MRO,MPC,MAR,MMC,MLM,MAS,MA,MAT,MKC,MCD,MCK,MDT,MRK,MET,MTD,MGM,KORS,MCHP,MU,MSFT,MAA,MHK,TAP,MDLZ,MNST,MCO,MS,MOS,MSI,MSCI,MYL,NDAQ,NOV,NKTR,NTAP,NFLX,NWL,NFX,NEM,NWSA,NWS,NEE,NLSN,NKE,NI,NBL,JWN,NSC,NTRS,NOC,NCLH,NRG,NUE,NVDA,ORLY,OXY,OMC,OKE,ORCL,PCAR,PKG,PH,PAYX,PYPL,PNR,PBCT,PEP,PKI,PRGO,PFE,PCG,PM,PSX,PNW,PXD,PNC,RL,PPG,PPL,PFG,PG,PGR,PLD,PRU,PEG,PSA,PHM,PVH,QRVO,PWR,QCOM,DGX,RJF,RTN,O,RHT,REG,REGN,RF&'
#fifth100 = 'RSG,RMD,RHI,ROK,COL,ROL,ROP,ROST,RCL,CRM,SBAC,SCG,SLB,STX,SEE,SRE,SHW,SPG,SWKS,SLG,SNA,SO,LUV,SPGI,SWK,SBUX,STT,SRCL,SYK,STI,SIVB,SYMC,SYF,SNPS,SYY,TROW,TTWO,TPR,TGT,TEL,FTI,TXN,TXT,TMO,TIF,TWTR,TJX,TMK,TSS,TSCO,TDG,TRV,TRIP,FOXA,FOX,TSN,UDR,ULTA,USB,UAA,UA,UNP,UAL,UNH,UPS,URI,UTX,UHS,UNM,VFC,VLO,VAR,VTR,VRSN,VRSK,VZ,VRTX,VIAB,V,VNO,VMC,WMT,WBA,DIS,WM,WAT,WEC,WCG,WFC,WELL,WDC,WU,WRK,WY,WHR,WMB,WLTW,WYNN,XEL,XRX&'
#sixth5 = 'XLNX,XYL,YUM,ZBH,ZION,ZTS&'
#urlTypes = 'types=chart&'
#urlRange = 'range=3m'
#urlRequest1 = beginingBatchReq + first100 + urlTypes + urlRange 
#urlRequest2 = beginingBatchReq + second100 + urlTypes + urlRange 
#urlRequest3 = beginingBatchReq + third100 + urlTypes + urlRange 
#urlRequest4 = beginingBatchReq + fourth100 + urlTypes + urlRange 
#urlRequest5 = beginingBatchReq + fifth100+ urlTypes + urlRange 
#urlRequest6 = beginingBatchReq + sixth5 + urlTypes + urlRange 

#encode strings as urls
#urllib.parse.quote_plus(urlRequest1)
#urllib.parse.quote_plus(urlRequest2)
#urllib.parse.quote_plus(urlRequest3)
#urllib.parse.quote_plus(urlRequest4)
#urllib.parse.quote_plus(urlRequest5)
#urllib.parse.quote_plus(urlRequest6)

    

def getFullBatch(range, type):
    beginingBatchReq = 'https://api.iextrading.com/1.0/stock/market/batch?symbols='
    first100 = 'MMM,ABT,ABBV,ABMD,ACN,ATVI,ADBE,AMD,AAP,AES,AET,AMG,AFL,A,APD,AKAM,ALK,ALB,ARE,ALXN,ALGN,ALLE,AGN,ADS,LNT,ALL,GOOGL,GOOG,MO,AMZN,AEE,AAL,AEP,AXP,AIG,AMT,AWK,AMP,ABC,AME,AMGN,APH,APC,ADI,ANSS,ANTM,AON,AOS,APA,AIV,AAPL,AMAT,APTV,ADM,ARNC,ANET,AJG,AIZ,T,ADSK,ADP,AZO,AVB,AVY,BHGE,BLL,BAC,BK,BAX,BBT,BDX,BRK-B,BBY,BIIB,BLK,HRB,BA,BKNG,BWA,BXP,BSX,BHF,BMY,AVGO,BR,BF-B,CHRW,COG,CDNS,CPB,COF,CAH,KMX,CCL,CAT,CBOE,CBRE,CBS,CELG&'
    second100 = 'CNC,CNP,CTL,CERN,CF,SCHW,CHTR,CVX,CMG,CB,CHD,CI,XEC,CINF,CTAS,CSCO,C,CFG,CTXS,CLX,CME,CMS,KO,CTSH,CL,CMCSA,CMA,CAG,CXO,COP,ED,STZ,COO,CPRT,GLW,COST,COTY,CCI,CSX,CMI,CVS,DHI,DHR,DRI,DVA,DE,DAL,XRAY,DVN,DLR,DFS,DISCA,DISCK,DISH,DG,DLTR,D,DOV,DWDP,DTE,DRE,DUK,DXC,ETFC,EMN,ETN,EBAY,ECL,EIX,EW,EA,EMR,ETR,EOG,EFX,EQIX,EQR,ESS,EL,EVRG,ES,RE,EXC,EXPE,EXPD,ESRX,EXR,XOM,FFIV,FB,FAST,FRT,FDX,FIS,FITB,FE,FISV,FLT,FLIR,FLS&'
    third100 = 'FLR,FMC,FL,F,FTNT,FTV,FBHS,BEN,FCX,GPS,GRMN,IT,GD,GE,GIS,GM,GPC,GILD,GPN,GS,GT,GWW,HAL,HBI,HOG,HRS,HIG,HAS,HCA,HCP,HP,HSIC,HSY,HES,HPE,HLT,HFC,HOLX,HD,HON,HRL,HST,HPQ,HUM,HBAN,HII,IDXX,INFO,ITW,ILMN,IR,INTC,ICE,IBM,INCY,IP,IPG,IFF,INTU,ISRG,IVZ,IPGP,IQV,IRM,JKHY,JEC,JBHT,JEF,SJM,JNJ,JCI,JPM,JNPR,KSU,K,KEY,KEYS,KMB,KIM,KMI,KLAC,KSS,KHC,KR,LB,LLL,LH,LRCX,LEG,LEN,LLY,LNC,LIN,LKQ,LMT,L,LOW,LYB,MTB,MAC&'
    fourth100 = 'M,MRO,MPC,MAR,MMC,MLM,MAS,MA,MAT,MKC,MCD,MCK,MDT,MRK,MET,MTD,MGM,KORS,MCHP,MU,MSFT,MAA,MHK,TAP,MDLZ,MNST,MCO,MS,MOS,MSI,MSCI,MYL,NDAQ,NOV,NKTR,NTAP,NFLX,NWL,NFX,NEM,NWSA,NWS,NEE,NLSN,NKE,NI,NBL,JWN,NSC,NTRS,NOC,NCLH,NRG,NUE,NVDA,ORLY,OXY,OMC,OKE,ORCL,PCAR,PKG,PH,PAYX,PYPL,PNR,PBCT,PEP,PKI,PRGO,PFE,PCG,PM,PSX,PNW,PXD,PNC,RL,PPG,PPL,PFG,PG,PGR,PLD,PRU,PEG,PSA,PHM,PVH,QRVO,PWR,QCOM,DGX,RJF,RTN,O,RHT,REG,REGN,RF&'
    fifth100 = 'RSG,RMD,RHI,ROK,COL,ROL,ROP,ROST,RCL,CRM,SBAC,SCG,SLB,STX,SEE,SRE,SHW,SPG,SWKS,SLG,SNA,SO,LUV,SPGI,SWK,SBUX,STT,SRCL,SYK,STI,SIVB,SYMC,SYF,SNPS,SYY,TROW,TTWO,TPR,TGT,TEL,FTI,TXN,TXT,TMO,TIF,TWTR,TJX,TMK,TSS,TSCO,TDG,TRV,TRIP,FOXA,FOX,TSN,UDR,ULTA,USB,UAA,UA,UNP,UAL,UNH,UPS,URI,UTX,UHS,UNM,VFC,VLO,VAR,VTR,VRSN,VRSK,VZ,VRTX,VIAB,V,VNO,VMC,WMT,WBA,DIS,WM,WAT,WEC,WCG,WFC,WELL,WDC,WU,WRK,WY,WHR,WMB,WLTW,WYNN,XEL,XRX&'
    sixth5 = 'XLNX,XYL,YUM,ZBH,ZION,ZTS&'
    urlTypes = type
    urlRange = range
    urlRequest1 = beginingBatchReq + first100 + urlTypes + urlRange 
    urlRequest2 = beginingBatchReq + second100 + urlTypes + urlRange 
    urlRequest3 = beginingBatchReq + third100 + urlTypes + urlRange 
    urlRequest4 = beginingBatchReq + fourth100 + urlTypes + urlRange 
    urlRequest5 = beginingBatchReq + fifth100+ urlTypes + urlRange 
    urlRequest6 = beginingBatchReq + sixth5 + urlTypes + urlRange 

    #encode strings as urls
    urllib.parse.quote_plus(urlRequest1)
    urllib.parse.quote_plus(urlRequest2)
    urllib.parse.quote_plus(urlRequest3)
    urllib.parse.quote_plus(urlRequest4)
    urllib.parse.quote_plus(urlRequest5)
    urllib.parse.quote_plus(urlRequest6)

    r = requests.get(url = urlRequest1)
    data = r.json()
    updateData = data
    r = requests.get(url = urlRequest2)
    data = r.json()
    updateData.update(data)            
    r = requests.get(url = urlRequest3)
    data = r.json()
    updateData.update(data)    
    r = requests.get(url = urlRequest4)
    data = r.json()
    updateData.update(data)    
    r = requests.get(url = urlRequest5)
    data = r.json()
    updateData.update(data)    
    r = requests.get(url = urlRequest6)
    data = r.json()
    updateData.update(data)

    return updateData


# These functions are for calls on the whole S&P 500
def getPrevious():
    this = getFullBatch('', 'previous&')
    return this
def get1d():
    this = getFullBatch('range=1d', 'chart&')
    return this
def get3m():
    this = getFullBatch('range=3m', 'chart&')
    return this




# These functions are for calls on single stocks
def getRealPrice(ticker):
    urlRequest = 'https://api.iextrading.com/1.0/stock/' + ticker + '/price'
    urllib.parse.quote_plus(urlRequest)
    r = requests.get(url = urlRequest)
    price = r.json()
    return price

def getSingleChart(ticker, range):
    urlRequest = 'https://api.iextrading.com/1.0/stock/' + ticker + 'chart/' + range
    urllib.parse.quote_plus(urlRequest)
    print(urlRequest)
    r = requests.get(url = urlRequest)
    chart = r.json()
    print(chart)
    return chart



def main():
   
    print(api.get_account().cash)
    print(api.get_account().cash)
    #chart = getSingleChart('AAPL/', '/3m') #test of: https://api.iextrading.com/1.0/stock/aapl/chart/3m
    #print(chart)
    executeOrder('AAPL', '100', 'sell',  'market','day')
    



main()