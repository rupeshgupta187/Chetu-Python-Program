first_term=0
second_term=1
print(first_term+second_term)
count=0
n=5

while count<=n:
    third_term=first_term+second_term
    print(third_term)
    first_term=second_term
    second_term=third_term
    count+=1
