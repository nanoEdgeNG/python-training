# Function to find and return the factors
def find_factors(number):
    # List to store the factors
    factors = []
    # Loop from 1 to the number
    for i in range(1, number + 1):
        # Check if i is a factor of the number
        if number % i == 0:
            # If so, add it to the list of factors
            factors.append(i)
    return factors

# Input from the user
num = int(input("Enter a number: "))
# Get the factors of the number
factors = find_factors(num)

# print factors
print(factors)
