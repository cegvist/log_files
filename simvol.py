e = open('logTM2.txt','r')
txt = e.read()
x = txt.split()
print(x[::18])

b=":"
for char in b:
     a=x[0].replace(char,"")
b="."
for char in b:
     a=a.replace(char,"")
print(a)

b=":"
for char in b:
     c=x[18].replace(char,"")
b="."
for char in b:
     c=c.replace(char,"")
print(c)


e.close()