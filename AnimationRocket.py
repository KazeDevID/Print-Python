import os
import time

def animate_rocket():
  distance_from_top = 20
  while True:
    print("\n" * distance_from_top)
    print("          /\        ")
    print("          ||        ")
    print("          ||        ")
    print("         /||\        ")
    time.sleep(0.2)
    os.system('clear')  
    distance_from_top -= 1
    if distance_from_top < 0:
      distance_from_top = 20
  
  
#Main Program Starts Here....
animate_rocket()