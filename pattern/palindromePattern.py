

def print_palindromic_pattern(n):
    for i in range(1, n + 1):
        # Print increasing numbers
        for j in range(1, i + 1):
            print(j, end=" ")
        
        # Print decreasing numbers
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        
        print()  # Move to the next line

# Change the value of 'n' to adjust the pattern size
n = int(input("Enter the number of rows: "))
print_palindromic_pattern(n)