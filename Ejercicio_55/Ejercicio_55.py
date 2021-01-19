"""from io import *
import io

nombres = open("bd_nombres.txt", "r+")

nombres.seek(0)

text = "Hola"

nombres.write(text)

nombres.seek(0)

y = nombres.read()

x = nombres.readinto([1:2])

print(y)

nombres.close()"""

#!/usr/bin/python
from os import *
import stat

import os 
  
# defining path and flag 
path = "C:/Users/jomuz/Desktop/Python/RegEx.txt"
flags = stat.UF_IMMUTABLE 
  
val = os.chflags(path, flags) 
  
# Doesn't return any value, so 
# nothing will be printed 
print("Operation successful, returning value: %s" %val)