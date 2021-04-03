import curses 

# initialize compile
# def initcolors(bg_color=-1)

def colors(stdscr):

  curses.start_color()
  curses.use_default_colors()

  stdscr.addstr(1, 0, "")
  for i in range(0, curses.COLORS):
  # for i in range (0, 20):
    #initialize the colour pair

    # pair number, foreground dolour, background colour
    #can not use 0 for init_pair
    curses.init_pair(i + 1, i, -1)
    # curses.init_pair (i + 1, i, bg_color)
    # -1 is a black background
    
    y = 1
    if i < 16:
      x = i * 3

    stdscr.addstr(y, x, "{0}".format (chr(9608) * 4), curses.color_pair(i + 1))
    # stdscr.addstr("[{0}-{1}]".format (str(i + 1), chr(9608) * 3), curses.color_pair(i + 1))
  
  stdscr.getch()

curses.wrapper(colors)