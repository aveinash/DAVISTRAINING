p = float(input("Enter P: "))
r = float(input("Enter R: "))
t = int(input("Enter T: "))

rate_per_year = (p * r) / 100
si = 0

for year in range(1, t + 1):
    si = si + rate_per_year   # har saal add

print("Simple Interest:", si)