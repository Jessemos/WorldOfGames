import requests
import random


request = requests.get('https://api.exchangeratesapi.io/latest?base=USD&symbols=ILS,USD')
request.text
rates = request.json()
new_rate =  int(float(rates["rates"]["ILS"])*1000)
print(new_rate)
new_rate = (new_rate + random.randrange(100)+1)/1000
print(new_rat)
