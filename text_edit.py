# O Problema:
# Imagine que você está criando um editor de texto super simples. O usuário pode:
# Digitar um caractere.
# Apagar (Backspace).
# Desfazer (Undo).
# Seu Desafio:
# Dada uma string de comandos onde:

# Letras normais = Digitar.
# # = Backspace (apaga o último caractere digitado).
# * = Undo (desfaz a última ação de digitar ou apagar).

# Exemplos:
# Input: "abc#" -> O c foi apagado pelo #. Resultado: "ab".
# Input: "abc#*" -> O * desfaz o #. Resultado: "abc".
# Input: "popeye**" -> Dois * desfazem o y e o e. Resultado: "pope".


def text_edit(value: str) -> str:
    value_copy = list(value)
    stack = []
    skip = False
    for idx, letter in enumerate(value):
        if skip:
            skip = False
            continue
        if value_copy[idx:idx + 2] == ["#", "*"]:
            skip = True
            continue
        if not letter in ["#", "*"]:
            stack.append(letter)
        elif stack:
            stack.pop()
    return "".join(stack)

print(text_edit("abc#"))  # "ab"
print(text_edit("abc#*")) # abc