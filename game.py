
e = open('logTM.txt','r')
txt = e.read()
x = txt.split()
print(x[::18])

e.close()