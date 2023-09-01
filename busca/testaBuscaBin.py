from buscas import Busca
b = Busca()
x = [1, 2, 3, 5, 6, 7, 8]
v = int(input('Digite o valor a pesquisar: '))
r = b.buscaBinaria(x, v)
if r > -1:
  print(v, 'está na posição', r, 'do vetor.')
else:
  print(v, 'não está no vetor')