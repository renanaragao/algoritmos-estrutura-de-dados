# Notas

- RAFT: algoritmo de sistema distribuídos;
- PAXOS: Algoritmos de sistemas distribuídos;
- Heurísticas e algoritmos de aproximação;

# Classificação de problemas de decisão

- Solucionável em tempo polinomial ( P )
  - Quando se tem um problema solucionável em tempo polinomial, temos um problema que está no conjunto de **P**.
    - Ex.: verificar se um telefone existe em uma lista telefônica. Se a lista não está ordenada o tempo do algoritmo é linear O(n), se estiver ordenada o algoritmo é O(log n).

- Verificável em tempo polinomial ( NP )
  - Problemas que não são solucionáveis em **P** são verificáveis em **NP**.
    - Ex.: Sudoku
- NP-Hard
  - Ex.: Xadrez
- NP-Completo
  - Problema **C** está em **NP**. Todo problema **NP** é redutível para **C** em tempo polinomial.

Se eu posso resolver um problema em **P** também posso verificar em **NP**, logo todo algoritmo que faz parte do conjunto de **P** também faz parte do conjunto de **NP**.
