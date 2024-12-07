import time

def timeSpent(f, l, show = 0):
    start_time = time.time()
    arr = f(list(l))
    end_time = time.time()
    if show == 1:
        print(f"tempo gasto em {f.__name__}: {end_time - start_time:.6f} segundos")
        print(f"\nArray ordenado: {arr}\n")
        return
    return end_time - start_time