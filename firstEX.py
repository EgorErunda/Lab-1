def draw_line():
  for _ in range(3):
    print(f'''\x1b[48;5;19m{'    '}\x1b[48;5;255m{'    '}\x1b[48;5;1m{'    '}\x1b[0m''')

if __name__ == '__main__':
  draw_line()

