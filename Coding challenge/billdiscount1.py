price = int(input("Enter price"))
discount = int(input("Enter discount % "))

final = price - (price * discount/100)
print("final price: ",final)