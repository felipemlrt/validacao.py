#simple module to perform basic checks on input data
#modulo para verificacoes simples de dados de entrada

class validacao():
 def check_range(self, maxi, mini, x):
  """Checks if a given value x is in a given range, between maxi and mini. Confere se um valor x esta entre maxi e mini.
  """
  try:
   if mini < x < maxi:
    return 1
   else:
    return 0
  except Exception as e:
   pass
  
 def check_equal(self, value, x):
  """Checks if a given x is equal to a test value. Verifica se um dado valor x é igual a um valor de teste.
  """
  try:
   if x == value:
    return 1
   else:
    return 0
  except Exception as e:
   pass
  finally:
   pass
  
 def zero_if_missing(self, x):
  """If x is NULL ti becomes 0 instead, otherwise it remains the same
  """
  try:
   if x is NULL:
    return 0
   else:
    return x
  except Exception as e:
   return e
  finally:
   pass
   
 def zero_if_negative(self, x):
  """If x is below 0 it becomes 0 instead. Caso x seja menor que 0 este se torna 0 entao.
  """
  try:
   if x < 0:
    return 0
   else:
    return x
  except Exception as e:
   return e
  finally:
   pass
  
  if __name__=="__main__":
   vld = validacao()
   print(vld.check_range(0, 10, 5))
   
