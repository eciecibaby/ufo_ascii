import os
import time
import sys

running = True

ufo1 = """
 _____
(_____)
"""

ufo2 = """
    _____
   (_____)
"""

ufo3 = """
        _____
       (_____)
"""

try:
	while running:
		os.system('clear')
		print(ufo1)
		time.sleep(0.5)
		os.system('clear')
		print(ufo2)
		time.sleep(0.5)
		os.system('clear')
		print(ufo3)
		time.sleep(0.5)
		os.system('clear')
		print(ufo2)
		time.sleep(0.5)
except KeyboardInterrupt:
	sys.exit()
