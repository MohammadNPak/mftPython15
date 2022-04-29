


# a = open('data.txt','r')
# b = a.read().replace("\n",",").split(',')
# print(b)


import csv

f = open('data.txt','r')
r = csv.reader(f)
for d in r:
    print(d)
print(type(r))


# a = ['1','2','3']
# ','.join(a)

# '1,2,3'