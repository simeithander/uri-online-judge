a,b = input().split()
a = float(a)
b = float(b)

res = (b - a) /a*100

print("{:.2f}%".format(res))