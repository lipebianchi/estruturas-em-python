from ..orderingData.utils.menus.menu_ordering import menu_ordering
from ..linkedList.utils.menu_list import menu_list
from ..fifo.utils.menu_fifo import menu_fifo
from ..lifo.utils.lifoMenu import menu_lifo
from ..searchAlgorithms.utils.menu_search import menu_search
from ..terminal_clear.terminal_clear import clear_terminal

def menu():
    choise = 1
    while choise != 0:
        choise = int(input("0 - Sair\n1 - Lista\n2 - Fila\n3 - Stack\n4 - Ordenação de dados\n5 - Algorítmo de busca\nEscolha qual estrutura de dados deseja utilizar: "))
        match choise:
            case 0:
                print("Obrigado por utilizar o programa!")
                return
            case 1:
                clear_terminal()
                menu_list()
            case 2:
                clear_terminal()
                menu_fifo()
            case 3:
                clear_terminal()
                menu_lifo()
            case 4:
                clear_terminal()
                menu_ordering()
            case 5:
                clear_terminal()
                menu_search()
            case _:
                clear_terminal()
                print("Digite um valor válido!")