from GoogleNews import GoogleNews
import pandas as pd

def get_news(ticket):
    googleNews = GoogleNews(encode='utf-8')
    googleNews.set_period('7d')
    googleNews.set_lang('pt')    
    googleNews.search(ticket)
    result = googleNews.result()     
    return result

print(get_news('petr4'))