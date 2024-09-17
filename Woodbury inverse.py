# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 05:54:30 2024

@author: tymur
"""
import numpy as np

def WoodburyInv(B,Omega,D):
    
    n = D.shape[0]
    aux1 = np.diag(np.divide(np.ones(n),np.diag(D)))
    aux2 = np.linalg.inv(Omega)
    elm0 = np.linalg.solve(D,B)
    
    return aux1-elm0@np.linalg.solve(B.T@elm0+aux2,elm0.T)
