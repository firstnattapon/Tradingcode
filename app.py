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
#         return pass

capital = st.sidebar.number_input('capital' , 0 , 10000 , 100)
upper   = st.sidebar.number_input('upper' , 0 , 10000 , 100)
lowwer  = st.sidebar.number_input('lowwer' , 0 , 10000 , 100)
model   =  Run_model(capital=capital)
_ = model.inverse(upper=upper ,lowwer=lowwer)
_ = model.Direct()
