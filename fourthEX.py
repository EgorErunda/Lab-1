BLUE = 12
GREEN = 29
YELLOW = 11

file = open("sequence.txt").read().split('\n')
plus = 0
minus = 0
for s in file:
    if s == '0':
        continue
    if s[0] =='-':
        minus += 1
    else:
        plus += 1
        
print('Всего чисел', f'''\x1b[48;5;{BLUE}m{'  '}\x1b[0m''')
print('Положительные числа', f'''\x1b[48;5;{GREEN}m{'  '}\x1b[0m''')
print('Отрицательные числа', f'''\x1b[48;5;{YELLOW}m{'  '}\x1b[0m''')

print(f'''\x1b[48;5;{BLUE}m{' ' * 125}\x1b[0m''')
print(f'''\x1b[48;5;{GREEN}m{' ' * 62}\x1b[0m''')
print(f'''\x1b[48;5;{YELLOW}m{' ' * 63}\x1b[0m''')
file.close()
