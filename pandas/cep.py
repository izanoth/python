import pandas as pd
import random, decimal
from decimal import Decimal

df = pd.read_excel('cep.xlsx')

#def gen_random_decimal(i,d):
#    return decimal.Decimal('%d.%d' % (random.randint(0,i),random.randint(0,d)))
#for i in range(10):
#    print(float(decimal.Decimal(random.randrange(9990, 10003))/1000))


for x, y in df.iteritems():
  print(x)
  print(y)
        #for j in i:
        #    if type(j)=='nan':
        #        j = str(float(decimal.Decimal(random.randrange(9990, 10003))/1000))

