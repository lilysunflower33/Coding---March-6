import curses 
from curses import textpad

def snake(stdscr): 
  
  sh, sw = stdscr.getmaxyx()

  # hide curser
  curses.curs_set(False)
  # turn on nodelay to make the snake move by itself
  stdscr.nodelay(0)
  # set the timeout to 0.1 second
  stdscr.timeout(100)
  
  # draw a rectangle 
  textpad.rectangle(stdscr, 3, 3, sh - 3, sw - 3)

  # snake variable setup
  snake = [
    [sh // 2, sw // 2 + 1],
    [sh // 2, sw // 2],
    [sh // 2, sw // 2 - 1],
  ]
  snake_ch = chr(9608)

  #9608 
  # paint the snake 
  for unit in snake:
    stdscr.addstr(unit[0], unit[1], chr(9608))

  # randomly generate and place the snake food 
  food_ch = "*"
  food = [

  ]

  while True:
    user_key = stdscr.getch()

    # exit game when player preses ESC, q, or Q
    if user_key in [27, 113, 81]:
      break
    elif user_key in [curses.]

    # add new head
    head = snake[0]
    # calculate the new help
    new_head = [head[0], head[1] +1]
    stdscr.addstr(new_head[0], new_head[1], snake_ch)
    # store the new head
    snake.insert(0, new_head)
    # erase the tail by painting an white space
    stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
    snake.pop()

  stdscr.getch() 

curses.wrapper(snake)