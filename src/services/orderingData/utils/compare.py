from ..bubble_sort import bubble_sort
from ..selection_sort import selection_sort
from ..insertion_sort import insertion_sort
from ..shell_sort import shell_sort
from ..merge_sort import merge_sort
from ..quick_sort import quick_sort
from time_spend import timeSpent
from random_array import randomArray

def compare(chooses, t):
    methods = {
        1: bubble_sort,
        2: selection_sort,
        3: insertion_sort,
        4: shell_sort,
        5: merge_sort,
        6: quick_sort
    }

    arr = randomArray(t)

    print(f"comparing: {methods[chooses[0]].__name__} with {methods[chooses[1]].__name__}")

    t1 = timeSpent(methods[chooses[0]], arr)
    t2 = timeSpent(methods[chooses[1]], arr)

    print(f"method: {methods[chooses[0]].__name__} took {t1:.6f} segundos")
    print(f"method: {methods[chooses[1]].__name__} took {t2:.6f} segundos")

    if t1 > t2:
        print(f"{methods[chooses[1]].__name__} was faster")
    elif t1 < t2:
        print(f"{methods[chooses[0]].__name__} was faster")
    else:
        print("the methods took the same time")