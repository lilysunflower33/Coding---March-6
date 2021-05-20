import curses

def main(stdscr): 

  curses.curs_set(False) 

  stdscr.addstr(2, 2, 'PAINTING TETRIS BLOCKS')
  stdscr.addstr(3, 2, '(TETRIMINOS)')

  tetrominos(stdscr, 'O-block')
  tetrominos(stdscr, 'I-block')
  tetrominos(stdscr, 'T-block')
  tetrominos(stdscr, 'J-block')
  tetrominos(stdscr, 'L-block')
  tetrominos(stdscr, 'S-block')
  tetrominos(stdscr, 'Z-block')

  stdscr.getch() 

def tetrominos(stdscr, type): 

  unit_ch = chr(9608) 

  curses.start_color()
  curses.use_default_colors()
  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, - 1)

  if type == 'O-block':
    for x in range(2, 4):
      stdscr.addstr(6, x, unit_ch, curses.color_pair(12))
      stdscr.addstr(7, x, unit_ch, curses.color_pair(12))

  if type == 'I-block':
    for x in range(8, 12): 
      stdscr.addstr(6, x, unit_ch, curses.color_pair(15))

    for y in range(8, 12):
      stdscr.addstr(y, 9, unit_ch, curses.color_pair(15))

  if type == 'T-block':
    for x in range(16, 19): 
      stdscr.addstr(6, x, unit_ch, curses.color_pair(93))
      stdscr.addstr(7, 17, unit_ch, curses.color_pair(93))

    for x in range(16, 19):
      stdscr.addstr(10, x, unit_ch, curses.color_pair(93))
      stdscr.addstr(9, 17, unit_ch, curses.color_pair(93)) 

    for y in range(12, 15):
      stdscr.addstr(y, 17, unit_ch, curses.color_pair(93))
      stdscr.addstr(13, 16, unit_ch, curses.color_pair(93))
      
    for y in range(16, 19):
      stdscr.addstr(17, 19, unit_ch, curses.color_pair(93))
      stdscr.addstr(y, 18, unit_ch, curses.color_pair(93)) 

  if type == 'J-block':
    for x in range(23, 26):
      stdscr.addstr(6, 23, unit_ch, curses.color_pair(33))
      stdscr.addstr(7, x, unit_ch, curses.color_pair(33))

    for y in range(9, 12):
      stdscr.addstr(11, 24, unit_ch, curses.color_pair(33))
      stdscr.addstr(y, 25, unit_ch, curses.color_pair(33))

    for x in range(23, 26):
      stdscr.addstr(13, x, unit_ch, curses.color_pair(33))
      stdscr.addstr(14, 25, unit_ch, curses.color_pair(33))

    for y in range(16, 19):
      stdscr.addstr(y, 23, unit_ch, curses.color_pair(33))
      stdscr.addstr(16, 24, unit_ch, curses.color_pair(33))

  if type == 'L-block':
    for x in range(30, 33):
      stdscr.addstr(6, 32, unit_ch, curses.color_pair(209))
      stdscr.addstr(7, x, unit_ch, curses.color_pair(209))

    for y in range(9, 12):
      stdscr.addstr(9, 31, unit_ch, curses.color_pair(209))
      stdscr.addstr(y, 32, unit_ch, curses.color_pair(209))

    for x in range(30, 33):
      stdscr.addstr(13, x, unit_ch, curses.color_pair(209))
      stdscr.addstr(14, 30, unit_ch, curses.color_pair(209))

    for y in range(16, 19):
      stdscr.addstr(y, 30, unit_ch, curses.color_pair(209))
      stdscr.addstr(16, 31, unit_ch, curses.color_pair(209))

  if type == 'S-block':
    for x in range(38, 40):
      stdscr.addstr(6, x, unit_ch, curses.color_pair(41))
    for x in range(37, 39):
      stdscr.addstr(7, x, unit_ch, curses.color_pair(41))

    for y in range(9, 11):
      stdscr.addstr(y, 37, unit_ch, curses.color_pair(41))
    for y in range(10, 12):
      stdscr.addstr(y, 38, unit_ch, curses.color_pair(41))

  if type == 'Z-block':
    for x in range(44, 46):
      stdscr.addstr(6, x, unit_ch, curses.color_pair(125))
    for x in range(45, 47):
      stdscr.addstr(7, x, unit_ch, curses.color_pair(125))

    for y in range(9, 11):
      stdscr.addstr(y, 45, unit_ch, curses.color_pair(125))
    for y in range(10, 12):
      stdscr.addstr(y, 44, unit_ch, curses.color_pair(125))

curses.wrapper(main)