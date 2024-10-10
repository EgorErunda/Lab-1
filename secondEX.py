square = f'''\x1b[48;5;255m{'   '}\x1b[0m'''
empthy = f'''\x1b[48;5;m{'   '}\x1b[0m'''
s1 = square + empthy + square
s2 = empthy + square + empthy
while True:
  print(s1)
  print(s2)
