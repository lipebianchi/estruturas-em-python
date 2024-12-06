import random

def randomArray(t):
    array = []
    for i in range(t):
        n = random.randint(0, 1000000)
        array.append(n)
    return array