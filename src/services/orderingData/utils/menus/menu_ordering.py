from ...bubble_sort import bubble_sort
from ...selection_sort import selection_sort
from ...insertion_sort import insertion_sort
from ...shell_sort import shell_sort
from ...merge_sort import merge_sort
from ...quick_sort import quick_sort
from ..random_array import randomArray
from ..compare_all import compare_all
from ..time_spend import timeSpent
from menu_compare import menuCompare


def menu_ordering():
    print("Choose which method you want to use: \n1 - Bubble Sort\n2 - Select Sort\n3 - Insertion Sort\n4 - Shell Sort\n5 - Merge Sort\n6 - Quick Sort\n7 - Compare methods\n8 - Compare all methods\n")

    methods = {
        1: bubble_sort,
        2: selection_sort,
        3: insertion_sort,
        4: shell_sort,
        5: merge_sort,
        6: quick_sort
    }


    c = int(input())

    if not c == 7 and not c == 8:
        print("Choose the size of your array\n")
        t = int(input())
        l = randomArray(t)
        f = methods[c]
        time = timeSpent(f, l)
        print(f"time spent in {f.__name__}: {time:.6f} seconds")
    elif c == 7:
        chooses = []
        menuCompare(chooses)
    else:
        compare_all()

    