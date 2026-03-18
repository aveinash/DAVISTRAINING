price = int(input("Enter price: "))
discount = int(input("Enter discount %: "))

discount_amount = price * discount / 100
final = price - discount_amount

print("Final price:", final)