# Informações

## OS.NAME

A função `os.system` executa comandos do sistema operacional no terminal. No windows, o comando para limpar a tela é `cls`, no Linux e macOS, o comando equivalente é `clear`.

O atributo `os.name` retorna uma string que identifica qual tipo de sistema operacional. Se o sistema for Windows será `nt` (abreviação para _New Tecnology_, o kernel do Windows). Em sistemas baseados em Unix (Linux, macOS), o valor será `posix`.

## LAMBDA

Uma função `lambda` em Python é uma maneira de criar funções curtas e anônimas (sem nome) diretamente no local onde são necessárias, sem usar a palavra-chave `def`.

### Definição Geral

```Python
lambda argumentos: expressão
```

- `argumentos`: Uma lista separada por vírgulas de parâmetros que a função recebe (assim como em funções normais);
- `expressão`: Um único retorno, que é o resultado da função. Não é necessário usar a palavra-chave `return`, pois o valor é retornado automaticamente.

### Como funciona

```Python
# Função lambda que retorna o dobro do número
dobro = lambda x: x * 2
print(dobro(5))  # Saída: 10
```

- `lambda x: x * 2`: define uma função que recebe um argumento (`x`) e retorna um valor de `x * 2`.

- `lambda` é atribuído a variável `dobro`.

- Quando chamamos `dobro(5)`, o valor 5 é passado como argumento para a função `lambda`, e o resultado é `5 * 2 = 10`.
  - OBS: Uma variável pode "receber um argumento" porque a variável contém uma função. Quando chamamos a variável como se fosse uma função, passamos os argumentos para ela. Teoricamente, a variável `dobro` se comporta como uma função.

```Python
comandos = {
    'listar': lambda: listar(tarefas),
    'desfazer': lambda: (desfazer(tarefas, tarefas_undone), listar(tarefas)),
    'refazer': lambda: (refazer(tarefas, tarefas_undone), listar(tarefas)),
    'limpar': limpar_tela
}
```
