# Taking input from the user.
n=int(input("Enter number of rows: "))

# Using for loop with range.
for i in range (n,0,-1):
    
    print((n-i) * ' ' + i * '*')
