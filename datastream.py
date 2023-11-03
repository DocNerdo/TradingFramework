# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 20:01:40 2023

@author: Mark
"""

import ConfigParser
import os

class TradingFramework():
    
    def __init__(self,config_file_path):
        
        #lese config ein
        config = ConfigParser.ConfigParser()
        config.read(config_file_path)
        
        #general
        
        
        pass
    
    

if __name__ == "__main__":

    tf=TradingFramework()
    
    