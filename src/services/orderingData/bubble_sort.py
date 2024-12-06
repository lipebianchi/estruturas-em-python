def bubble_sort(l):
    t = len(l)

    for i in range(t):
        for j in range(0, t - i - 1):
            if l[j] > l[j + 1]:
                l[j], l[j+1] = l[j+1], l[j]
    return l