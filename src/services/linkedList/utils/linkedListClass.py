from .node import Node

class LinkedList:
    # iniciando a lista.
    def __init__(self):
        self.head = None
        self._size = 0
    
    # método de inserção na lista
    def append(self, elem):
        if self.head: # se a lista já tiver algum valor
            pointer = self.head 
            while(pointer.next):
                pointer = pointer.next
            pointer.next = Node(elem)
        else: # caso a lista iniciando esteja vazia
            self.head = Node(elem)
        self._size += 1 # adiciona +1 ao tamanho da lista

    def _getNode(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range") # caso o índice passado seja maior q o tamanho da lista
        return pointer
    
    def __len__(self): # permite que reconheça a linkedList como uma lista padrão do python, tornando possível a utilização do comando len(minhaLista)
        return self._size
    

    def __getitem__(self, index): # permite o tratamento como uma lista padrão do python, tornando possível utilizar a expressão: a = lista[1] 
        pointer = self._getNode(index)
        if pointer:
            return pointer.data
        raise IndexError("list index out of range") # caso o índice passado seja maior q o tamanho da lista

    def __setitem__(self, index, elem): # permite o tratamento como uma lista padrão do python, tornando possível utilizar a expressão: lista[2] = 3
        pointer = self._getNode(index)
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range") # caso o índice passado seja maior q o tamanho da lista
        
    def indexOf(self, elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f"{elem} is not in list")
    
    def insert(self, index, elem):
        node = Node(elem)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._getNode(index-1)
            node.next = pointer.next
            pointer.next = node
        self._size += 1

    def remove(self, elem):
        if self.head == None:
            raise ValueError(f"{elem} is not in list")
        elif self.head.data == elem:
            self.head = self.head.next
            self._size -= 1
            return True
        else:
            previous = self.head
            pointer = self.head.next
            while(pointer):
                if pointer.data == elem:
                    previous.next = pointer.next
                    pointer.next = None
                previous = pointer
                pointer = pointer.next
            self._size -= 1
            return True
        raise ValueError(f"{elem} is not in list")
        
    
    def __repr__(self):
        r = ""
        pointer = self.head
        while(pointer):
            if pointer.next:
                r = r + str(pointer.data) + " -> "
                pointer = pointer.next
            else:
                r = r + str(pointer.data) + " -> NULL"
                pointer = pointer.next
        return r
    
    def __str__(self):
        return self.__repr__()