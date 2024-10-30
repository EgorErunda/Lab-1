BL = 19
WH = 255
RE = 1
PR = '    '

def draw_line():
  for _ in range(3):
    print(f'\x1b[48;5;{BL}m{PR}\x1b[48;5;{WH}m{PR}\x1b[48;5;{RE}m{PR}\x1b[0m')

if __name__ == '__main__':
  draw_line()

