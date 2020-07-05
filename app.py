from scipy.stats import linregress
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

class Run_model :
    def __init__(self,capital):
        self.capital = capital
        
    def inverse (self,upper=100 ,lowwer=0):
        x1 = lowwer ;  y1 = self.capital
        x2 = upper  ;  y2 = 0
        slope,b,_,_,_ = linregress([x1,x2],[y1,y2])
        x = np.arange(x1 , x2 , (y1 / x2))
        y = (slope * x) + b
        plt.figure(figsize=(12,8))
        plt.plot(x , y)
        st.pyplot()
        st.write( slope , b)
        
    def Direct (self,upper=100 ,lowwer=0):
        x1 = lowwer;  y1 = 0
        x2 = upper ;  y2 = self.capital
        slope,b,_,_,_ = linregress([x1,x2],[y1,y2])
        x = np.arange(x1 , x2 , (x2 /y2))
        y = (slope * x) + b
        plt.figure(figsize=(12,8))
        plt.plot(x , y)
        st.pyplot()
        st.write( slope , b)

if __name__ == '__main__':
    if st.checkbox('inverse'):
        capital_inverse = st.sidebar.number_input('capital' , 0 , 10000 , 100)
        inverse         = Run_model(capital=capital_inverse)
        upper_inverse   = st.sidebar.number_input('upper_inverse'   , 0 , 10000 , 100)
        lowwer_inverse  = st.sidebar.number_input('lowwer_inverse'  , 0 , 10000 , 0)
        _               = inverse.inverse(upper=upper_inverse ,lowwer=lowwer_inverse)
    if st.checkbox('Direct'):
        capital_Direct  = st.sidebar.number_input('Direct' , 0 , 10000 , 100)
        Direct          = Run_model(capital=capital_Direct)
        upper_Direct    = st.sidebar.number_input('upper_Direct'   , 0 , 10000 , 100)
        lowwer_Direct   = st.sidebar.number_input('lowwer_Direct'  , 0 , 10000 , 0)
        _               = Direct.inverse(upper=upper_Direct ,lowwer=lowwer_Direct)
