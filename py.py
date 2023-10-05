import random


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
    if len (arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
        L=[]
        M=[]
        R=[]
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
sel_sort(a)
print(a)
