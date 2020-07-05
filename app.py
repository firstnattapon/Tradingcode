from scipy.stats import linregress
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

class Run_model :
    def __init__(self,capital,upper,lowwer):
        self.capital = capital
        self.upper = upper
        self.lowwer = lowwer

    @property
    def inverse (self):
        x1 = 0            ;  y1 = self.capital
        x2 = self.capital ;  y2 = 0
        slope,b,_,_,_ = linregress([x1,x2],[y1,y2])
        x = np.arange(x1 , x2 , (y1 / x2))
        y = (slope * x) + b
        plt.figure(figsize=(12,8))
        plt.plot(x , y)
        st.pyplot()
        st.write( slope , b)

    @property
    def Direct (self):
        pass
#         return pass

model =  Run_model(100 , 250 , 0)
model.inverse
