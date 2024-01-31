import yfinance as yfr
import pandas_datareader.data as pdr
import pandas as pd
from datetime import datetime, timedelta

def get_detalhes_papel(papel):    
    data = yfr.Ticker(papel+".SA")    
    return data.info

def get_cotacao(papel):
    yfr.pdr_override()
    data_now = datetime.now()
    date_before = data_now - timedelta(days=7)     
    result =  pdr.get_data_yahoo(papel+".SA", date_before.strftime("%Y-%m-%d"), data_now.strftime("%Y-%m-%d"))["Adj Close"]
    df = pd.DataFrame(result)    
    dictresult = df.to_json(orient='columns', date_format='iso')
    return dictresult

print(get_cotacao("petr4"))