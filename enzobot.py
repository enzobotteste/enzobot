import tweepy
import datetime
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options # apenas pra facilitar a leitura do codigo
from selenium.webdriver.common.keys import Keys
import datetime
import time

auth = tweepy.OAuthHandler("yTN05yKL6x0A6boQJABGRnk57", "oz08RguRf1zzViz7nQSHVBP29MMKhmbYfctl4eFCP2ZqdchCQ7")
auth.set_access_token("1198082144096194560-wNHbZB5USfvRNP6l2lLfQBjLBYFl8c", "OLT9bISVVLAQrLUN91V22kzHi6I3dbLIGyxJnID39YyLG")
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

diferenca = datetime.timedelta(hours=-3)
fuso_horario = datetime.timezone(diferenca)
horariomin = datetime.datetime.now().minute
num = 1
options = Options()
options.headless = True # o navegador passa a nao ter interface grafica (ja' que estara' rodando em um EC2)
browser = webdriver.Chrome(options = options)   

while(True):
    try:
        horariomin = datetime.datetime.now().minute
        if(horariomin==28):
            api.update_status('Enzo número {}'.format(num))
            num += 1
            sleep(60)
        '''for tweet in tweepy.Cursor(api.search,q='Enzo', lang="pt",).items(25):
            if(re.search(r'\benzo\b', tweet.text) or re.search(r'\bEnzo\b', tweet.text)):
                tweet.favorite()'''
    except tweepy.TweepError as e:
        print(e.reason)
