import curses 

def game(stdscr): 

  sh, sw = stdscr.getmaxyx()
  # y always comes first in coding 

  # turn off curser 
  curses.curs_set(False) 
  # set the nodelay mode 
  stdscr.nodelay(True)
  # set the timeout 
  stdscr.timeout(100)

  # paint the verticle line 
  for y in range(5, sh - 5):
    stdscr.addstr(y, sw - 5, chr(9474))

  # paint the moving object 
  body_ch = chr(9608)
  body = [sh // 2, sw // 2]
  stdscr.addstr(sh //2, sw // 2, body_ch)

  while True: 

    while True:
      key = stdscr.getch()

      #if key in [ord('q')]:
        #break 

    # move body right by a unit 
    stdscr.addstr(body[0], body[1], ' ')
    body = [body[0], body[1] + 1]
    stdscr.addstr(body[0], body[1], body_ch) 

    if body[1] == sw - 5: 
      # game over 
      msg = "Game Over!"
      stdscr.addstr(sh // 2 , sw // 2, msg)
      msg = "Press 'r' to restart the game or press any other key to exit."
      stdscr.addstr(sh // 2 + 1, sw // 2, msg)
      # turn off nodelay 
      stdscr.nodelay(False)
      

      rkey = stdscr.getch() 
      if rkey == ord('r'): 
        # restart game 
        stdscr.addstr(sh // 2 + 2, sw // 2, 'restarting')
        # reset the moving object to the center 
        body = [sh // 2, sw // 2]
        # clear the screen 
        stdscr.addstr(sh // 2, sw // 2, ' ' * 15)
        stdscr.addstr(sh // 2 + 1, sw // 2, ' ' * 46)
        #stdscr.addstr(sh // 2 + 2, sw // 2, ' ' * 15)
        # turn on nodelay mode 
        stdscr.nodelay(True)
        stdscr.addstr.timeout(100)
        # paint the vertical line again 
      else: 
        break 

curses.wrapper(game)