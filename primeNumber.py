# def prime(n):
    # flag=False
    # for i in range(2,n+1):
    #     if (n%i)==0:
    #         flag=True
    #         break
    #     else:
    #         flag=False
    # if flag:
    #     print(n ,"it is not a prime number")
    # else:
    #     print(n, "it is a prime number")
def prime(num):
    flag=False
    for i in range(2, num):
        if (num % i) == 0:
            # if factor is found, set flag to True
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")

prime(9)

