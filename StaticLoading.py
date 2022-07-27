import curses, time, os
import sys
from time import sleep

def sp(str):
  for letter in str:
    sys.stdout.write(letter)
    sys.stdout.flush()
    time.sleep(0.09)
    
  print()

# to use it:

sp("▁ ▂ ▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃ ▁")

# this will output each of those different cacracters one by one
# thus making a loading animation