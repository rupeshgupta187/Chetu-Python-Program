def arithematicError(x,y):
    try:
        result=x/y
        print(result)
    except Exception as e:
        print(f"Erroer has occure {e} ")
n1=int(input("enter first number :"))
n2=int(input("enter first number :"))
arithematicError(n1,n2)