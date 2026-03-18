units = int(input("Enter units: "))

if units <= 100:
    bill = units * 5
else:
    bill = units * 7

print("Total bill:", bill)