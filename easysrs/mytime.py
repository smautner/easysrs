
from datetime import date, timedelta
'''
now()  return nowdate string 
indays(x) return now() + x days 
'''



def format(date):
    return date.strftime("%Y-%m-%d") 

def now(): 
    return format(date.today())

def indays(d):
    return format(date.today()+timedelta(days=d))
