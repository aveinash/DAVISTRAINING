age = int(input("Enter age: "))

eligible = False

if age >= 18:
    eligible = True

if eligible:
    print("Eligible")
else:
    print("Not Eligible")