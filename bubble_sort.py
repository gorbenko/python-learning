import random

nums = []

for i in range(10):
    nums.append(random.randint(1, 10))

print(nums)

def bubble(a):
    length = len(a) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if a[i] > a[i + 1]:
                sorted = False
                a[i], a[i + 1] = a[i + 1], a[i]

def bubble_sort(a):
    for i in reversed(range(len(a))):  # 9, 8, ..., 0
        for j in range(1, i + 1):  # 1 -> 9, 8, ..., 0
            if a[j-1] > a[j]:
                a[j], a[j-1] = a[j-1], a[j]

bubble_sort(nums)

print nums