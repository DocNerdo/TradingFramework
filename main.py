# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:35:15 2023

@author: Mark
"""

import configparser
from ast import literal_eval
import os
from backtest import Backtest


class TradingFramework():
    
    def __init__(self,config_file_path):
        
        #erstelle generelle benoetigte Klassen
        self.backtest=Backtest()
        
        
        #lese config ein
        config = configparser.ConfigParser()
        config.read(config_file_path)
        
        #general
        for option in config.options('general'):
            setattr(self,option,literal_eval(config.get('general', option)))
    
        #backtesting
        for option in config.options('backtesting'):
            setattr(self.backtest,option,literal_eval(config.get('backtesting', option)))
            
        self.backtest.tickers_to_observe=self.tickers_to_observe
        
        print(self.backtest.tickers_to_observe)
    
