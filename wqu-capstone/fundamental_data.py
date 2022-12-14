#region imports
from AlgorithmImports import *
#endregion
import pandas as pd

class FundamentalData(object):
    '''
    FundamentalData class is responsible to handle fundamental data of stocks.
    This class collects and maintain the fundamental data and perforam different operations on same.
    '''
    def __init__(self):
        self.fundamentals = {}
    
    def add_symbol(self, symbol):
        '''
        Add the symbol to the dataframe when it don't exist.
        '''
        data = pd.DataFrame(columns=['Time','PE', 'PB', 'PCF', 'DY', 'CFO','ROA','ROE', 'DE', 'EPS', 'MCAP', 'SP', 
        'NIGrowth', 'Signal'])
        data = data.set_index('Time')
        self.fundamentals[symbol] = data
    
    def update_data(self, symbol, time, pe, pb, pcf, dyield, cfo, roa, roe, de_ratio, eps, mc, sp, ni_growth, signal):
        '''
        Update the dataframe from new data.
        '''
        #create pandas series to add entry into dataframe
        series = pd.Series({"Time": time, "PE":pe,"PB":pb,"PCF":pcf,"DY":dyield,
            "CFO": cfo, "ROA": roa, "ROE": roe, "DE": de_ratio, "EPS": eps, "MCAP": mc , "SP":sp,
            "NIGrowth": ni_growth, "Signal": signal}, name=time)
        #append the series/new data into dataframe
        self.fundamentals[symbol] = self.fundamentals[symbol].append(series,ignore_index=True)
        return
        
    def getValueZScore(self, symbol):
        '''
        Calculate value Z Score for given stock.
        '''
        # calculate z score for value parameters
        z_pe = (self.fundamentals[symbol].tail(1)["PE"] - self.fundamentals[symbol]["PE"].mean())/self.fundamentals[symbol]["PE"].std()
        z_pb = (self.fundamentals[symbol].tail(1)["PB"] - self.fundamentals[symbol]["PB"].mean())/self.fundamentals[symbol]["PB"].std()
        z_pcf = (self.fundamentals[symbol].tail(1)["PCF"] - self.fundamentals[symbol]["PCF"].mean())/self.fundamentals[symbol]["PCF"].std()
        z_div_yield = (self.fundamentals[symbol].tail(1)["DY"] - self.fundamentals[symbol]["DY"].mean())/self.fundamentals[symbol]["DY"].std()
        
        #calculate z score for stock
        return -1.0 * (0.25 * z_pe.values[0] if z_pe.any()  else 0.0 + 
        0.25* z_pb.values[0] if z_pb.any() else 0.0  + 0.25 * z_pcf.values[0] if z_pcf.any() else 0.0)
        + (0.25 * z_div_yield.values[0] if z_div_yield.any() else 0.0)
    
    def getQualityZScore(self, symbol):
        '''
        Calculate quality Z score for given stock
        '''
        # calculate z score for value parameters
        z_cfo = (self.fundamentals[symbol].tail(1)["CFO"] - self.fundamentals[symbol]["CFO"].mean())/self.fundamentals[symbol]["CFO"].std()
        z_roa = (self.fundamentals[symbol].tail(1)["ROA"] - self.fundamentals[symbol]["ROA"].mean())/self.fundamentals[symbol]["ROA"].std()
        z_roe = (self.fundamentals[symbol].tail(1)["ROE"] - self.fundamentals[symbol]["ROE"].mean())/self.fundamentals[symbol]["ROE"].std()
        z_de = (self.fundamentals[symbol].tail(1)["DE"] - self.fundamentals[symbol]["DE"].mean())/self.fundamentals[symbol]["DE"].std()
        z_eps = (self.fundamentals[symbol].tail(1)["EPS"] - self.fundamentals[symbol]["EPS"].mean())/self.fundamentals[symbol]["EPS"].std()
        
        #calculate z score for stock
        return (0.2 * z_cfo.values[0] if z_cfo.any()  else 0.0 + 0.2 * z_roa.values[0] if z_roa.any()  else 0.0 
        + 0.2 * z_roe.values[0] if z_roe.any()  else 0.0) +  (-0.2 * z_de.values[0] if z_de.any()  else 0.0 
        + -0.2 * z_eps.values[0] if z_eps.any()  else 0.0)