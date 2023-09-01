class OrdenacaoOtima:
  def mergesort(self, vet):
    self.merge(vet, 0, len(vet))
    return vet

  def merge(self, vet, inicio, fim):
    print(inicio, fim, vet)
    if fim - inicio > 1:
      meio = (inicio + fim) // 2
      self.merge(vet, inicio, meio)
      self.merge(vet, meio, fim)
      self.intercala(vet, inicio, meio, fim)  
    print(inicio, fim, vet)

  def intercala(self, vet, inicio, meio, fim):
    x = vet[inicio:meio]
    y = vet[meio:fim]
    ix = 0
    iy = 0
    i = inicio
    while i < fim:
      if x[ix] < y[iy]:
        vet[i] = x[ix]
        ix = ix + 1
      else:
        vet[i] = y[iy]
        iy = iy + 1
      i = i + 1
      if ix == len(x):
        vet[i:fim] = y[iy:len(y)]
        break
      if iy == len(y):
        vet[i:fim] = x[ix:len(x)]
        break
    return vet    
