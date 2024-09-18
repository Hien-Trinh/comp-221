r = 0
n = 100
for i in range(1, n+1):
    for j in range(1, i+1):
        for k in range(j, i+j+1):
            r = r + 1

print(r)

r = (n**3 + 3*n**2 + 2*n)/3
print(r)
