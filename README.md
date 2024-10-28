## Simulador de Máquina de Turing 

Projeto de um simulador de Máquina de Turing na linguagem Python.

## Funcionalidades

- Leitura de máquinas de Turing a partir de arquivos JSON.
- Leitura de fitas de entrada a partir de arquivos de texto.
- Execução da máquina de Turing com transições definidas.
- Geração de resultados da simulação em um arquivo de saída, indicando se a entrada foi aceita ou rejeitada.

## Estrutura dos Arquivos

Para usar o simulador, são necessários dois arquivos.

### Arquivo JSON

O arquivo JSON deve conter os seguintes campos:

- `initial`: Estado inicial.
- `final`: Lista de estados de aceitação.
- `white`: Simbolo branco que representa espaços em branco na fita.
- `transitions`: Lista de transições, onde cada transição é um objeto com os campos `from`, `to`, `read`, `write`, e `dir`.

### Exemplo de arquivo JSON

    ```json
    {
        "initial" : 0,
        "final" : [4],
        "white" : "_",
        "transitions" : [
            {"from": 0, "to": 1, "read": "a", "write": "A", "dir":"R"},
            {"from": 1, "to": 1, "read": "a", "write": "a", "dir":"R"},
            {"from": 1, "to": 1, "read": "B", "write": "B", "dir":"R"},
            {"from": 1, "to": 2, "read": "b", "write": "B", "dir":"L"},
            {"from": 2, "to": 2, "read": "B", "write": "B", "dir":"L"},
            {"from": 2, "to": 2, "read": "a", "write": "a", "dir":"L"},
            {"from": 2, "to": 0, "read": "A", "write": "A", "dir":"R"},
            {"from": 0, "to": 3, "read": "B", "write": "B", "dir":"R"},
            {"from": 3, "to": 3, "read": "B", "write": "B", "dir":"R"},
            {"from": 3, "to": 4, "read": "_", "write": "_", "dir":"L"}      
        ]
    }

### Exemplo de arquivo de entrada e resultado esperado

Entrada:
    
    aabb

Resultado esperado:

    AABB_

ou

Entrada:
    
    aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbb

Resultado esperado:

    AAAAAAAAAAAAAAAAAAAABBBBBBBBBBBBBBBBBBBB_

### Saída da Simulação

O simulador imprimirá 1 ou 0 no terminal, indicando se a entrada foi aceita ou rejeitada...

1: A entrada foi aceita pela máquina de Turing (ou seja, a execução chegou a um estado de aceitação).

0: A entrada foi rejeitada (ou seja, não há transições possíveis que permitam que a máquina chegue a um estado de aceitação).
