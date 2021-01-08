#simple module to perform basic checks on input data

class validacao():
 def check_range(self, max, min, x):
  if min < x < max:
   return 1
  else:
   return 0
