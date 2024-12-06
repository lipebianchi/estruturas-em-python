import time

def timeSpent(f, l, show = 0):
    start_time = time.time()
    arr = f(list(l))
    end_time = time.time()
    if show == 1:
        print(f"time spent in {f.__name__}: {end_time - start_time:.6f} seconds")
        print(f"\nORDERED ARRAY: {arr}\n")
        return
    return end_time - start_time