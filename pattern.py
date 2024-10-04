def print_number_pyramid(rows):
    for i in range(1, rows + 1):
        # Print spaces
        for j in range(rows - i):
            print(" ", end="")
        # Print numbers
        for j in range(2 * i - 1):
            print(j + 1, end="")
        # Move to the next line after each row
        print()

# Example usage
num_rows = 5
print_number_pyramid(num_rows)
n = 5
alph = 65
for i in range(0, n):
    print(" " * (n-i), end=" ")
    for j in range(0, i+1):
        print(chr(alph), end=" ")
        alph += 1
    alph = 65
    print()

# Function to print full pyramid pattern
def full_pyramid(n):
    for i in range(1, n + 1):
        # Print leading spaces
        for j in range(n - i):
            print(" ", end="")
        
        # Print asterisks for the current row
        for k in range(1, 2*i):
            print("*", end="")
        print()
   
full_pyramid(5)


# Function to print a half pyramid pattern
def half_pyramid(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print("* ", end="")
        print("")

# Example: Print a half pyramid with 5 rows
n = 5
half_pyramid(n)
