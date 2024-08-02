import random, decimal
from decimal import Decimal
import pandas as pd

f = open('simple2.csv', 'x')

for i in range(10):
    for j in range(6):
        if j != 5:
            f.write(str(float(decimal.Decimal(random.randrange(9990, 10003))/1000))+',')
        else:
            f.write(str(float(decimal.Decimal(random.randrange(9990, 10003))/1000))+'\n')


f.close()

df = pd.read_csv('simple2.csv')

df.to_excel("output.xlsx")

