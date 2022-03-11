import curses 
from curses import textpad 

def main(stdscr):
  curses.curs_set(False) 

  stdscr.addstr(1, 2, 'Tetris Game-Board')
  stdscr.addstr(2, 2, 'Press q to Quit') 

  border(stdscr) 

def border(stdscr):
  sh, sw = stdscr.getmaxyx()

  # non-breaking hyphen 
  unit1 = chr(8209)
  # verticle line 
  unit2 = chr(124)

  border = [
    [4, 1], [4, sw - 1]
    #[] 
  ]
  for unit in border: 
    stdscr.addstr(border[0], border[1], unit1)

def grid(stdscr): 
  sh, sw = stdscr.getmaxyx() 

  # hyphen 
  unit1 = chr(8208) 
  # broken verticle line 
  unit2 = chr(166)

curses.wrapper(main)