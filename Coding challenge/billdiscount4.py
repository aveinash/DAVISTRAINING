price = int(input("Enter price: "))
discount = int(input("Enter discount %: "))

final = price * (1 - discount/100)

print("Final price:", final)