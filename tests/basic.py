# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:06:27 2023

@author: Mark
"""
from TradingFramework.main import TradingFramework

tf=TradingFramework('config.ini')
tf.backtest.run()
