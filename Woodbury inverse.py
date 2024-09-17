# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 05:54:30 2024

@author: tymur
"""
import numpy as np

def WoodburyInv(B,Omega,D):
    
    if (len(B.shape) != 2) | (len(Omega.shape) != 2) | (len(D.shape) != 2):
        
        print("ATTENTION: all the input arrays have to be two dimensional!")
        
    if (B.shape[1] != Omega.shape[0]) | (B.shape[0] != D.shape[0]):
        
        print("ATTENTION: check the dimensions of the input arrays for consistency!")
    
    n = D.shape[0]
    aux1 = np.diag(np.divide(np.ones(n),np.diag(D)))
    aux2 = np.linalg.inv(Omega)
    elm0 = np.linalg.solve(D,B)
    
    return aux1-elm0@np.linalg.solve(B.T@elm0+aux2,elm0.T)
