from scipy.stats import linregress
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from datetime import  datetime
import ccxt

class Run_model :
    def __init__(self,capital):
        self.capital = capital
        self.timeframe = "1m"  
        self.limit = 3

    def dataset (self  , pair_data = "BTC-USD"):
        self.exchange = ccxt.ftx({'apiKey': '' ,'secret': ''  , 'enableRateLimit': True }) 
        timeframe = self.timeframe
        limit =  self.limit 
        ohlcv = self.exchange.fetch_ohlcv(pair_data,timeframe , limit=limit )
        ohlcv = self.exchange.convert_ohlcv_to_trading_view(ohlcv)
        df =  pd.DataFrame(ohlcv)
        df.t = df.t.apply(lambda  x :  datetime.fromtimestamp(x))
        df =  df.set_index(df['t']) ; df = df.drop(['t'] , axis= 1 )
        df = df.rename(columns={"o": "open", "h": "high"  , "l": "low", "c": "close" , "v": "volume"})
        close = df['close'][-1]  
        return close
        
    def inverse (self,upper=100.0 ,lowwer=0.0 , Asset_prices=0):
        x1 = lowwer ;  y1 = self.capital
        x2 = upper  ;  y2 = 0
        slope,b,_,_,_ = linregress([x1,x2],[y1,y2])
        x = np.arange(x1 , x2 , 0.05)
        y = (slope * x) + b
        plt.figure(figsize=(12,8))
        Port_value = slope *(Asset_prices) + b
        x_capital  = [lowwer , Asset_prices] ; y_capital = [Port_value , Port_value]
        x_asset    = [Asset_prices  , Asset_prices] ; y_asset = [0 , Port_value]
        plt.plot(x , y , label='D = {:.2f}'.format(abs(slope)))
        if Asset_prices != 0:
            plt.plot(x_capital, y_capital , color='r')
            plt.plot(x_asset , y_asset , color='r')
        if upper >= 5:
            plt.legend(fontsize=12)
        plt.xlabel('Asset_prices',fontsize=14)
        plt.ylabel('Port_value',fontsize=14)
        st.pyplot()
        st.write('Formula')
        st.write('Port_value = ' , round(slope,4) ,'*(Asset_prices) +', round(b  , 4))
        st.write('Port_value = ' , round(slope,4) , '*(' ,Asset_prices, ') +' , round(b  , 4))
        st.write('Port_value = ' , round(Port_value , 4))
        st.write('') ; st.write('_'*40) ; st.write('')

    def Direct (self,upper=100.0 ,lowwer=0.0, Asset_prices=0):
        x1 = lowwer;  y1 = 0
        x2 = upper ;  y2 = self.capital
        slope,b,_,_,_ = linregress([x1,x2],[y1,y2])
        x = np.arange(x1 , x2 , 0.05)
        y = (slope * x) + b
        plt.figure(figsize=(12,8))
        Port_value = slope *(Asset_prices) + b
        x_capital  = [lowwer , Asset_prices] ; y_capital = [Port_value , Port_value]
        x_asset    = [Asset_prices  , Asset_prices] ; y_asset = [0 , Port_value]
        plt.plot(x , y , label='D = {:.2f}'.format(abs(slope)))
        if Asset_prices != 0:
            plt.plot(x_capital, y_capital , color='r')
            plt.plot(x_asset , y_asset , color='r')
        if upper >= 5:
            plt.legend(fontsize=12)
        plt.xlabel('Asset_prices',fontsize=14)
        plt.ylabel('Port_value',fontsize=14)
        st.pyplot()
        st.write('Formula')
        st.write('Port_value = ' , round(slope,4) ,'*(Asset_prices) +', round(b  , 4))
        st.write('Port_value = ' , round(slope,4) , '*(' ,Asset_prices, ') +' , round(b  , 4))
        st.write('Port_value = ' , round(Port_value , 4))
        st.write('') ; st.write('_'*40) ; st.write('')
    
if __name__ == '__main__':
    st.subheader('Tradingcode')  ; st.write('-'*50)
    if  st.checkbox('Inverse (ผกผัน)'):
        st.sidebar.text('-'*40)
        capital_inverse  = st.sidebar.number_input('capital_inverse(เงินทุนเริ่มต้น)',min_value=0.0,max_value=10000.0,value=1000.0,step=0.1,format='%f')   
        inverse             = Run_model(capital=capital_inverse)
        upper_inverse    = st.sidebar.number_input('upper_inverse(โซนบน)    !ต้องมากกว่า Asset_prices',min_value=0.0,max_value=30000.0,value=20000.0,step=0.1,format='%f')        
        lowwer_inverse  = st.sidebar.number_input('lowwer_inverse(โซนล่าง) !ต้องน้อยกว่า Asset_prices',min_value=0.0,max_value=30000.0,value=0.000,step=0.1,format='%f')
        Auto_asset = st.checkbox('Auto_prices')
        if Auto_asset :    
            pair_data      =  st.text_input( 'symbol_ftx' , 'BTC-PERP')
            Auto_inverse   =  inverse.dataset(pair_data)
            Asset_prices  = st.number_input('Asset_prices', min_value=lowwer_inverse ,max_value= upper_inverse , value=Auto_inverse ,step=0.1,format='%f') 
        else:
            Asset_prices  = st.number_input('Asset_prices', min_value=lowwer_inverse ,max_value= upper_inverse ,value=upper_inverse,step=0.1,format='%f') 
        _                      = inverse.inverse(upper=upper_inverse ,lowwer= lowwer_inverse , Asset_prices=Asset_prices)
        st.sidebar.text('-'*40)
        
    if  st.checkbox('Direct (ผันตรง)'):
        st.sidebar.text('-'*40)
        capital_Direct   = st.sidebar.number_input('capital_Direct(เงินทุนเริ่มต้น) ',min_value=0.0,max_value=10000.0,value=1000.0,step=0.1,format='%f')
        Direct              = Run_model(capital=capital_Direct)
        upper_Direct    = st.sidebar.number_input('upper_Direct(โซนบน)   !ต้องมากกว่า Asset_price   ',min_value=0.0,max_value=30000.0,value=20000.0,step=0.1,format='%f')       
        lowwer_Direct  = st.sidebar.number_input('lowwer_Direct(โซนล่าง)!ต้องน้อยกว่า Asset_prices ',min_value=0.0,max_value=30000.0,value=0.000,step=0.1,format='%f')
        Auto_asset = st.checkbox('Auto_prices ')
        if Auto_asset :   
            pair_data      =  st.text_input( 'Symbol_ftx' , 'BTC-PERP')
            Auto_Direct   =  Direct.dataset(pair_data)
            Asset_prices    = st.number_input('Asset_prices ', min_value= lowwer_Direct ,max_value= upper_Direct ,value=Auto_Direct,step=0.1,format='%f')
            Asset_prices   =  Direct.dataset(pair_data)
        else:
            Asset_prices    = st.number_input('Asset_prices ', min_value= lowwer_Direct ,max_value= upper_Direct ,value=upper_Direct,step=0.1,format='%f')
        _                    = Direct.Direct(upper=upper_Direct ,lowwer=lowwer_Direct , Asset_prices=Asset_prices)
        st.sidebar.text('-'*40)

    code = """
v 1.20 (7/7/2020)
- Added  Auto_prices

Donate
XRP Addres: rpXTzCuXtjiPDFysxq8uNmtZBe9Xo97JbW
XRP Tag   : 1024466261"""
    st.sidebar.code(code, language='python')
