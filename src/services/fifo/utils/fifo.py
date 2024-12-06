class queueFifo:
    def __init__(self):
        self.fila = []
        self.size = 0

    def enqueue(self, data):
        self.fila.append(data)
        self.size += 1

    def dequeue(self):
        if len(self.fila) != 0:
            self.size -= 1
            self.fila.pop(0)
        else:
            raise IndexError('the queue is empty')
        
    def __len__(self):
        return self.size
        
    def __getitem__(self, index): 
        if len(self.fila) != 0:
            return self.fila[index]
        raise IndexError("list index out of range") 
    
    def __setitem__(self, index, elem): # permite o tratamento como uma lista padrão do python, tornando possível utilizar a expressão: lista[2] = 3
        if len(self.fila) != 0:
            self.fila[index] = elem
        else:
            raise IndexError("list index out of range") # caso o índice passado seja maior q o tamanho da lista
        
    def __repr__(self):
        r = ''
        for i in range(len(self.fila)):
            if i == 0:
                r = r +  '[ ' + str(self.fila[i])
            elif len(self.fila) - 1 == i:
                r = r + str(self.fila[i]) + ' ]'
            else:
                r = r + str(self.fila[i]) + ', '
        return r
    
    def __str__(self):
        return self.__repr__()

fila = queueFifo()

print(len(fila))

        
    