price = int(input("Enter price: "))
discount = int(input("Enter discount %: "))

i = 0
deduct = 0

while i < discount:
    deduct += price / 100
    i += 1

final = price - deduct

print("Final price:", final)