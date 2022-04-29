


a = open('data.txt','r')

b = a.read().replace("\n",",").split(',')

print(b)


