import curses

def main(stdscr):

  curses.curs_set(False) 

  stdscr.addstr(2, 2, 'Moving Tetrominos')
  stdscr.addstr(3, 2, 'Press q to Quit')

  tetrominos(stdscr, 'O-block')
  tetrominos(stdscr, 'I-block')
  tetrominos(stdscr, 'I-block2')
  tetrominos(stdscr, 'T-block')
  tetrominos(stdscr, 'T-block2')
  tetrominos(stdscr, 'T-block3')
  tetrominos(stdscr, 'T-block4')
  tetrominos(stdscr, 'J-block')
  tetrominos(stdscr, 'J-block2')
  tetrominos(stdscr, 'J-block3')
  tetrominos(stdscr, 'J-block4')
  tetrominos(stdscr, 'L-block')
  tetrominos(stdscr, 'L-block2')
  tetrominos(stdscr, 'L-block3')
  tetrominos(stdscr, 'L-block4')
  tetrominos(stdscr, 'S-block')
  tetrominos(stdscr, 'S-block2')
  tetrominos(stdscr, 'Z-block')
  tetrominos(stdscr, 'Z-block2')

  stdscr.getch()  

  while True:

    key = stdscr.getch() 
    unit_ch = chr(9609) 
    
    if key == ord('q'):
      break;

    if key == curses.KEY_RIGHT:
      direction = key
    elif key == curses.KEY_LEFT:
      direction = key
    elif key == curses.KEY_DOWN:
      direction = key
    elif key == curses.KEY_UP:
      direction = key
    
    # move O-block
    if direction == curses.KEY_DOWN: 
      stdscr.addstr(5, 2, ' ')
      stdscr.addstr(5, 4, ' ')
      stdscr.addstr(7, 2, unit_ch, curses.color_pair(12)) 
      stdscr.addstr(7, 4, unit_ch, curses.color_pair(12)) 

    elif direction == curses.KEY_UP: 
      stdscr.addstr(6, 2, ' ')
      stdscr.addstr(6, 4, ' ')
      stdscr.addstr(4, 2, unit_ch, curses.color_pair(12)) 
      stdscr.addstr(4, 4, unit_ch, curses.color_pair(12)) 

    elif direction == curses.KEY_RIGHT: 
      stdscr.addstr(5, 2, ' ')
      stdscr.addstr(6, 2, ' ')
      stdscr.addstr(5, 6, unit_ch, curses.color_pair(12)) 
      stdscr.addstr(6, 6, unit_ch, curses.color_pair(12)) 

    elif direction == curses.KEY_LEFT: 
      stdscr.addstr(5, 4, ' ')
      stdscr.addstr(6, 4, ' ')
      stdscr.addstr(5, 0, unit_ch, curses.color_pair(12)) 
      stdscr.addstr(6, 0, unit_ch, curses.color_pair(12)) 

