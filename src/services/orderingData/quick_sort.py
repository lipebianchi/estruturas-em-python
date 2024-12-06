def quick_sort(l):
    if len(l) <= 1:
        return l  
    
    pivô = l[-1]
    
    minors = [x for x in l[:-1] if x <= pivô]
    biggers = [x for x in l[:-1] if x > pivô]
    
    return quick_sort(minors) + [pivô] + quick_sort(biggers)