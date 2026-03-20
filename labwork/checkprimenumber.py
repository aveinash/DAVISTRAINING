# Function to check prime number
def is_prime(n):
    if n <= 1:
        return False
# using for loop to check divisibility if divisible return ,false otherwise return, true
    for i in range(2, n):
        if n % i == 0:
            return False
    
    return True


# Input from user
num = int(input("Enter a number: "))

# Display result using if-else
if is_prime(num):
    print("It is a Prime Number")
else:
    print("It is not a Prime Number")