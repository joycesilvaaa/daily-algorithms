# O Problema:
# Dada uma string, encontre o primeiro caractere que não se repete nela e retorne o seu índice. Se todos se repetirem, retorne -1.
# Exemplos:
# "popeye" -> O 'p' repete, o 'o' é o primeiro que aparece só uma vez. (Índice 1)
# "swiss" -> O 's' repete, o 'w' é o primeiro único. (Índice 1)
# "aabb" -> Todos se repetem. (Retorno -1)

from collections import Counter

def unique_char(values: str) -> int:
    map = Counter(values) 
    
    for index, value in enumerate(values):
        if map.get(value) == 1:
            return index
    return -1

print(unique_char("popeye")) # 1
print(unique_char("swiss")) # 1
print(unique_char("aabb")) # -1
print(unique_char("test")) # 1



        