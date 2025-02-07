# Métodos em PYTHON

No Python, o `@classmethod` é um decorador que transforma um método em um método de classe. Isso significa que o método recebe a classe (`cls`) como primeiro argumento, em vez da instância (`self`). Agora, vamos analisar o código e as diferenças entre os tipos de métodos.

---

## 🔹 **Tipos de Métodos no Python**

Dentro de uma classe, podemos ter três tipos principais de métodos:

1. **Métodos de Instância (`method`)**:
   - São os mais comuns.
   - Recebem `self` como primeiro parâmetro, que representa a instância do objeto.
   - Podem acessar e modificar os atributos da instância.

2. **Métodos de Classe (`@classmethod`)**:
   - Recebem `cls` como primeiro parâmetro, que representa a classe.
   - Podem ser chamados tanto na instância quanto diretamente na classe.
   - Podem modificar atributos da classe, mas não diretamente os atributos da instância (a menos que criem uma nova instância).

3. **Métodos Estáticos (`@staticmethod`)**:
   - Não recebem `self` nem `cls` como parâmetro.
   - São independentes da instância e da classe.
   - São usados para funções auxiliares que fazem sentido dentro da classe, mas que não precisam acessar atributos da classe ou da instância.

---

## 🔹 **Explicação do Código**

### **1️⃣ Método de Instância**

```python
def set_user(self, user):
    self.user = user
```

Esse método precisa de uma instância (`self`) para ser chamado e modifica o atributo `user` dessa instância.

---

### **2️⃣ Método de Classe (`@classmethod`)**

```python
@classmethod
def create_with_auth(cls, user, password):
    connection = cls()
    connection.user = user
    connection.password = password
    return connection
```

- Esse método recebe a **classe** como primeiro argumento (`cls`).
- Ele cria uma nova **instância da classe** (`cls()`), define `user` e `password` e retorna essa instância.
- Pode ser chamado diretamente na classe sem precisar criar um objeto antes.

#### 📌 **Diferença para método de instância**

- Um método de instância modifica os atributos de um objeto **já existente**.
- O `@classmethod` pode **criar e configurar uma nova instância** da classe.

---

### **3️⃣ Método Estático (`@staticmethod`)**

```python
@staticmethod
def log(msg):
    print('LOG:', msg)
```

- Esse método não recebe `self` nem `cls`.
- Apenas executa uma função que imprime uma mensagem no console.
- Não interage com a instância nem com a classe.

#### 📌 **Diferença para os outros métodos**

- **Métodos de instância** interagem com os atributos da instância.
- **Métodos de classe** interagem com a classe (`cls`).
- **Métodos estáticos** não interagem com a classe nem com a instância.

---

## 🔹 **Chamadas no Código**

```python
c1 = Connection.create_with_auth('luiz', '1234')
```

Aqui, `create_with_auth` está sendo chamado **diretamente na classe**, sem precisar de uma instância antes. Ele retorna um novo objeto `c1`.

```python
print(Connection.log('Essa é a mensagem de log'))
```

- O método `log` é chamado diretamente na classe, pois é estático.
- Ele apenas imprime uma mensagem e **não retorna nada** (`None` é impresso por causa do `print`).

```python
print(c1.user)
print(c1.password)
```

Exibe os valores `user` e `password` da instância `c1`, que foram configurados no método de classe.

---

## 🔹 **Resumo Rápido**

| Tipo | Parâmetro | Acesso a `self` | Acesso a `cls` | Pode modificar atributos da instância? | Pode modificar atributos da classe? |
|------|-----------|----------------|----------------|--------------------------------|--------------------------------|
| **Método de Instância** | `self` | ✅ | ❌ | ✅ | ❌ |
| **Método de Classe (`@classmethod`)** | `cls` | ❌ | ✅ | ❌ (a menos que crie uma nova instância) | ✅ |
| **Método Estático (`@staticmethod`)** | Nenhum | ❌ | ❌ | ❌ | ❌ |

No Python, dentro de uma classe, podemos ter diferentes tipos de métodos, cada um com sua função específica. Aqui está uma lista completa dos métodos que podem ser usados:

---

## 🔹 **1. Métodos de Instância (Instance Methods)**

São os métodos mais comuns e operam em uma instância da classe. Eles sempre recebem `self` como primeiro argumento.

