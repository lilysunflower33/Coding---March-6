import curses 
import math
import random 

def initfeild(stdscr):

  sh, sw = stdscr.getmaxyx() 
  
  border = 