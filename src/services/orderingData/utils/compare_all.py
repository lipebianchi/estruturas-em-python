from ..bubble_sort import bubble_sort
from ..selection_sort import selection_sort
from ..insertion_sort import insertion_sort
from ..shell_sort import shell_sort
from ..merge_sort import merge_sort
from ..quick_sort import quick_sort
from time_spend import timeSpent
from random_array import randomArray

def compare_all():

    methods = {
        1: bubble_sort,
        2: selection_sort,
        3: insertion_sort,
        4: shell_sort,
        5: merge_sort,
        6: quick_sort
    }

    print("Choose the size of your array: ")
    t = int(input())
    l = randomArray(t)
    
    print(f"\nUNORDERED ARRAY: {l}\n")

    cout = 1
    for i, method in methods.items():
        if cout == len(methods):
            timeSpent(method, l, 1)
        else:
            time = timeSpent(method, l)
            print(f"time spent in {method.__name__}: {time:.6f} seconds\n")
        cout+=1