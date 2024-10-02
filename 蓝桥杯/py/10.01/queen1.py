n = input()
x = [0 for i in range(int(n.split()[0]))]

arr = [x[:] for j in range(int(n.split()[0]))]  # 使用切片复制，避免引用问题


def King(n, m):
    n = n - 1
    m = m - 1
    if 0 <= n < len(arr) and 0 <= m < len(arr[0]):
        # print(n, m)
        arr[n][m] = 2
        if 0 <= m+1 < len(arr[0]):
            arr[n][m+1] = 1
        if 0 <= m-1 < len(arr[0]):
            arr[n][m-1] = 1
        if 0 <= n+1 < len(arr):
            arr[n+1][m] = 1
            if 0 <= m+1 < len(arr[0]):
                arr[n+1][m+1] = 1
            if 0 <= m-1 < len(arr[0]):
                arr[n+1][m-1] = 1
        if 0 <= n-1 < len(arr):
            arr[n-1][m] = 1
            if 0 <= m+1 < len(arr[0]):
                arr[n-1][m+1] = 1
            if 0 <= m-1 < len(arr[0]):
                arr[n-1][m-1] = 1


King(int(n.split()[1]), int(n.split()[2]))
# for i in arr:
#     print(i)


def Queen():
    resoult = 0
    resoult = (int(n.split()[0]))**2 - \
        ((3*len(arr)) if (3*len(arr) > 0) else 0)
    print(resoult)


Queen()
