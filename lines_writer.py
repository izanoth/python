

f = open('temp', 'x')

x = 0
y = 0

while x < 600:
    f.write("<circle cx='"+str(x)+"' cy='"+str(y)+"' r='3' />\n")
    x += 8
    if x + 6 >= 600 :
        x = 0
        y += 8
    if y >= 600:
        break
