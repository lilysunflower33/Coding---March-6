import curses 
from curses import textpad
import random

def snake(stdscr): 
  
  sh, sw = stdscr.getmaxyx()

  # hide curser
  curses.curs_set(False)
  # turn on nodelay to make the snake move by itself
  stdscr.nodelay(True)
  # set the timeout to milliseconds 
  # timeout is the defult moving speed for the snake 
  stdscr.timeout(150)
  
  # draw a rectangle 
  textpad.rectangle(stdscr, 2, 2, sh - 2, sw - 2)

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

  # set up the defult moving direction 
  direction = curses.KEY_RIGHT

  # randomly generate and place the snake food 
  food_ch = "*"
  food = [
    random.randint(4, sh - 3)
    random.randint(4, sw - 3)
  ]
  stdscr.addstr(food[0], food[1], food_ch)

  while True:

    user_key = stdscr.getch()

    # exit game when player preses ESC, q, or Q
    if user_key in [27, 113, 81]:
      break 
    #elif user_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
    # move the snake unit one right 
    # reset the initial direction 
      #direction = user_key

    if user_key == curses.KEY_UP: 
      direction = user_key 
    elif user_key == curses.KEY_LEFT: 
      direction = user_key 
    elif user_key == curses.KEY_RIGHT: 
      direction = user_key 
    elif user_key == curses.KEY_DOWN: 
      direction = user_key 

    # add new head
    head = snake[0] 

    # calculate where the snake goes based on direction on userkey 
    if direction == curses.KEY_RIGHT: 
      new_head = [head[0], head[1] + 1]
    elif direction == curses.KEY_LEFT: 
      new_head = [head[0], head[1] - 1] 
    elif direction == curses.KEY_UP: 
      new_head = [head[0] - 1, head[1]] 
    elif direction == curses.KEY_DOWN: 
      new_head = [head[0] + 1, [1]]

    # calculate the new snake after it moves
    # new_head = [head[0], head[1] +1] *doesn't work*
    stdscr.addstr(new_head[0], new_head[1], snake_ch)
    # store the new head
    snake.insert(0, new_head)
    # erase the tail by painting an white space
    stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
    snake.pop()

  stdscr.getch() 

curses.wrapper(snake)