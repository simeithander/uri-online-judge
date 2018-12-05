a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)

x, y, z = input().split()
x = int(x)
y = int(y)
z = int(z)

if c <=z:
    res = (y//b)*(x//a)*(z//c)
else:
    res = 0
print('{:.0f}'.format(res))