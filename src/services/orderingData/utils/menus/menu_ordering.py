from ...bubble_sort import bubble_sort
from ...selection_sort import selection_sort
from ...insertion_sort import insertion_sort
from ...shell_sort import shell_sort
from ...merge_sort import merge_sort
from ...quick_sort import quick_sort
from ..random_array import randomArray
from ..compare_all import compare_all
from ..time_spend import timeSpent
from .menu_compare import menuCompare
from ....terminal_clear.terminal_clear import clear_terminal


def menu_ordering():
    print("Escolha qual método de ordenação deseja usar: \n0 - Sair\n1 - Bubble Sort\n2 - Select Sort\n3 - Insertion Sort\n4 - Shell Sort\n5 - Merge Sort\n6 - Quick Sort\n7 - Compare methods\n8 - Compare all methods\n")

    methods = {
        1: bubble_sort,
        2: selection_sort,
        3: insertion_sort,
        4: shell_sort,
        5: merge_sort,
        6: quick_sort
    }


    c = int(input())

    if c == 0:
        return

    if not c == 7 and not c == 8:
        print("Escolha o tamanho do array\n")
        t = int(input())
        l = randomArray(t)
        f = methods[c]
        time = timeSpent(f, l)
        print(f"tempo gasto em {f.__name__}: {time:.6f} seconds")
    elif c == 7:
        chooses = []
        clear_terminal()
        menuCompare(chooses)
    else:
        clear_terminal()
        compare_all()

    