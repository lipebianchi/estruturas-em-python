class stackLifo:
    def __init__(self):
        self.stack = []
        self._size = 0

    def push(self, elem):
        self._size += 1
        self.stack.append(elem)


    def pop(self):
        if len(self.stack) != 0:
            self._size -= 1
            self.stack.pop(len(self.stack) - 1)
        else:
            raise IndexError('the queue is empty')
        
    def __len__(self):
        return self._size
        
    def __getitem__(self, index): 
        if len(self.stack) != 0:
            return self.stack[index]
        raise IndexError("list index out of range")
        
    def __repr__(self):
        r = ''
        for i in range(len(self.stack)):
            if i == 0:
                r = r +  '[ ' + str(self.stack[i]) + ', '
            elif len(self.stack) - 1 == i:
                r = r + str(self.stack[i]) + ' ]'
            else:
                r = r + str(self.stack[i]) + ', '
        return r
    
    def __str__(self):
        return self.__repr__()

        
    