class OrdenacaoNaoOtima:
  def bubble(self, x):
    n = len(x) - 1
    for i in range(0, n):
      for j in range(n-1, i-1, -1):
        if x[j] > x[j+1]:
          x[j], x[j+1] = x[j+1], x[j]
      print(i, x)
    return x
  
  def bubble2(self, x):
    n = len(x) - 1
    for i in range(0, n):
      ordenado = True
      for j in range(n-1, i-1, -1):
        if x[j] > x[j+1]:
          x[j], x[j+1] = x[j+1], x[j]
          ordenado = False
      print(i, x)
      if ordenado:
        break
    return x 

  def selection(self, x):
    n = len(x)
    for i in range(0, n-1):
      for j in range(i+1, n):
        if x[i] > x[j]:
          x[i], x[j] = x[j], x[i]
      print(i, x)
    return x
    
  def selection2(self, x):
    n = len(x)
    for i in range(0, n-1):
      ordenado = True
      for j in range(i+1, n):
        if x[i] > x[j]:
          x[i], x[j] = x[j], x[i]
          ordenado = False
      print(i, x)
      if ordenado:
        break
    return x

  def selection3(self, x):
    n = len(x)
    for i in range(0, n-1):
      m = i
      for j in range(i+1, n):
        if x[m] > x[j]:
          m = j
      x[i], x[m] = x[m], x[i]
      print(i, x)
    return x
    
  def insertion(self, x):
    n = len(x)
    for i in range(1, n):
      atual = x[i]
      j = i - 1
      while j >= 0 and atual < x[j]:
        x[j+1] = x[j]
        j = j - 1
      x[j+1] = atual
      print(i, x)
    return x
  
  def shell(self, x):
    n = len(x)
    h = 1
    while h < n:
      h = h * 3 + 1
    while h > 1:
      h = h // 3
      for i in range(h, n, h):
        atual = x[i]
        j = i - h
        while j >= 0 and atual < x[j]:
          x[j+h] = x[j]
          j = j - h
        x[j+h] = atual
        print(i, x)
    return x

