from itertools import zip_longest
number=[1,2,3,4,5]
letters=['b','c','r','s','u']
longest=range(9)

zipped=list(zip(number,letters,longest))
zipped_1=list(zip_longest(number,letters,longest,fillvalue='?'))
print(zipped)
print(zipped_1)