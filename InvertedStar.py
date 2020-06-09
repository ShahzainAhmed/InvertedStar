# Program to create Inverted Star pattern. 

# Taking input from the user.
n=int(input("Enter number of rows: "))

# Using for loop with range.
for i in range (n,0,-1):
    
    # Using print statement.
    print((n-i) * ' ' + i * '*')
