def linear_search(l, elem):
    n = len(l)
    cout = 0
    for i in range(n):
        cout += 1
        if elem == l[i]:
            print(f"Elemento encontrado no índice: {cout - 1}\nQuantidade de elementos percorridos até encontrar: {cout}")
            return
    print("Elemento não existente no array!")