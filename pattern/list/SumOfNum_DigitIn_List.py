# list = [12, 67, 98, 34]
# b=[]
# for x in list:
#     sum=0
#     for y in str(x):
#         sum+=int(y)
#     b.append(sum)
# print(b)


lst = [12, 67, 98, 34]
def digit_sum(x):
	digit_sum = 0
	while x > 0:
		digit_sum += x % 10
		x //= 10
	return digit_sum

def sum_of_digits_list(lst):
	return list(map(digit_sum, lst))

print(sum_of_digits_list(lst))
