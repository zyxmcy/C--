# 求n!
arr = []


def process_calculate_result(n):
    resoult = calculate(n)
    # 把r里的每一个数存进数组里

    while resoult > 0:
        a = resoult % 10
        arr.append(a)
        resoult = resoult // 10
    arr.reverse()
    for i in range(len(arr)):
        print(arr[i])


def calculate(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 1000:
        return 1000*999*998*calculate(n-3)
    elif n == 999:
        return 999*998*calculate(n-2)
    else:
        return n * calculate(n-1)


if __name__ == '__main__':
    # process_calculate_result(n)
    process_calculate_result(1)
