from ..create import createStack
from ...terminal_clear.terminal_clear import clear_terminal

stack = createStack()

def menu_lifo():
    choice = 1
    while choice != 0:
        choice = int(input("0 - Sair\n1 - Inserir na pilha\n2 - Remover da pilha\n3 - Imprimir a pilha\n4 - Imprimir tamanho da pilha\nEscolha oque deseja utilzar: "))

        match choice:
            case 0:
                return
            case 1:
                clear_terminal()
                elem = int(input("Digite o valor a inserir na pilha: "))
                stack.push(elem)
            case 2:
                clear_terminal()
                elem = stack[len(stack) - 1]
                stack.pop()
                print(f"Valor retirado da pilha: {elem}")
            case 3:
                clear_terminal()
                print(stack)
            case 4:
                clear_terminal()
                print(len(stack))
            case _:
                clear_terminal()
                print("escolha uma opção válida!")