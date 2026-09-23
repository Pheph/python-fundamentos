# Python: exercícios de aula

Os exercícios de Python do curso Técnico Especialista em Gestão de Informação e Ciência dos Dados (IEFP Aveiro / C-EFAV), pela ordem em que foram feitos.

Estão aqui como registo do percurso: começam no `print` e acabam a ler ficheiros e a separar dados de texto.

## O percurso

| Ficheiros | Tema | O que se aprende |
|---|---|---|
| `01` a `06` | Base da linguagem | `print`, variáveis, operadores aritméticos, `input` e strings |
| `07` a `09` | Decisão | `if`, `elif` e `else`, com o dia da semana a partir de um número |
| `10` a `14` | Repetição | `for` e `while`, tabuada, triângulos de asteriscos e o primeiro menu interativo |
| `15` | Erros | `try` e `except` a proteger a leitura do `input` |
| `16` | Projeto integrador | Máquina de bebidas, o exercício maior do conjunto |
| `20` a `22` | Strings | Percorrer caracteres, tabela ASCII e manipulação de nomes |
| `27` a `33` | Listas | Médias, maior e menor valor, somas, filtros por condição, temperaturas e números aleatórios |
| `35`, `36`, `38` | Ficheiros | Ler um `.txt` inteiro, linha a linha e com ciclo; converter valores; separar nomes de emails |

## Destaque: máquina de bebidas

O `16_maquina_bebidas.py` é o exercício que junta tudo o que veio antes, em 189 linhas:

* Menu de bebidas com validação da opção escolhida
* Cálculo do troco a partir das moedas disponíveis, de 2 euros a 5 cêntimos
* Controlo do stock de moedas no moedeiro, que desce à medida que a máquina dá troco
* Menu administrativo escondido, acessível pelo código `123`, para ver o dinheiro em caixa e desligar a máquina
* Ciclos encaixados, com o programa a voltar sempre ao menu principal
* `match` e `case` para as bebidas e para as moedas, em vez de uma escada de `elif`

## Correr os exercícios

Python 3.10 ou superior, sem dependências para instalar. A versão mínima vem do `match` e `case`, usados no `16_maquina_bebidas.py` e no `28_idade.py`.

```bash
python3 01_print.py
```

Os exercícios de ficheiros leem dados da própria pasta:

* `36_ler_contas.py` lê o `35_valores.txt`
* `38_ler_26_revisoes.py` lê o `formandos.txt`

O `formandos.txt` tem nomes e endereços inventados. Os dados reais da turma não estão aqui.

## Nota sobre o código

Está como foi escrito na aula, sem arrumações posteriores. Onde aparece `except:` sem tipo de exceção, ou `subprocess.run('cls')` a limpar o ecrã (que só funciona no Windows, onde as aulas decorrem), é assim que estava no dia. Preferi deixar o registo verdadeiro a maquilhar exercícios de aprendizagem.
