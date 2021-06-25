import curses

def main(stdscr):

  curses.curs_set(False) 
  
  curses.start_color()
  curses.use_default_colors()
  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, - 1)

  stdscr.addstr(1, 2, 'Moving Tetrominoes (T-block)')
  stdscr.addstr(2, 2, 'Use the Arrow Keys to Move and Space Bar to Rotate')
  stdscr.addstr(3, 2, 'Press q to Quit') 

  unit_ch = chr(9609)
  erase_ch = ' '

  T_block = [
    [5,2], [5,4], [5,6], [6,4]
  ] 
  for unit in T_block:
    stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(93))

  while True: 
    key = stdscr.getch()

    if  key == ord('q'):
      break

    if key == curses.KEY_RIGHT:
      direction = key
    if key == curses.KEY_LEFT:
      direction = key
    if key == curses.KEY_DOWN:
      direction = key
    if key == curses.KEY_UP:
      direction = key

    if key == curses.KEY_RIGHT:

      new_r = [
        [T_block[2][0], T_block[2][1] + 2], 
        [T_block[3][0], T_block[3][1] + 2]
      ]

      erase_r = [
        [T_block[0][0], T_block[0][1]], 
        [T_block[3][0], T_block[3][1]]
      ]

      T_block = [
        T_block[1], T_block[2], new_r[0], new_r[1]
      ]

      for unit in new_r: 
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(93))
      for unit in erase_r:
        stdscr.addstr(unit[0], unit[1], erase_ch)

    if key == curses.KEY_LEFT:

      new_l = [
        [T_block[0][0], T_block[0][1] - 2], 
        [T_block[3][0], T_block[3][1] - 2]
      ]

      erase_l = [
        [T_block[2][0], T_block[2][1]], 
        [T_block[3][0], T_block[3][1]]
      ]

      T_block = [
        new_l[0], T_block[0], T_block[1], new_l[1]
      ]

      for unit in new_l: 
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(93))
      for unit in erase_l:
        stdscr.addstr(unit[0], unit[1], erase_ch)

    if key == curses.KEY_DOWN:

      new_d = [
        [T_block[0][0] + 1, T_block[0][1]], 
        [T_block[2][0] + 1, T_block[2][1]], 
        [T_block[3][0] + 1, T_block[3][1]]
      ]

      erase_d = [
        [T_block[0][0], T_block[0][1]], 
        [T_block[1][0], T_block[1][1]], 
        [T_block[2][0], T_block[2][1]]
      ]

      T_block = [
        new_d[0], T_block[3], new_d[1], new_d[2]
      ]

      for unit in new_d: 
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(93))
      for unit in erase_d:
        stdscr.addstr(unit[0], unit[1], erase_ch)

    if key == curses.KEY_UP:

      new_u = [
        [T_block[0][0] - 1, T_block[0][1]], 
        [T_block[1][0] - 1, T_block[1][1]], 
        [T_block[2][0] - 1, T_block[2][1]]
      ]

      erase_u = [
        [T_block[0][0], T_block[0][1]], 
        [T_block[2][0], T_block[2][1]], 
        [T_block[3][0], T_block[3][1]]
      ]

      T_block = [
        new_u[0], new_u[1], new_u[2], T_block[1]
      ]

      for unit in new_u: 
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(93))
      for unit in erase_u:
        stdscr.addstr(unit[0], unit[1], erase_ch) 

    if key == 32: 

      new1 = [
        [T_block[0][0] - 1, T_block[0][1]], 
        [T_block[1][0] - 1, T_block[1][1]], 
        [T_block[2][0] - 1, T_block[2][1]]
      ]

      erase1 = [
        [T_block[0][0], T_block[0][1]], 
        [T_block[2][0], T_block[2][1]], 
        [T_block[3][0], T_block[3][1]]
      ]

      T_block = [
        new1[0], T_block[3], new1[1], new1[2]
      ]

      for unit in new1: 
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(93))
      for unit in erase1:
        stdscr.addstr(unit[0], unit[1], erase_ch)

curses.wrapper(main) 