# Program to generate a multiplication table

# Outer loop
for i in range(1, 13):
    # Inner loop 
    #print heading
    heading = f'{i} TIMES MULTIPLICATION'
    print(heading)
    print() # blank line
    for j in range(1, 13):
        
        # Print the product
        result = i * j
        print(f"{i} x {j} = {result}")
        print('-'*20)
    # Print a newline character after each row
    print()