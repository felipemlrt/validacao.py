#simple module to perform basic checks on input data

class validacao():
 def check_range(self, maxi, mini, x):
  if mini < x < maxi:
   return 1
  else:
   return 0
  
 def check_equal(self, value, x):
  if x == value:
   return 1
  else:
   return 0
