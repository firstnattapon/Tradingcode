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
        st.write('Portvalue =', slope ,'*(Asset prices)+', b )
        
    def Direct (self,upper=100 ,lowwer=0):
        x1 = lowwer;  y1 = 0
        x2 = upper ;  y2 = self.capital
        slope,b,_,_,_ = linregress([x1,x2],[y1,y2])
        x = np.arange(x1 , x2 , (x2 /y2))
        y = (slope * x) + b
        plt.figure(figsize=(12,8))
        plt.plot(x , y)
        st.pyplot()
        st.write('Portvalue =', slope ,'*(Asset prices)+', b )

if __name__ == '__main__':
    if st.checkbox('inverse'):
        capital_inverse = streamlit.sidebar.number_input('capital_inverse(ผกผัน)'min_value=0.0,max_value=10000.0,value=100.0,step=0.01,format='%d')
        inverse         = Run_model(capital=capital_inverse)
        upper_inverse   = st.sidebar.number_input('upper_inverse(ผกผัน)'   , 0 , 10000 , 100)
        lowwer_inverse  = st.sidebar.number_input('lowwer_inverse(ผกผัน)'  , 0 , 10000 , 0)
        _               = inverse.inverse(upper=upper_inverse ,lowwer=lowwer_inverse)
        st.sidebar.text('-'*40)
    if st.checkbox('Direct'):
        capital_Direct  = st.sidebar.number_input('capital_Direct(ผันตรง)' , 0 , 10000 , 100)
        Direct          = Run_model(capital=capital_Direct)
        upper_Direct    = st.sidebar.number_input('upper_Direct(ผันตรง)'   , 0 , 10000 , 100)
        lowwer_Direct   = st.sidebar.number_input('lowwer_Direct(ผันตรง)'  , 0 , 10000 , 0)
        _               = Direct.Direct(upper=upper_Direct ,lowwer=lowwer_Direct)
        st.sidebar.text('-'*40)
        
