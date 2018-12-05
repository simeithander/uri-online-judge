l, d = input().split()
l = int(l)
d = int(d)

k, p = input().split()
k = int(k)
p = int(p)

pedagio = l // d
custo_pedagio = pedagio * p
custo_km = l * k
custo_total = custo_pedagio + custo_km

print('{:.0f}'.format(custo_total))