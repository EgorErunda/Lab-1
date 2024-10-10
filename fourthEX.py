f = open("sequence.txt").read().split('\n')
plus = 0
minus = 0
for s in f:
    if s == '0':
        continue
    if s[0] =='-':
        minus += 1
    else:
        plus += 1
        
print('Всего чисел', f'''\x1b[48;5;12m{'  '}\x1b[0m''')
print('Положительные числа', f'''\x1b[48;5;29m{'  '}\x1b[0m''')
print('Отрицательные числа', f'''\x1b[48;5;11m{'  '}\x1b[0m''')

print(f'''\x1b[48;5;12m{' ' * 125}\x1b[0m''')
print(f'''\x1b[48;5;29m{' ' * 62}\x1b[0m''')
print(f'''\x1b[48;5;11m{' ' * 63}\x1b[0m''')

