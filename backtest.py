# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:41:01 2023

@author: Mark
"""

from datastream import DataStream

class Backtest():
    
    def __init__(self):
        pass
        
    def run(self):
        
        # gehe alle testperioden durch
        for test_period in self.test_periods:
            
            #initiere data stream
            test_period_start_date=self.test_periods[test_period]['start_date']
            test_period_end_date=self.test_periods[test_period]['end_date']
            ds=DataStream(tickers=self.tickers_to_observe,mode='backtesting',
                          start_date=test_period_start_date,
                          end_date=test_period_end_date)
            
            
            current_time_stamp=ds.historical_data.index.values[0]

            #gehe jeden timestamp durch
            for i in range(len(ds.historical_data.index.values)):
                
                ds.getCurrentData()
            
            
                #hole cash und alle positionen etc.
                
                    
                    #evaluiere jede strategie
                    
                
                #fuehre alle positionen aus die aus strategien folgen
                
                
            
            #print(test_period_start_date)
        