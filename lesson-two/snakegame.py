import curses 
from curses import textpad
import random

def snake(stdscr): 
  
  sh, sw = stdscr.getmaxyx()

  # hide curser
  curses.curs_set(False)
  
  # turn on nodelay to make the snake move by itself
  stdscr.nodelay(True)
  
  # timeout is set and counted in milliseconds 
  # timeout is the defult moving speed for the snake 
  interval = 250
  stdscr.timeout(interval)

  # define the gameboard
  border = [
    [1, 1],
    [sh - 2, sw -2]  
  ]

  # draw the border of the gameboard
  textpad.rectangle(stdscr, border[0][0], border[0][1], border[1][0], border[1][1])

  # another way to draw the border
  # textpad.rectangle(stdscr, 2, 2, sh - 2, sw - 2)

  # snake variable setup
  snake = [
    # head
    [sh // 2, sw // 2 + 1],
    # body
    [sh // 2, sw // 2],
    # tail
    [sh // 2, sw // 2 - 1],
  ]

  snake_ch = chr(9608)

  # paint the snake 
  for unit in snake:
    stdscr.addstr(unit[0], unit[1], snake_ch)

  # set up the defult moving direction 
  direction = curses.KEY_RIGHT

  # randomly generate and place the snake food 
  food()

  while True:

    user_key = stdscr.getch()

    # exit game when player preses ESC 
    if user_key in [27]:
      break; 

    # reset the initial direction 
    if user_key == curses.KEY_UP: 
      direction = user_key 
    elif user_key == curses.KEY_LEFT: 
      direction = user_key 
    elif user_key == curses.KEY_RIGHT: 
      direction = user_key 
    elif user_key == curses.KEY_DOWN: 
      direction = user_key 

    # another way to reset the initial direction 
    # if user_key in [curses.KEY_UP, curses.KEY_DOWN, curses.KEY_LEFT, curses.KEY_RIGHT]:
      # direction = user_key

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
      new_head = [head[0] + 1, head[1]]

    # calculate the new snake after it moves
    stdscr.addstr(new_head[0], new_head[1], snake_ch)
    # store the new head
    snake.insert(0, new_head)

    # check if the snake ate the food
    if new_head != food:
      # erase the tail by painting a white space
      stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
      # .pop() takes the last list item while also removing it from the list, last item is defult (defult - 1)
      # you can choose the list item by using a number  ex. .pop(1)
      snake.pop() 
    else:
      # place the new snake food randomly
      food()

      # make the snake move faster by reducing the timeout 
      #interval = interval - 10
      #stscr.timeout(interval) 
  
  # check if the snake touches the border of the game
  snake[0][0]
  snake[1][0]

  stdscr.getch() 

def food(stdscr): 
  # create a function to radomly generate the snake food 
  
  sh, sw = stdscr.getmaxyx()

  food_ch = "*"
  food = [
    random.randint(3, sh - 3),
    random.randint(3, sw - 3)
  ]
  stdscr.addstr(food[0], food[1], food_ch)

curses.wrapper(snake, food)