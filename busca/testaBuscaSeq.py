from buscas import Busca
b = Busca()
x = [3, 5, 6, 7, 1, 2, 8]
v = int(input('Digite o valor a pesquisar: '))
r = b.buscaSequencial(x, v)
if r > -1:
  print(v, 'está na posição', r, 'do vetor.')
else:
  print(v, 'não está no vetor')