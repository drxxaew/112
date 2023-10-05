import random

N = 10
a = []
for i in range(N):
    a.append(random.randint(1, 20))
    
print(a)

for i in range(N-1):
    for j in range(N - i - 1):
         if a[j] > a[j+1]:
             a[j], a[j+1] = a [j+1], a[j]

print(a)
