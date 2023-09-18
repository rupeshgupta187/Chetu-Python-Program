number=[1,2,3,4,5]
letters=['b','c','r','s','u']
operators=['+','-','*','/','%']

for n, l, o in zip(number,letters,operators):
    print(f'number is :{n} ')
    print(f'letter is : {l}')
    print(f'operator is : {o}')
    print()
