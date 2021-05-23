import curses

def main(stdscr):

  curses.curs_set(False) 
  
  curses.start_color()
  curses.use_default_colors()
  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, - 1)

  stdscr.addstr(2, 2, 'Moving Tetrominos')
  stdscr.addstr(3, 2, 'Press q to Quit') 

  unit_ch = chr(9609)
  erase_ch = ' '

  O_block = [
    [5,12], [5,14], [6,14], [6,12]
  ] 
  for unit in O_block:
    stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(12))

  while True: 
    key = stdscr.getch()

    if  key == ord('q'):
      break
      
    if key == curses.KEY_LEFT:
      direction = key
    if key == curses.KEY_DOWN:
      direction = key
    if key == curses.KEY_UP:
      direction = key

    if key == curses.KEY_LEFT:
      
      new_l = [
        [O_block[0][0], O_block[0][1] - 2], 
        [O_block[3][0], O_block[3][1] - 2]
      ]

      erase_l = [
        [O_block[1][0], O_block[1][1]], 
        [O_block[2][0], O_block[2][1]]
      ]

      O_block = [
        O_block[0], new_l[0], new_l[1], O_block[3]
      ]

      for unit in new_l: 
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(12))
      for unit in erase_l:
        stdscr.addstr(unit[0], unit[1], erase_ch)

curses.wrapper(main)