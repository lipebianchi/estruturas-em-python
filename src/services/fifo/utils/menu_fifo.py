from ..create import createFifo
from ...terminal_clear.terminal_clear import clear_terminal

fila = createFifo()

def menu_fifo():
    choice = 1
    while choice != 0:
        choice = int(input("0 - Sair\n1 - Inserir na fila\n2 - Remover da fila\n3 - Imprimir fila\n4 - imprimir tamanho da fila\nEscolha oque deseja utilizar: "))

        match choice:
            case 0:
                return
            case 1:
                clear_terminal()
                elem = int(input("Insira o valor que deseja inserir: "))
                fila.enqueue(elem)
            case 2:
                elem = fila[0]
                fila.dequeue()
                clear_terminal()
                print(f"Elemento retirado da fila: {elem}")
            case 3:
                clear_terminal()
                print(fila)
            case 4:
                clear_terminal()
                print(len(fila))
            case _:
                clear_terminal()
                print("Digite um valor válido")