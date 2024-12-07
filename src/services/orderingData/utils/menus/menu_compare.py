from ..compare import compare

def menuCompare(chooses, count = 0):
    if count == 2:
        t = int(input("Escolha o tamanho do array: "))
        return compare(chooses, t)

    print("Escolha qual método deseja comparar: \n1 - Bubble Sort\n2 - Select Sort\n3 - Insertion Sort\n4 - Shell Sort\n5 - Merge Sort\n6 - Quick Sort\n")

    c = int(input())

    chooses.append(c)
    return menuCompare(chooses, count + 1)