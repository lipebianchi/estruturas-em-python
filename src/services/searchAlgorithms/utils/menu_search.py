from ..binary_search import binary_search
from ..linear_search import linear_search
from ...orderingData.utils.random_array import randomArray
from ...orderingData.quick_sort import quick_sort
from ...terminal_clear.terminal_clear import clear_terminal


def menu_search():
    choice = 1    
    while choice != 0:
        choice = int(input("0 - Sair\n1 - Busca Sequencial\n2 - Busca Binária\nQual busca deseja utilizar?: "))
        if choice == 0:
            return
        
        t = int(input("Deseja escolher um array aleatório de que tamanho?"))

        arr = randomArray(t)

        match choice:
            case 1:
                clear_terminal()
                elem = int(input("Que valor deseja checar se existe no array?: "))
                linear_search(arr, elem)
            case 2:
                clear_terminal()
                print("Ordenando o array...")
                ordered_arr = quick_sort(arr)
                elem = int(input("Que valor deseja checar se existe no array?: "))
                binary_search(ordered_arr, elem)
            case _:
                clear_terminal()
                print("escolha uma opção válida!")
