try:
    n = int(input("Input a number: "))
    print("You entered:", n)
except KeyboardInterrupt as e:
    print(f"Input canceled by the user {e}")
