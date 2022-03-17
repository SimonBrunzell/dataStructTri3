N = 3
arr1 = [0]*N
N = 3
arr2 = [0]*N
N = 3
arr3 = [0]*N


n = 1
while n < 4:
    arr1[n-1] = n
    n = n + 1

n = 4
while n < 7:
    arr2[n-4] = n
    n = n + 1

n = 7
while n < 10:
    arr3[n-7] = n
    n = n + 1

print()
print("here's my matrix!")

print(arr1)
print(arr2)
print(arr3)




