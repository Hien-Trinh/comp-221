n = 100
s = 0

for i in range(n + 1):
    for j in range(n - i):
        s += 1

print(s)

r = (n ** 2 + n) / 2
print(r)
