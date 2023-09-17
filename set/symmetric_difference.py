s1 = {1,2,3,4,5,6}
s2={2,3,4,5,7,8}

c=s1.symmetric_difference(s2)
print(c)

c2=s1.issubset(s2)
c3=s1.issuperset(s2)
print(c2)
print(c3)