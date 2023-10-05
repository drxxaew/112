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
N = 10
a = gen()
print(a)
sel_sort(a)
print(a)
