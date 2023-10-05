import random
import time
f = open('out.txt', 'w')
def gen(size):
    a = []
    for i in range(size):
        a.append(random.randint(0, 9))
    a.append(10)
    return a

def find(cv, qw):
    i = 0
    while i < len(cv):
        if cv[i] == qw:
            return i
        i += 1
    return -1

size = 1000000
iter = 100
a = gen(size)

start = time.time()

for i in range(iter):
    a.index(10)
def test(iter, size):
    start = time.time()
  
end = (time.time() - start) / iter

print(f'в начале: {end}')   


a[size // 2] = 11
start = time.time()
for i in range(iter):
    a.index(11)
end = (time.time() - start) / iter
print(f'в середине: {end}')

a[-1] = 12
start = time.time()
for i in range(iter):
    a.index(12)
end = (time.time() - start) / iter
print(f'в конце: {end}')







def gen():
    a = []
    for i in range(N):
        a.append(random.randint(1, 20))
    return a


def bubble(arr):
    for i in range(N-1):
        for j in range(N - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a [j+1], a[j]
def sel_sort(arr):
    n = len(arr)
    for i in range(n-1):
        m = i
        for j in range (i+1, n):
            if arr[j] < arr[m]:
                m = j
            arr[i], arr [m] = arr[m], arr[i]
def quick_sort(arr):
    if len(arr) <=1:
        return arr
    else:
        q = random.choice(arr)
        L = []
        M = []
        R = []
        for elem in arr:
            if elem < q:
                L.append(elem)
            elif elem > q:
                R.append(elem)
            else:
                M.append(elem)
    return quick_sort(L) + M + quick_sort(R)
N = 10
a = gen()
print(a)
a = quick_sort(a)
print(a)
