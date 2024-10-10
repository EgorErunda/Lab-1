
# from math import *

X = [c for c in range(20)]
for i in range(20, 0, -1):
    X.append(i + 0.5)
     
X.sort(reverse = False)

for y in range(20, 0, -1):
    for x in X:
        if round(x ** 2) == y:
            print(f'''\x1b[48;5;52m{'  '}\x1b[0m''', end= '')
        else:
            print(f'''\x1b[48;5;5m{'  '}\x1b[0m''', end= '')
    print('')



   



