n = input()
x = [0 for i in range(int(n.split()[0]))]

arr = [x[:] for j in range(int(n.split()[0]))]


def queen(n, m):
    print(n, m)
    arr[n][m] = 1
    arr[n][m+1] = 1
    arr[n][m-1] = 1
    arr[n+1][m] = 1
    arr[n+1][m+1] = 1
    arr[n+1][m-1] = 1
    arr[n-1][m] = 1
    arr[n-1][m+1] = 1
    arr[n-1][m-1] = 1


queen(2, 2)
for i in arr:
    print(i)
