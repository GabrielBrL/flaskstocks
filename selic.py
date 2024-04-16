import requests
from datetime import datetime

# Função para obter a taxa SELIC atual
def get_rates(codigo):
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados?formato=json"
    response = requests.get(url)
    data = response.json()    
    last_record = data[-1]
    return float(last_record["valor"])

# Obtendo a taxa SELIC atual
# selic_daily_rate = get_rates(432)
# cdi = get_rates(4389)
# ipca = get_rates(433)

# print("Taxa SELIC anual:", selic_daily_rate, "%")
# print("Taxa SELIC anual:", cdi, "%")
# print("Taxa SELIC anual:", ipca, "%")