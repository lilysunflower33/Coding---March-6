import curses

def main(stdscr): 

  curses.curs_set(False) 

  stdscr.addstr(2, 2, 'PAINTING TETRIS BLOCKS')
  stdscr.addstr(3, 2, '(TETRIMINOS)')

  tetriminos(stdscr, 'O-block')
  tetriminos(stdscr, 'I-block')
  tetriminos(stdscr, 'T-block')
  tetriminos(stdscr, 'J-block')
  tetriminos(stdscr, 'L-block')
  tetriminos(stdscr, 'S-block')
  tetriminos(stdscr, 'Z-block')

  stdscr.getch() 

def tetriminos(stdscr, type): 

  unit_ch = chr(9608) 

  if type == 'O-block':
    for x in range(2, 4):
      stdscr.addstr(6, x, unit_ch)
      stdscr.addstr(7, x, unit_ch)

  if type == 'I-block': 
    for x in range(2, 6): 
      stdscr.addstr(10, x, unit_ch)
    for y in range(9, 13):
      stdscr.addstr(y, 8, unit_ch)

  if type == 'T-block':
    for x in range(2, 5): 
      stdscr.addstr(14, x, unit_ch)
      stdscr.addstr(15, 3, unit_ch)

    for x in range(7, 10):
      stdscr.addstr(15, x, unit_ch)
      stdscr.addstr(14, 8, unit_ch)

    for y in range(14, 17):
      stdscr.addstr(y, 12, unit_ch)
      stdscr.addstr(15, 13, unit_ch)

    for y in range(14, 17):
      stdscr.addstr(15, 16, unit_ch)
      stdscr.addstr(y, 17, unit_ch)

  if type == 'J-block':
    for x in range(2, 5):
      stdscr.addstr(18, 2, unit_ch)
      stdscr.addstr(19, x, unit_ch)

    for y in range(18, 21):
      stdscr.addstr(20, 7, unit_ch)
      stdscr.addstr(y, 8, unit_ch)

    for x in range(11, 14):
      stdscr.addstr(19, x, unit_ch)
      stdscr.addstr(20, 13, unit_ch)

    for y in range(18, 21):
      stdscr.addstr(y, 16, unit_ch)
      stdscr.addstr(18, 17, unit_ch)

  if type == 'L-block':
    for x in range(2, 5):
      stdscr.addstr(22, 4, unit_ch)
      stdscr.addstr(23, x, unit_ch)

    for y in range(22, 25):
      stdscr.addstr(22, 7, unit_ch)
      stdscr.addstr(y, 8, unit_ch)

    for x in range(11, 14):
      stdscr.addstr(23, x, unit_ch)
      stdscr.addstr(24, 11, unit_ch)

    for y in range(22, 25):
      stdscr.addstr(y, 16, unit_ch)
      stdscr.addstr(24, 17, unit_ch)
  
  if type == 'S-block':
    for x in range(3, 5):
      stdscr.addstr(26, x, unit_ch)
    for x in range(2, 4):
      stdscr.addstr(27, x, unit_ch)

    for y in range(26, 28):
      stdscr.addstr(y, 7, unit_ch)
    for y in range(27, 29):
      stdscr.addstr(y, 8, unit_ch)

  if type == 'Z-block':
    for x in range(2, 4):
      stdscr.addstr(30, x, unit_ch)
    for x in range(3, 5):
      stdscr.addstr(31, x, unit_ch)

    for y in range(30, 32):
      stdscr.addstr(y, 8, unit_ch)
    for y in range(31, 33):
      stdscr.addstr(y, 7, unit_ch)

curses.wrapper(main)