import os
import glob

# dir = "layers/5-legs"
# dir = "layers/6-hat"
# dir = "layers/7-face"
# dir = "layers/8-hand"
# dir = "layers/12-legs-trim"
dir = "layers/13-hoody-hoods"

for filename in os.listdir(dir):
    start = str(filename)
    final = start[6:]
    start = dir + "/" + start
    final = dir + "/" + final
    print(start, " => ", final)
    os.rename(start, final)