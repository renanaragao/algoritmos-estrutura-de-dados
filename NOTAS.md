# Notas

- RAFT: algoritmo de sistema distribuídos;
- PAXOS: Algoritmos de sistemas distribuídos;
- Heurísticas e algoritmos de aproximação;

# Conceitos Fundamentais

## Classificação de problemas de decisão

- Solucionável em tempo polinomial ( P )
  - Quando se tem um problema solucionável em tempo polinomial, temos um problema que está no conjunto de **P**.
    - Ex.: verificar se um telefone existe em uma lista telefônica. Se a lista não está ordenada o tempo do algoritmo é linear $O(n)$, se estiver ordenada o algoritmo é $O(log n)$.

- Verificável em tempo polinomial ( NP )
  - Problemas que não são solucionáveis em **P** são verificáveis em **NP**.
    - Ex.: Sudoku
- NP-Hard
  - Ex.: Xadrez
- NP-Completo
  - Problema **C** está em **NP**. Todo problema **NP** é redutível para **C** em tempo polinomial.

Se eu posso resolver um problema em **P** também posso verificar em **NP**, logo todo algoritmo que faz parte do conjunto de **P** também faz parte do conjunto de **NP**.

# Alguns Algoritmos

Ordenar é importante, pois reduz o tempo das consultas.

O limite de performance de um algoritmo de ordenação é $O(nlogn)$.

## BUBBLESORT

- Pior caso: $O(n^2)$;
- Caso médio: $O(n^2)$;
- Melhor caso: $O(n)$.

## QUICKSORT

- Pior caso: $O(n²)$;
- Caso médio: $O(n log n)$;
- Melhor caso: $O(n log n)$.

## MERGESORT

- Pior caso: $O(n log n)$
- Caso médio: $O(n log n)$;
- Melhor caso: $O(n log n)$.
  
## HEAPSORT

- Pior caso: $O(n log n)$
- Caso médio: $O(n log n)$;
- Melhor caso: $O(n log n)$.

Combina algoritmo com estrutura de dados. Baseado na estrutura de dados "binary HEAP" (com propriedade HEAP-MAX).
O HEAPSORT tem uma representação em árvores, mas pode ser representada em array:

- O índice do nó-pai para o nó $j$ será $(j-1/2)$;
- O índice do nó-filho-esquerda para o nó $j$ será $(2*j)+1$;
- O índice do nó-filho-direito para o nó $j$ será $(2*j)+2$.

Uma **BINARy HEAP** pode ser "MIN HEAP" ou "MAX HEAP":

- **MIN HEAP**: o valor do nó-pai é menor que o valor dos nós-filhos;
- **MAX HEAP**: o valor do nó-pai é maior que o valor dos nós-filhos.

A **BINARY HEAP** é fundamental para implementar o HEAPSORT, além disso, ela é uma das principais alternativas para implementação de um **PIRORITY QUEUE**.

# Análise de Algoritmos e Notação Big O

Mesmo os algorítmos com mesmo Big O podem ter desempenhos diferentes:

![](big-o-nao-eh-suficiente-para-definir-performance.png)

Quantos passos são necessaŕios para esse algoritmo completar?

![](search-algoritmo.png)

A complexidade do algoritmo está relacionada com o tempo que você precisa pra processar e geralmente a resposta está relacionda com o pior caso.
No caso do exemplo a complexidade é $O(n)$ = linear.

Busca binária tem complexidade $O(log n)$, ou seja, a cada iteração o número de elementos que você tem que processar é reduzido pela metade:

![](busca-binaria.png)
