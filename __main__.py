#simple module to perform basic checks on input data
#modulo para verificacoes simples de dados de entrada

class validacao():
 def check_range(self, maxi, mini, x):
  """Checks if a given value x is in a given range, between maxi and mini.
  """
  try:
   if mini < x < maxi:
    return 1
   else:
    return 0
  except Exception as e:
   pass
  
 def check_equal(self, value, x):
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
  """Used to remove negative values, making them all be 0.
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
   
