#simple module to perform basic checks on input data

class validacao():
 def check_range(self, maxi, mini, x):
  try:
   if mini < x < maxi:
    return 1
   else:
    return 0
  except Exception as e:
   pass
  finally:
   pass
  
 def check_equal(self, value, x):
  if x == value:
   return 1
  else:
   return 0
