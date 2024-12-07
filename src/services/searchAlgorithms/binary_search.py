def binary_search(l, elem):
    fim = len(l) - 1
    inicio = 0
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1
        if l[meio] == elem:
            print(f"Elemento: [{elem}] encontrado na posição: {l[meio]}, comparações feitas: {comparacoes}")
            return
        elif l[meio] < elem:
            inicio = meio + 1
        else:
             fim = meio - 1
        comparacoes += 1
    print("Elemento não existente no array!")
    return
    

        

    