- `__init__` → Construtor (inicializa atributos)
- `__str__` → Representação amigável (ex.: `print(obj)`)
- `__repr__` → Representação oficial da classe (ex.: debugging)
- `__eq__` → Define `==`
- `__ne__` → Define `!=`
- `__lt__` → Define `<`
- `__le__` → Define `<=`
- `__gt__` → Define `>`
- `__ge__` → Define `>=`
- `__len__` → Define `len(obj)`
- `__call__` → Permite chamar a instância como uma função (`obj()`)
- `__getitem__` → Permite acessar elementos (`obj[index]`)
- `__setitem__` → Permite modificar elementos (`obj[index] = valor`)
- `__delitem__` → Permite deletar elementos (`del obj[index]`)
- `__contains__` → Define `in` (`valor in obj`)

---

## 🔹 **2. Métodos de Classe (`@classmethod`)**

Métodos que operam na classe em vez de uma instância. Recebem `cls` como primeiro argumento.

- `@classmethod def metodo_de_classe(cls):` → Pode acessar/modificar atributos da classe.
- `@classmethod def from_something(cls, *args):` → Métodos auxiliares para criar instâncias de outra forma.

---

## 🔹 **3. Métodos Estáticos (`@staticmethod`)**

Não recebem `self` nem `cls`. São independentes e funcionam como funções normais dentro da classe.

- `@staticmethod def metodo_estatico():` → Não acessa atributos da classe nem da instância.

---

## 🔹 **4. Propriedades (`@property`, `@setter`, `@deleter`)**

Métodos especiais que atuam como atributos controlados.

- `@property` → Transforma um método em uma propriedade somente leitura.
- `@propriedade.setter` → Permite modificar um atributo com regras.
- `@propriedade.deleter` → Define comportamento ao deletar o atributo.

---

## 🔹 **5. Métodos Especiais (`Magic Methods` ou `Dunder Methods`)**

Métodos que começam e terminam com `__`, usados para operações internas.

### **🔸 Inicialização e Representação**

- `__new__` → Criação do objeto antes do `__init__`
- `__init__` → Construtor da classe
- `__del__` → Destrutor da classe
- `__str__` → Representação amigável (`str(obj)`)
- `__repr__` → Representação para debugging (`repr(obj)`)
- `__format__` → Define `format(obj, "formato")`

### **🔸 Operadores Aritméticos**

Permitem modificar o comportamento dos operadores matemáticos.

- `__add__` → `+`
- `__sub__` → `-`
- `__mul__` → `*`
- `__truediv__` → `/`
- `__floordiv__` → `//`
- `__mod__` → `%`
- `__pow__` → `**`
- `__iadd__` → `+=`
- `__isub__` → `-=`
- `__imul__` → `*=`
- `__itruediv__` → `/=`
- `__ifloordiv__` → `//=`
- `__imod__` → `%=`
- `__ipow__` → `**=`

### **🔸 Comparações**

Definem como a classe lida com operadores de comparação.

- `__eq__` → `==`
- `__ne__` → `!=`
- `__lt__` → `<`
- `__le__` → `<=`
- `__gt__` → `>`
- `__ge__` → `>=`

### **🔸 Acesso e Modificação**

- `__getitem__` → `obj[key]`
- `__setitem__` → `obj[key] = value`
- `__delitem__` → `del obj[key]`
- `__contains__` → `x in obj`
- `__iter__` → `for x in obj`
- `__next__` → `next(obj)`
- `__len__` → `len(obj)`

### **🔸 Conversão de Tipos**

- `__int__` → `int(obj)`
- `__float__` → `float(obj)`
- `__bool__` → `bool(obj)`
- `__bytes__` → `bytes(obj)`

### **🔸 Context Manager (`with` Statement)**

- `__enter__` → Executado no início do `with`
- `__exit__` → Executado no final do `with`

### **🔸 Controle de Chamadas**

- `__call__` → Permite que a instância seja chamada como uma função (`obj()`)

---

## 🔹 **Resumo**

| Tipo | Prefixo | Exemplo |
|------|---------|---------|
| **Métodos de Instância** | `self` | `def metodo(self):` |
| **Métodos de Classe** | `cls` | `@classmethod def metodo(cls):` |
| **Métodos Estáticos** | Nenhum | `@staticmethod def metodo():` |
| **Propriedades** | `@property` | `@property def atributo(self):` |
| **Métodos Especiais (`dunder methods`)** | `__nome__` | `def __str__(self):` |

---

## UML
