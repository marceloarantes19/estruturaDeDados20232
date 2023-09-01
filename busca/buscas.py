class Busca:
  def buscaSequencial(self, x, v):
    n = len(x)
    for i in range(0, n):
      if x[i] == v:
        return i
    return -1
  
  def buscaBinaria(self, x, v):
    li, ls = 0, len(x) - 1
    while li <= ls:
      atual = (li+ls)//2
      if v == x[atual]:
        return atual
      elif v < x[atual]:
        ls = atual - 1
      else:
        li = atual + 1
    return -1
