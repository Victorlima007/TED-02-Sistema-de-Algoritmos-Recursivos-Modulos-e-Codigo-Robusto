# TED 02 – Central Recursiva

**Integrantes da dupla**

- Jadson Paz Sales - 26.1.13308
- Victor Gabriel Guida Lima - 26.1.13209

## Descrição

Operações suportadas:

| Operação | Entrada | Saída |
|---|---|---|
| MDC | `M A B` (inteiros positivos) | `MDC = X` |
| Soma dos dígitos | `S N` (inteiro não negativo) | `SOMA = X` |
| Operação desconhecida | qualquer outra letra | `ERRO: OperacaoInvalida` |
| Valores inválidos | ex.: `M 0 25`, `S -50`, `M 5`, `S abc` | `ERRO: EntradaInvalida` |

A primeira linha da entrada contém `Q` (quantidade de operações) e as `Q`
linhas seguintes contêm uma operação cada.

## Como executar

```bash
python executar.py < exemplos/entrada1.txt
```

```bash
python executar.py --resumo < exemplos/entrada2.txt
```

### Testes automatizados

```bash
python -m unittest -v
```
para executar algum exemplo no powershell: Get-Content .\exemplos\entrada1.txt | python .\executar.py

## Estrutura do projeto

```
TED02_CentralRecursiva/
├── executar.py          
├── beecrowd_submissao.py
├── central_recursiva/   
│   ├── __init__.py
│   ├── excecoes.py      
│   ├── algoritmos.py    
│   ├── validador.py     
│   ├── processador.py   
│   └── main.py          
├── tests/test_central_recursiva.py
└── exemplos/            
```

## Módulos

| Módulo | Responsabilidade |
|---|---|
| `excecoes.py` | Define as exceções personalizadas e o texto de erro de cada uma. |
| `algoritmos.py` | Contém apenas os cálculos recursivos, sem validação nem I/O. |
| `validador.py` | Identifica a operação, converte os textos em inteiros e verifica o domínio (levanta exceções, não imprime nada). |
| `processador.py` | Une validador + algoritmos e trata as exceções com `try`/`except`/`finally`. |
| `main.py` | Lê a entrada padrão, chama o processador para cada operação e imprime. |

Cada módulo tem uma única responsabilidade, então `algoritmos.py` pode ser
reutilizado ou testado sem depender do resto do sistema.

## Algoritmos recursivos

### 1. MDC – algoritmo de Euclides (`mdc(a, b)`)

- **Caso base:** se `b == 0`, o MDC é `a`.
- **Passo recursivo:** `mdc(a, b) = mdc(b, a mod b)`.

O segundo argumento diminui a cada chamada até chegar a 0, o que garante o
término. Exemplo: `mdc(48, 18) → mdc(18, 12) → mdc(12, 6) → mdc(6, 0) = 6`.
Para valores até 10⁹ a profundidade é de poucas dezenas de chamadas.

### 2. Soma dos dígitos (`soma_digitos(n)`)

- **Caso base:** se `n < 10`, a soma é o próprio `n`.
- **Passo recursivo:** `soma_digitos(n) = (n mod 10) + soma_digitos(n div 10)`.

Separa o último dígito e repete para o restante do número. Exemplo:
`soma_digitos(2026) = 6 + 2 + 0 + 2 = 10`. Para `N` até 10¹⁸ são no máximo
19 chamadas.

## Exceções personalizadas

Todas herdam, direta ou indiretamente, de `Exception`:

```
Exception
└── CentralRecursivaError        base das exceções do sistema
    ├── OperacaoInvalidaError    operação diferente de M ou S
    └── EntradaInvalidaError     operação conhecida com valores inválidos
```

- **`OperacaoInvalidaError`** — levantada em `validador.identificar_operacao()`
  quando a operação não é `M` nem `S`. Saída: `ERRO: OperacaoInvalida`.
- **`EntradaInvalidaError`** — levantada em `validador.py` quando faltam ou
  sobram números, o valor não é um inteiro (`abc`, `1.5`, `+5`), ou está fora
  do domínio (`M` com zero/negativo, `S` com negativo). Saída:
  `ERRO: EntradaInvalida`.

### Fluxo

1. `validador.py` **verifica** e **levanta** (`raise`) a exceção adequada.
2. `processador.py` **captura** (`try/except CentralRecursivaError`) e devolve
   a mensagem do erro.
3. O bloco **`finally`** sempre executa (com sucesso ou erro): em
   `processar_linha()` atualiza os contadores de linhas processadas/com erro e,
   em `main()`, garante o `flush` da saída.


