def test_index(data,index):
    try:
        result=data[index]
        print("result is : ",result)
    except Exception as e:
        print(f"type error has eccur {e}")

num=[1,2,3,4,5,5]
input=int(input("enter index number is : "))
test_index(num,input)
