def shell_sort(l):
    n = len(l)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = l[i]
            j = i
            while j >= gap and l[j - gap] > temp:
                l[j] = l[j - gap]
                j -= gap
            l[j] = temp
        gap //= 2
    return l