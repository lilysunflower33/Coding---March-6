import curses 

def colors(stdscr):

  curses.start_color()
  curses.use_default_colors()

  stdscr.addstr(1, 0, "")
  for i in range(0, curses.COLORS):
    #initialize the colour pair

    #can not use 0 for init_pair
    curses.init_pair(i + 1, i, -1)
    # -1 is a black background
    
    stdscr.addstr("[{0}-{1}]".format (str(i + 1), chr(9608) * 3), curses.color_pair(i + 1))
  
  stdscr.getch()

curses.wrapper(colors)