def tetrominos(stdscr, type): 

  unit_ch = chr(9609)
  
  curses.start_color()
  curses.use_default_colors()
  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, - 1)

  if type == 'O-block': 
    stdscr.addstr(5, 2, unit_ch, curses.color_pair(12))
    stdscr.addstr(5, 4, unit_ch, curses.color_pair(12))
    stdscr.addstr(6, 4, unit_ch, curses.color_pair(12))
    stdscr.addstr(6, 2, unit_ch, curses.color_pair(12)) 

  if type == 'I-block':
    stdscr.addstr(6, 10, unit_ch, curses.color_pair(52))
    stdscr.addstr(6, 12, unit_ch, curses.color_pair(52))
    stdscr.addstr(6, 14, unit_ch, curses.color_pair(52))
    stdscr.addstr(6, 16, unit_ch, curses.color_pair(52))
  elif type == 'I-block2':
    stdscr.addstr(8, 13, unit_ch, curses.color_pair(52))
    stdscr.addstr(9, 13, unit_ch, curses.color_pair(52))
    stdscr.addstr(10, 13, unit_ch, curses.color_pair(52))
    stdscr.addstr(11, 13, unit_ch, curses.color_pair(52))

  if type == 'T-block':
    stdscr.addstr(5, 24, unit_ch, curses.color_pair(93))
    stdscr.addstr(6, 22, unit_ch, curses.color_pair(93))
    stdscr.addstr(6, 24, unit_ch, curses.color_pair(93))
    stdscr.addstr(6, 26, unit_ch, curses.color_pair(93))
  elif type == 'T-block2':
    stdscr.addstr(8, 24, unit_ch, curses.color_pair(93))
    stdscr.addstr(9, 24, unit_ch, curses.color_pair(93))
    stdscr.addstr(10, 24, unit_ch, curses.color_pair(93))
    stdscr.addstr(9, 26, unit_ch, curses.color_pair(93))
  elif type == 'T-block3':
    stdscr.addstr(12, 24, unit_ch, curses.color_pair(93))
    stdscr.addstr(12, 22, unit_ch, curses.color_pair(93))
    stdscr.addstr(12, 26, unit_ch, curses.color_pair(93))
    stdscr.addstr(13, 24, unit_ch, curses.color_pair(93))
  elif type == 'T-block4':
    stdscr.addstr(15, 24, unit_ch, curses.color_pair(93))
    stdscr.addstr(16, 24, unit_ch, curses.color_pair(93))
    stdscr.addstr(17, 24, unit_ch, curses.color_pair(93))
    stdscr.addstr(16, 22, unit_ch, curses.color_pair(93))

  if type == 'J-block':
    stdscr.addstr(5, 32, unit_ch, curses.color_pair(21))
    stdscr.addstr(6, 32, unit_ch, curses.color_pair(21))
    stdscr.addstr(6, 34, unit_ch, curses.color_pair(21))
    stdscr.addstr(6, 36, unit_ch, curses.color_pair(21))
  elif type == 'J-block2':
    stdscr.addstr(8, 34, unit_ch, curses.color_pair(21))
    stdscr.addstr(8, 36, unit_ch, curses.color_pair(21))
    stdscr.addstr(9, 34, unit_ch, curses.color_pair(21))
    stdscr.addstr(10, 34, unit_ch, curses.color_pair(21))
  elif type == 'J-block3':
    stdscr.addstr(12, 32, unit_ch, curses.color_pair(21))
    stdscr.addstr(12, 34, unit_ch, curses.color_pair(21))
    stdscr.addstr(12, 36, unit_ch, curses.color_pair(21))
    stdscr.addstr(13, 36, unit_ch, curses.color_pair(21))
  elif type == 'J-block4':
    stdscr.addstr(17, 32, unit_ch, curses.color_pair(21))
    stdscr.addstr(15, 34, unit_ch, curses.color_pair(21))
    stdscr.addstr(16, 34, unit_ch, curses.color_pair(21))
    stdscr.addstr(17, 34, unit_ch, curses.color_pair(21))

  if type == 'L-block':
    stdscr.addstr(6, 42, unit_ch, curses.color_pair(4))
    stdscr.addstr(6, 44, unit_ch, curses.color_pair(4))
    stdscr.addstr(5, 46, unit_ch, curses.color_pair(4))
    stdscr.addstr(6, 46, unit_ch, curses.color_pair(4)) 
  elif type == 'L-block2':
    stdscr.addstr(8, 44, unit_ch, curses.color_pair(4))
    stdscr.addstr(9, 44, unit_ch, curses.color_pair(4))
    stdscr.addstr(10, 44, unit_ch, curses.color_pair(4))
    stdscr.addstr(10, 46, unit_ch, curses.color_pair(4))   
  elif type == 'L-block3':
    stdscr.addstr(12, 46, unit_ch, curses.color_pair(4))
    stdscr.addstr(12, 44, unit_ch, curses.color_pair(4))
    stdscr.addstr(12, 42, unit_ch, curses.color_pair(4))
    stdscr.addstr(13, 42, unit_ch, curses.color_pair(4))
  elif type == 'L-block4':
    stdscr.addstr(15, 44, unit_ch, curses.color_pair(4))
    stdscr.addstr(15, 42, unit_ch, curses.color_pair(4))
    stdscr.addstr(16, 44, unit_ch, curses.color_pair(4))
    stdscr.addstr(17, 44, unit_ch, curses.color_pair(4))

  if type == 'S-block':
    stdscr.addstr(6, 52, unit_ch, curses.color_pair(47))
    stdscr.addstr(6, 54, unit_ch, curses.color_pair(47))
    stdscr.addstr(5, 54, unit_ch, curses.color_pair(47))
    stdscr.addstr(5, 56, unit_ch, curses.color_pair(47))
  elif type == 'S-block2':
    stdscr.addstr(8, 54, unit_ch, curses.color_pair(47))
    stdscr.addstr(9, 54, unit_ch, curses.color_pair(47))
    stdscr.addstr(9, 56, unit_ch, curses.color_pair(47))
    stdscr.addstr(10, 56, unit_ch, curses.color_pair(47))

  if type == 'Z-block':
    stdscr.addstr(6, 64, unit_ch, curses.color_pair(10))
    stdscr.addstr(5, 64, unit_ch, curses.color_pair(10))
    stdscr.addstr(6, 66, unit_ch, curses.color_pair(10))
    stdscr.addstr(5, 62, unit_ch, curses.color_pair(10))
  elif type == 'Z-block2':
    stdscr.addstr(8, 66, unit_ch, curses.color_pair(10))
    stdscr.addstr(9, 66, unit_ch, curses.color_pair(10))
    stdscr.addstr(9, 64, unit_ch, curses.color_pair(10))
    stdscr.addstr(10, 64, unit_ch, curses.color_pair(10))

curses.wrapper(main)