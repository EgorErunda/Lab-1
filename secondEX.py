WHITE = 255

square = f'''\x1b[48;5;{WHITE}m{'   '}\x1b[0m'''
empthy = f'''\x1b[48;5;m{'   '}\x1b[0m'''
str1 = square + empthy + square
str2 = empthy + square + empthy
while True:
  print(str1)
  print(str2)
