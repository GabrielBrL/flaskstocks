import yfinance as yfr
import pandas as pd
from datetime import datetime, timedelta

def get_detalhes_papel(papel):
    data = yfr.Ticker(papel+".SA")    
    #data.info['DataUltCotacao'] = get_variacao(papel)
    var = get_variacao(papel)
    index = list(var.keys())[0]    
    percVar = var[index][0]
    vlrVar = var[index][1]
    ultVar = var[index][2]
    dtCotacao = index    
    data.info["CurrentPrice"] = ultVar
    data.info["DataUltCotacao"] = dtCotacao
    data.info["VariacaoPercentual"] = percVar
    data.info["VariacaoValue"] = vlrVar
    return data.info

def get_variacao(papel):    
    ticker = papel
    acao = yfr.Ticker(f"{ticker}.SA")
    historico_precos = acao.history(period='2d')
    df = pd.DataFrame(historico_precos)
    df.fillna(0, inplace=True)    
    dict = df.to_dict(orient="dict")
    value = dict['Close']
    data_str_keys = {key.strftime('%Y-%m-%d'): value for key, value in value.items()}    
    primeiro_valor = next(iter(data_str_keys.values()))
    ultima_data = list(data_str_keys.keys())[-1]
    ultimo_valor = data_str_keys[ultima_data]
    variacaoPerc = ((ultimo_valor - primeiro_valor) / ultimo_valor)
    variacaoValue = ultimo_valor - primeiro_valor
    return {ultima_data : [variacaoPerc, variacaoValue, ultimo_valor]}

def get_hist(papel, variacao):    
    ticker = papel
    acao = yfr.Ticker(f"{ticker}.SA")
    historico_precos = acao.history(period=variacao)    
    df = pd.DataFrame(historico_precos)
    df.fillna(0, inplace=True)  
    dict = df.to_dict(orient="dict")
    value = dict['Close']
    data_str_keys = {key.strftime('%Y-%m-%d'): value for key, value in value.items()}    
    return data_str_keys

def get_history_dividends(papel):
    acoes = yfr.Ticker(f'{papel}.SA')
    history_divs = acoes.get_dividends()
    df = pd.DataFrame(history_divs)
    df.fillna(0, inplace=True)  
    dict = df.to_dict(orient="dict")
    value = dict['Dividends']
    data_str_keys = {key.strftime('%Y-%m-%d'): value for key, value in value.items()}
    return data_str_keys

print(get_detalhes_papel("vale3"))