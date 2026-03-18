price = int(input("Enter price: "))
discount = int(input("Enter discount %: "))

reduction = price
reduction *= discount
reduction /= 100

final = price - reduction

print("Final price:", final)