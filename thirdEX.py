PURPLE = 56
PINK = 5

arr = [c for c in range(20)]
for i in range(20, 0, -1):
    arr.append(i + 0.5)
     
arr.sort(reverse = False)

for y in range(20, 0, -1):
    for x in arr:
        if round(x ** 2) == y:
            print(f'''\x1b[48;5;{PURPLE}m{'  '}\x1b[0m''', end= '')
        else:
            print(f'''\x1b[48;5;{PINK}m{'  '}\x1b[0m''', end= '')
    print('')



   



