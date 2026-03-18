p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = int(input("Enter T: "))

si = 0
for i in range(t):
    si += (p * r) / 100

print("Simple Interest:", si)