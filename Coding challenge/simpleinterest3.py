p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = int(input("Enter T: "))

si = 0
i = 1

while i <= t:
    si += (p * r) / 100
    i += 1

print("Simple Interest:", si)