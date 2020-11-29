# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 17:32:05 2020
%matplotlib qt
@author: Leonardo Milos
"""

import pandas as pd
import json
class pagerank():
    def __init__(self):
        with open('rank.txt') as json_file:
            self.data = json.load(json_file)
    def ordena(self,vet):
        self.modelo={}
        for i in vet:
            try:
                self.modelo[i]=self.data[i]
            except:
                print(i)
        self.sort_orders = sorted(self.modelo.items(), key=lambda x: x[1], reverse=True)
        retorno=[]
        for i in self.sort_orders:
            retorno.append(i[0])
        return retorno
        

