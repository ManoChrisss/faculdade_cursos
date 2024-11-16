# conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
#  tipos imutáveis e primitivos:
# str, int, float, bool
print(int('1'), type(int('1')), end='\n\n')

print(type(float('1') + 1), end='\n\n')

print(bool(' '), end='\n\n')

print(str(11) + 'b', end='\n\n')

print(int('1'), type(int('1')), end='\n\n')

print(float('11.2') + 1, end="\n\n")




# Em Python, tipos imutáveis são aqueles cujos valores não podem ser alterados após sua criação. Isso significa que, ao tentar modificar o valor, um novo objeto é criado com o novo valor, enquanto o antigo permanece inalterado. Esses tipos incluem:

# 1. int (números inteiros):
# Exemplo: a = 5


# 2. float (números de ponto flutuante):
# Exemplo: b = 3.14


# 3. bool (booleanos):
# Exemplo: c = True


# 4. str (cadeias de caracteres):
# Exemplo: d = "texto"


# 5. tuple (tuplas, listas imutáveis):
# Exemplo: e = (1, 2, 3)


# 6. frozenset (versão imutável de set):
# Exemplo: f = frozenset([1, 2, 3])