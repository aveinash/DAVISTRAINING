def calc(price, discount):
    return price - (price * discount / 100)

price = int(input("Enter price: "))
discount = int(input("Enter discount %: "))

print("Final price:", calc(price, discount))