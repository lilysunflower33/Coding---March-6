import curses

unit_ch = chr(9609)
erase_ch = ' '

def main(stdscr):

  curses.curs_set(False) 
  
  curses.start_color()
  curses.use_default_colors()
  for i in range(0, curses.COLORS):
    curses.init_pair(i + 1, i, - 1)

  stdscr.addstr(1, 2, 'Moving Tetrominoes (I-block)')
  stdscr.addstr(2, 2, 'Use the Arrow Keys to Move and Space Bar to Rotate')
  stdscr.addstr(3, 2, 'Press q to Quit') 

  movement(stdscr)

def movement(stdscr):
  
  I_block = [
    [5,2], [5,4], [5,6], [5,8]
  ] 
  for unit in I_block:
    stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(52))

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
        [I_block[3][0], I_block[3][1] + 2]
      ]

      erase_r = [
        [I_block[0][0], I_block[0][1]]
      ]

      I_block = [
        I_block[1], I_block[2], I_block[3], new_r[0]
      ]

      for unit in new_r: 
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(52))
      for unit in erase_r:
        stdscr.addstr(unit[0], unit[1], erase_ch)

    if key == curses.KEY_LEFT:

      new_l = [
        [I_block[0][0], I_block[0][1] - 2]
      ]

      erase_l = [
        [I_block[3][0], I_block[3][1]]
      ]

      I_block = [
        new_l[0], I_block[0], I_block[1], I_block[2]
      ]

      for unit in new_l: 
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(52))
      for unit in erase_l:
        stdscr.addstr(unit[0], unit[1], erase_ch)

    if key == curses.KEY_DOWN:

      new_d = [
        [I_block[0][0] + 1, I_block[0][1]], 
        [I_block[1][0] + 1, I_block[1][1]], 
        [I_block[2][0] + 1, I_block[2][1]], 
        [I_block[3][0] + 1, I_block[3][1]]
      ]

      erase_d = [
        [I_block[0][0], I_block[0][1]], 
        [I_block[1][0], I_block[1][1]], 
        [I_block[2][0], I_block[2][1]], 
        [I_block[3][0], I_block[3][1]]
      ]

      I_block = [
        new_d[0], new_d[1], new_d[2], new_d[3]
      ]

      for unit in new_d: 
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(52))
      for unit in erase_d:
        stdscr.addstr(unit[0], unit[1], erase_ch)

    if key == curses.KEY_UP:

      new_u = [
        [I_block[0][0] - 1, I_block[0][1]], 
        [I_block[1][0] - 1, I_block[1][1]], 
        [I_block[2][0] - 1, I_block[2][1]], 
        [I_block[3][0] - 1, I_block[3][1]]
      ]

      erase_u = [
        [I_block[0][0], I_block[0][1]], 
        [I_block[1][0], I_block[1][1]], 
        [I_block[2][0], I_block[2][1]], 
        [I_block[3][0], I_block[3][1]]
      ]

      I_block = [
        new_u[0], new_u[1], new_u[2], new_u[3]
      ]

      for unit in new_u: 
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(52))
      for unit in erase_u:
        stdscr.addstr(unit[0], unit[1], erase_ch) 

def rotation(stdscr):
  
  I_block = [
    [5,2], [5,4], [5,6], [5,8]
  ] 
  for unit in I_block:
    stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(52)) 

  while True: 
    key = stdscr.getch()

    if key == 32: 

      new1 = [
        [I_block[0][0] - 2, I_block[0][1] + 4], 
        [I_block[1][0] - 1, I_block[1][1] + 2], 
        [I_block[3][0] + 1, I_block[3][1] - 2]
      ]

      erase1 = [
        [I_block[0][0], I_block[0][1]], 
        [I_block[1][0], I_block[1][1]],
        [I_block[3][0], I_block[3][1]]
      ]

      I_block = [
        new1[0], new1[1], I_block[2], new1[2]
      ]

      for unit in new1: 
        stdscr.addstr(unit[0], unit[1], unit_ch, curses.color_pair(52))
      for unit in erase1:
        stdscr.addstr(unit[0], unit[1], erase_ch)

curses.wrapper(main) 