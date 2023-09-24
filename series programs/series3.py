# #Determine the missing number in the series 13, 15, 21, 33, 53, 81, 117, 161, 213, 273, 341 ___.

# 15 - 13 = 2.
# The difference between the third term (21) and the second term (15) is 21 - 15 = 6.
# The difference between the fourth term (33) and the third term (21) is 33 - 21 = 12.
# The difference between the fifth term (53) and the fourth term (33) is 53 - 33 = 20.
first_term=13
second_term=15

series=[first_term,second_term]
length=10
i=2
while i<length:
    next_term=series[-1]+(i*3)
    series.append(next_term)
    i+=1

for x in series:
    print(x,end=" ")
    