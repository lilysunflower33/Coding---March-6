import curses 

def game(stdscr): 

  sh, sw = stdscr.getmaxyx()
  # y always comes first in coding 

  body_ch = chr(9608)

  # paint the verticle line 
  for y in range(5, sh - 5):
    stdscr.addstr(y, sw - 5, chr(9474))

  # paint the moving object 
  stdscr.addstr(sh //2, sw // 2, body_ch)

  # set the nodelay mode 
  stdscr.nodelay(True)
  # set the timeout 
  stdscr.timeout(100)

  while True: 

    key = stdscr.getch()

    if key in [ord('ESC')]:
      break 

    

curses.wrapper(game)