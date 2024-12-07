# Projeto de Estruturas de Dados em Python

Este projeto implementa diferentes estruturas de dados listas, pilhas, filas, algoritmos de ordenação (Bubble Sort, Selection Sort, Insertion Sort, Shell Sort, Merge Sort e Quick Sort) e Algorítmos de busca (Busca linear e busca binária) em Python.

## 🎯 Objetivo do Projeto
Este projeto visa explorar e comparar o comportamento das estruturas de dados, dos algoritmos de ordenação e dos algorítmos de busca em diferentes cenários. Ele também permite a análise do desempenho dos algoritmos em termos de tempo de execução, ao comparar métodos de ordenação em listas de diferentes tamanhos.

# 🎆Features

## 🥇 Estruturas de Dados Implementadas
- **Lista**: Implementação de listas encadeadas simples. São fornecidas funções para inserir no inicio, inserir no meio, inserir no fim, remover determinado valor da lista e exibir elementos.
- **Pilha**: Implementação de uma pilha, utilizando o conceito de LIFO (Last In, First Out). Permite operações como imprimir pilha, empilhar e desempilhar elementos.
- **Fila**: Implementação de uma fila, utilizando o conceito de FIFO (First In, First Out). Permite operações de imprimir fila, enfileiramento e desenfileiramento.

## 🥈 Algoritmos de Ordenação

- **Bubble Sort**: Algoritmo de ordenação simples baseado na comparação e troca de elementos adjacentes. A ordenação é realizada em várias passagens pela lista.
- **Selection Sort**: Algoritmo de ordenação que seleciona repetidamente o menor (ou maior) elemento e o coloca na posição correta.
- **Insertion Sort**: Algoritmo de ordenação simples que constrói a lista ordenada gradualmente, inserindo um elemento de cada vez na posição correta, comparando-o com os elementos anteriores.
- **Shell Sort**: Algoritmo de ordenação que melhora o Insertion Sort, utilizando uma sequência de intervalos (gaps) para ordenar elementos distantes antes de refiná-los com gaps menores, acelerando o processo de ordenação.
- **Merge Sort**: Algoritmo de ordenação que tem como principio "dividir para conquistar", utiliza funções recursivas para quebrar o vetor lógicamente em partes menores, para assim que o vetor ficar em tamanho 1, começar a dar merge (mesclar) os vetores menores com os maiores.
- **Quick Sort**: Algoritmo de ordenação eficiente baseado no princípio "dividir para conquistar". Ele escolhe um pivô, particiona os elementos menores à esquerda e os maiores à direita, e aplica recursivamente o mesmo processo nas sublistas até que estejam ordenadas.

## 🥉 Algorítmos de Busca

- **Busca Linear**: Algoritmo de busca que percorre sequencialmente todos os elementos de uma lista até encontrar o valor desejado ou chegar ao final da lista. É simples, mas ineficiente em listas grandes, pois exige a verificação de cada item individualmente.

- **Busca Binária**: Algoritmo eficiente de busca que utiliza o conceito de "dividir para conquistar". Funciona apenas em listas ordenadas, dividindo a lista ao meio a cada iteração e descartando metade dos elementos, até encontrar o valor ou determinar que ele não está presente. 

## 🏅 Tecnologias Utilizadas

- Python;

## 💻 Pré-requisitos

- Python3 instalado em sua máquina.

## 🚀 Rodando localmente

**1. Clone o projeto**

```bash
  git clone https://github.com/lipebianchi/estruturas-em-python.git
```

**2. Entre no diretório do projeto:**

```bash
  cd estruturas-em-python
```

**3. Execute o arquivo:**

```bash
  python ./src/main.py
```


## 📁 Estrutura do projeto


```graphql
estruturas-em-python/
│
├── src/
│   ├── services/                      # Serviços principais
│   │   ├── fifo/                      # Estrutura FIFO
│   │   │   ├── utils/                 # Funções auxiliares FIFO
│   │   │   │   ├── fifo.py           # Implementação da estrutura FIFO
│   │   │   │   └── menu_fifo.py      # Menu de interação FIFO
│   │   │   └── create.py             # Função de criação FIFO
│   │   │
│   │   ├── lifo/                      # Estrutura LIFO
│   │   │   ├── utils/                 # Funções auxiliares LIFO
│   │   │   │   ├── lifo.py           # Implementação da estrutura LIFO
│   │   │   │   └── lifoMenu.py       # Menu de interação LIFO
│   │   │   └── create.py             # Função de criação LIFO
│   │   │
│   │   ├── linkedList/                # Estrutura Linked List
│   │   │   ├── utils/                 # Funções auxiliares Linked List
│   │   │   │   ├── linkedListClass.py # Implementação da classe Linked List
│   │   │   │   ├── menu_list.py      # Menu de interação Linked List
│   │   │   │   └── node.py           # Implementação do nó da lista encadeada
│   │   │   └── create.py             # Função de criação Linked List
│   │   │
│   │   ├── menus/                     # Menus principais do projeto
│   │   │   ├── __init__.py           # Inicialização do módulo menus
│   │   │   └── menu_main.py          # Menu principal do projeto
│   │   │
│   │   ├── orderingData/              # Algoritmos de ordenação e utilitários
│   │   │   ├── utils/                 # Utilitários de ordenação
│   │   │   │   ├── menus/             # Menus específicos de ordenação
│   │   │   │   │   ├── __init__.py   # Inicialização dos menus de ordenação
│   │   │   │   │   ├── menu_compare.py # Menu para comparação de dados
│   │   │   │   │   └── menu_ordering.py # Menu de ordenação
│   │   │   │   └── __init__.py       # Inicialização dos utilitários de ordenação
│   │   │   ├── compare_all.py        # Função para comparar dados de várias fontes
│   │   │   ├── compare.py            # Função para comparação de dados
│   │   │   ├── random_array.py      # Função para geração de arrays aleatórios
│   │   │   └── time_spend.py        # Função para medir o tempo de execução dos algoritmos
│   │   │
│   │   ├── bubble_sort.py            # Algoritmo Bubble Sort
│   │   ├── selection_sort.py         # Algoritmo Selection Sort
│   │   ├── insertion_sort.py         # Algoritmo Insertion Sort
│   │   ├── shell_sort.py             # Algoritmo Shell Sort
│   │   ├── merge_sort.py             # Algoritmo Merge Sort
│   │   └── quick_sort.py             # Algoritmo Quick Sort
│   │   │
│   │   ├── searchAlgorithms/         # Algoritmos de busca
│   │   │   ├── utils/                # Utilitários de busca
│   │   │   │   └── menu_search.py    # Menu de interação para busca
│   │   │   ├── binary_search.py      # Algoritmo de busca binária
│   │   │   └── linear_search.py      # Algoritmo de busca linear
│   │   │
│   │   ├── terminal_clear/           # Função para limpar o terminal
│   │   │   └── terminal_clear.py     # Implementação para limpar o terminal
│   │   │
│   ├── __init__.py                   # Inicialização do módulo principal
│   ├── main.py                       # Ponto de entrada principal do projeto
│
├── README.md                         # Documentação do projeto
```

## 🎓 Conclusão

Ao desenvolver e testar essas implementações, consegui entender melhor o funcionamento de cada algoritmo e estrutura, o que me ajudou a aprimorar meus conhecimentos em análise de algoritmos, modularização, complexidade e resolução de problemas computacionais. Esse projeto foi um recurso valioso para reforçar meus estudos, permitindo visualizar como esses conceitos são aplicados na prática.