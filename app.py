from scipy.stats import linregress
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

class Run_model :
    def __init__(self,capital):
        self.capital = capital
        
    def inverse (self,upper=100.0 ,lowwer=0.0 ,Asset_prices=0 ):
        x1 = lowwer ;  y1 = self.capital
        x2 = upper  ;  y2 = 0
        slope,b,_,_,_ = linregress([x1,x2],[y1,y2])
        x = np.arange(x1 , x2 , 0.01)
        y = (slope * x) + b
        plt.figure(figsize=(12,8))
        Port_value = slope *(Asset_prices) + b
        x_capital  = [0 , Asset_prices] ; y_capital = [Port_value , Port_value]
        x_asset    = [Asset_prices , Asset_prices] ; y_asset = [Asset_prices , Port_value]
        plt.plot(x , y)
        if Asset_prices != 0:
            plt.plot(x_capital, y_capital)
            plt.plot(x_asset , y_asset)
        st.pyplot()
        st.write('*Formula*')
        st.write('Port_value = ' , round(slope,4) ,'*(Asset_prices) +', round(b  , 4))
        st.write('Port_value = ' , round(slope,4) , Asset_prices  , round(b  , 4))
        st.write('Port_value = ' , Port_value)
        
    def Direct (self,upper=100.0 ,lowwer=0.0):
        x1 = lowwer;  y1 = 0
        x2 = upper ;  y2 = self.capital
        slope,b,_,_,_ = linregress([x1,x2],[y1,y2])
        x = np.arange(x1 , x2 , 0.01)
        y = (slope * x) + b
        plt.figure(figsize=(12,8))
        plt.plot(x , y)
        st.pyplot()
        st.write('Port_value = ', round(slope,3) , '*(Asset_prices) +', round(b  , 4))
        st.write('Port_value = ', round(slope,3) , '*(' , Asset_prices , ')+', round(b  , 4))
        st.write('') ; st.write('_'*40) ; st.write('')
    
if __name__ == '__main__':
    if st.checkbox('inverse(ผกผัน)'):
        capital_inverse = st.sidebar.number_input('capital_inverse(ผกผัน)',min_value=0.0,max_value=10000.0,value=1000.0,step=0.1,format='%f')   
        inverse         = Run_model(capital=capital_inverse)
        upper_inverse   = st.sidebar.number_input('upper_inverse(ผกผัน) ',min_value=0.0,max_value=10000.0,value=100.0,step=0.1,format='%f')        
        lowwer_inverse  = st.sidebar.number_input('lowwer_inverse(ผกผัน)',min_value=0.0,max_value=10000.0,value=0.000,step=0.1,format='%f')
        Asset_prices    = st.number_input('Asset_prices', min_value=0.0 ,max_value= upper_inverse ,value=0.0,step=0.1,format='%f')
        _               = inverse.inverse(upper=upper_inverse ,lowwer=lowwer_inverse , Asset_prices=Asset_prices)
        st.sidebar.text('-'*40)
        
    if st.checkbox('Direct(ผันตรง)'):
        capital_Direct  = st.sidebar.number_input('capital_Direct(ผันตรง) ',min_value=0.0,max_value=10000.0,value=1000.0,step=0.1,format='%f')
        Direct          = Run_model(capital=capital_Direct)
        upper_Direct    = st.sidebar.number_input('upper_Direct(ผันตรง)   ',min_value=0.0,max_value=10000.0,value=100.0,step=0.1,format='%f')       
        lowwer_Direct   = st.sidebar.number_input('lowwer_Direct(ผันตรง)  ',min_value=0.0,max_value=10000.0,value=0.000,step=0.1,format='%f')        
        _               = Direct.Direct(upper=upper_Direct ,lowwer=lowwer_Direct)
        st.sidebar.text('-'*40)
