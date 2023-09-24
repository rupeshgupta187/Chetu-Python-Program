# Given series: 1, 2, 10, 37, 101, ___.

# 1 + 1**3 = 1 + 1 = 2

# 2 + 2**3 = 2 + 8 = 10

# 10 + 3**3 = 10 + 27 = 37

# 37 + 4**3 = 37 + 64 = 101

# 101 + 5**3 = 101+ 125 = 226
curent_term=1
user_num=5
for x in range(1,user_num):
    print(f"{curent_term} + {x**3} =" ,end="")
    curent_term+=x**3
    print(curent_term)


for i in range(1, 21):
    print(i * (i + 1) // 2,end=" ")
