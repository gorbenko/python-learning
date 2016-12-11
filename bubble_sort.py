def sort_1(a):
    length = len(a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if a[i] > a[i + 1]:
                sorted = False
                a[i], a[i + 1] = a[i + 1], a[i]
    return a


def sort_2(a):
    for i in reversed(range(len(a))):  # 9, 8, ..., 0
        for j in range(1, i + 1):  # 1 -> 9, 8, ..., 0
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]
    return a
