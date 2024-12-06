def selection_sort(l):
    t = len(l)
    for i in range(t):
        min_Idx = i
        for j in range(i + 1, t):
            if l[j] < l[min_Idx]:
                min_Idx = j
        l[i], l[min_Idx] = l[min_Idx], l[i]
    return l