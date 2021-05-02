import curses 
from curses import textpad
import random

def snake_game(stdscr): 
  
  # get the screen and screen size 
  sh, sw = stdscr.getmaxyx()

  # hide curser
  curses.curs_set(False)
  
  # turn on nodelay to make the snake move by itself
  stdscr.nodelay(True)
  
  # timeout is set and counted in milliseconds 
  # timeout is the defult moving speed for the snake 
  interval = 250 
  stdscr.timeout(interval)

  # set the welcome message 
  game_msg(stdscr) 

  # define the gameboard
  border = [
    # top left vertex coordinate
    [5, 1],
    # bottom right vertex coordinate
    [sh - 2, sw - 2]  
  ]
  textpad.rectangle(stdscr, border[0][0], border[0][1], border[1][0], border[1][1])

  snake = snake_body(stdscr)

  # set up the defult moving direction 
  direction = curses.KEY_RIGHT

  # randomly generate and place the snake food 
  food = snake_food(stdscr) 
  snake_ch = chr(9608)

  score = 0
  points(stdscr, score) 
  score_increase = 1

  while True:
  # set the control while loop
    
    while True:
    # set the game loop
    
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
      # store the new head in a snake variable 
      snake.insert(0, new_head)

      # check if the snake ate the food
      if new_head != food:
        # erase the tail by painting a white space
        stdscr.addstr(snake[-1][0], snake[-1][1], ' ')
        # .pop() takes the last list item while also removing it from the list, the last item is set by defult (defult - 1)
        # you can choose the list item by using a number  (.pop(1))
        snake.pop() 
      else:
        # place the new snake food randomly
        food = snake_food(stdscr)

        # increase the score when the snake eats the food 
        score += score_increase 
        points(stdscr, score)

        # make the snake move faster by reducing the timeout 
        interval = interval - 10 
        stdscr.timeout(interval) 

        # make the speed increase slower once the snake gets too fast 
        #


      # if the snake touches the border game over 
      # border setup is at line 30 in the code
      # snake setup is at line 44 in the code

      # 
      if (snake[0][0] == border[0][0] or
      #
      snake[0][1] == border[0][1] or
      # 
      snake[0][0] == border[1][0] or
      # 
      snake[0][1] == border[1][1]): 

        #score_msg = YOUR SCORE IS 

        # game over message 
        msg = "GAME OVER!"
        stdscr.addstr(sh // 2 - 4, sw // 2 - len(msg) // 2, msg) 
        msg = "PRESS 'R' TO RESTART GAME, PRESS 'ESC' TO EXIT!"
        stdscr.addstr(sh // 2 - 3, sw // 2 - len(msg) // 2, msg)

        # turn off nodelay 
        stdscr.nodelay(False)
        # break out of game loop
        break

    # restart function input
    rkey = stdscr.getch()
    if rkey in[114, 82]:

      # turn on the nodelay mode 
      stdscr.nodelay(True)
      stdscr.timeout(interval)

      # clear the screen
      stdscr.clear()
      stdscr.addstr( sh // 2 - 4, sw // 2 - 10, ' ' * 15)
      stdscr.addstr( sh // 2 - 3, sw // 2 , ' ' * 40)

      # reset the snake to center of the screen
      snake = snake_body(stdscr)
      snake_ch = chr(9608) 
      # paint the snake 
      for unit in snake:
        stdscr.addstr(unit[0], unit[1], snake_ch) 

      # re-paint the border
      game_border(stdscr)

      # reset direction 
      direction = curses.KEY_RIGHT 

      # re-paint food 
      food = snake_food(stdscr)

      if snake[0][0] == food and snake[0][1] == food: 
        snake_food(stdscr) 

        interval = interval - 10 
        stdscr.timeout(interval) 

      # re-paint the score 
      score = 0
      points(stdscr, score) 
      score_increase = 1

      # reset the welcome message 
      game_msg(stdscr)

    elif rkey in[27]:
      break

def game_msg(stdscr):
  # paint the instructions and welcome message 

  sh, sw = stdscr.getmaxyx()

  welcome_msg = "SNAKE GAME"
  stdscr.addstr(1, sw // 2 - len(welcome_msg) // 2, welcome_msg) 
  welcome_msg = 'USE THE ARROW KEYS TO CHANGE DIRECTION' 
  stdscr.addstr(2, sw // 2 - len(welcome_msg) // 2, welcome_msg)
  welcome_msg = 'PRESS ESC TO EXIT' 
  stdscr.addstr(3, sw // 2 - len(welcome_msg) // 2, welcome_msg)

def game_border(stdscr): 
  # function to paint the border 

  sh, sw = stdscr.getmaxyx()

  border = [
    # top left vertex coordinate
    [5, 1],
    # bottom right vertex coordinate
    [sh - 2, sw - 2]  
  ]

  # draw the border of the gameboard
  textpad.rectangle(stdscr, border[0][0], border[0][1], border[1][0], border[1][1])

  # another way to draw the border
  # textpad.rectangle(stdscr, 1, 1, sh - 1, sw - 1)

def snake_body(stdscr): 
  # function for painting the snake 

  sh, sw = stdscr.getmaxyx()
  
  snake = [
    # head
    [sh // 2, sw // 2 + 1],
    # body
    [sh // 2, sw // 2],
    # tail
    [sh // 2, sw // 2 - 1],
  ]

  return snake

def snake_food(stdscr): 
  # create a function to radomly generate the snake food without needing to type in code mutiple times
  
  sh, sw = stdscr.getmaxyx()

  food_ch = "*"
  food = [
    # set the coordinates of where the food will be generated radomly 
    random.randint(6, sh - 3),
    random.randint(3, sw - 3)
  ]

  # place the food 
  stdscr.addstr(food[0], food[1], food_ch)

  # return function will block anything after it from being executed inside the function 
  return food 

#def timeout_interval(stdscr): 

def points(stdscr, score): 

  # paint the score as the snake eats the food 
  stdscr.addstr(4, 2, "SCORE: ") 
  stdscr.addstr(str(score)) 

# def restart(stdscr): 
  # restart game function 

curses.wrapper(snake_game)

# bonus work: 

  # make the snake game run by itself without a person playing 

  # colour the snake 