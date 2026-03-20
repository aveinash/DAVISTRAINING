# Function to check palindrome
def is_palindrome(value):
    original = str(value)
    reversed_val = ""

    # Using loop to reverse
    for ch in original:
        reversed_val = ch + reversed_val

    # Check using if-else
    if original == reversed_val:
        print("It is a Palindrome")
    else:
        print("It is not a Palindrome")


# Input from user
data = input("Enter a number or string: ")

# Call function
is_palindrome(data)