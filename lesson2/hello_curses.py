import curses

def hello(stdscr):
  
  #get the screen size
  sh, sw = stdscr.getmaxyx()

  #single slash(/) gives the division reslut
  # double slash(//) gives only the whole number part of the division answer
  
  msg = "Welcome to my keyboard decoding game! Press ESC to exit."
  stdscr.addstr(sh // 2, sw // 2 - len(msg) // 2, msg)
  
  while True:
    userkey = stdscr.getch()
    if userkey == 27:
      break
    
    msg = "ASCII CODE: {0}, Character: {1}".format(userkey, chr(userkey))
    stdscr.addstr(sh // 2 + 2, sw // 2 -len(msg) // 2, msg)

  stdscr.getch()

curses.wrapper(hello)