from ..create import createLinkedList
from ...terminal_clear.terminal_clear import clear_terminal

lista = createLinkedList()
def menu_list():
    choise = 1
    while choise != 0:
        choise = int(input("0 - Sair\n1 - Adicionar no final da lista\n2 - Adicionar em um índice especifico da lista\n3 - Remover da lista\n4 - Encontrar índice de um elemento\n5 - imprimir lista\n6 - Imprimir tamanho da lista\nEscolha oque deseja fazer: "))
        
        match choise:
            case 0:
                return
            case 1:
                clear_terminal()
                elem = int(input("Digite o valor que deseja inserir: "))
                lista.append(elem)
            case 2:
                clear_terminal()
                try:
                    index = int(input("Digite o indice na qual deseja inserir: "))
                    elem = int(input("Digite o valor que deseja inserir: "))
                    lista.insert(index, elem)
                except IndexError:
                    print("Esse índice não existe na lista!")
            case 3:
                clear_terminal()
                elem = int(input("Digite o valor que deseja remover: "))
                lista.remove(elem)
            case 4:
                clear_terminal()
                try:
                    elem = int(input("Digite o valor que deseja descobrir em que índice da lista se encontra."))
                    print(lista.indexOf(elem))
                except ValueError:
                    print("Erro: esse valor não existe na lista.")
            case 5:
                clear_terminal()
                print(lista)
            case 6:
                clear_terminal()
                print(len(lista))
            case _:
                clear_terminal()
                print("Digite um valor válido!")
