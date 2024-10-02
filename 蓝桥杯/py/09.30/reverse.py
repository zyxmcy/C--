def reverse():
    # n = input()
    n = "123 345"
    m = n.split(" ")
    for i in range(len(m)):
        m[i] = int(str(m[i])[::-1])

    print(m[0]+m[1])


if __name__ == '__main__':
    reverse()
