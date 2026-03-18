def simple_interest(p, r, t):
    return (p * r * t) / 100

p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = float(input("Enter T: "))

si = simple_interest(p, r, t)

print("Simple Interest:", si)