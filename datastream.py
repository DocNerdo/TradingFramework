# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:01:40 2023

@author: Mark
"""

import os
import yfinance as yf

class DataStream():
    
    def __init__(self,tickers,mode,start_date=None,end_date=None):
        
        self.mode=mode
        self.tickers=tickers
        
        if mode == 'backtesting':
            
            #im backtesting mode beinhaltet das history dataframe
            #alle historischen werte vom startzeitpunkt bis zum endzeitpunkt
            
            self.historical_data=self.getTestPeriodData(tickers,start_date,end_date)['Close']
            print(self.historical_data)
            
    def getTestPeriodData(self,tickers,start_date,end_date):
        
        data=yf.download(tickers,start=start_date, end=end_date,interval = "1d",prepost = False,repair = True,auto_adjust=True,progress=False)
        return data
       
    
    def getCurrentData(self):
        pass
        
        
    
    
    