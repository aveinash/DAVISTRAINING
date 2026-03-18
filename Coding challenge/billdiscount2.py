price = int(input("Enter price: "))
discount = int(input("Enter discount %: "))

final = price * (100 - discount) // 100

print("Final price:", final)