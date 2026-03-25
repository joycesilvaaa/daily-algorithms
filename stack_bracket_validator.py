# Problema:
# Você recebeu uma string contendo apenas os caracteres (, ), {, }, [ e ].
# Sua tarefa é escrever um algoritmo que diga se a sequência é VÁLIDA.
# Uma sequência é válida se:
# As aberturas são fechadas pelo mesmo tipo de fechamento.
# As aberturas são fechadas na ordem correta.
# Todo fechamento tem uma abertura correspondente anterior.

# Exemplos:
# ()[]{} -> Válido
# ([{}]) -> Válido (o {} está dentro do [], que está dentro do ())
# (] -> Inválido (abriu parêntese, tentou fechar colchete)
# ([)] -> Inválido (ordem errada: o ) tentou fechar antes do ])

# ESTRUTURA: STACK (Pilha)
# TIPO: LIFO (Last-In, First-Out) -> O último que entra é o primeiro que sai.

# Lógica Inicial (Descartada):
# Tentar tratar casos isolados (vizinhos vs extremidades) usando FIFO e LIFO. 
# Motivo: Complexidade desnecessária e falha em casos mistos.

# Lógica Final (Implementada):
# Combinação de STACK + HASHMAP.
# - HASHMAP: Armazena os pares (Chave = Fechamento / Valor = Abertura).
# - STACK: Armazena apenas as ABERTURAS encontradas na string.
# - PROCESSO: Ao encontrar um fechamento, verifica-se se ele combina com 
#   o topo da Stack. Se a Stack terminar vazia, a sequência é válida.

def validation(values: str) -> bool:
    stack = []
    map = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for value in values:
        if map.get(value):
            if stack and stack[-1] == map.get(value) :
                stack.pop()
            else:
                return False 
        else:
            stack.append(value)
    
    return not stack

print(validation("()[]{}")) # True
print(validation("([{}])")) # True
print(validation("([)]"))   # False
print(validation("]")) # False
print(validation("(")) # False
print(validation("{}")) # True
            

            

