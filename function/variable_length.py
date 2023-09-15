def average(*numbers):
    sum=0
    for i in numbers:
        sum+=i
    print("average of number is : ",sum/len(numbers))


average(122,234,45)