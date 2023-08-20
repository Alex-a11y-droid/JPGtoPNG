import sys
import os
from PIL import Image

arg1= sys.argv[1] #folder imagini initiale
arg2= sys.argv[2] #cale

path1= './'+arg1+'/'
path2= './'+arg2+'/'

check_file = os.path.isfile(path2)

if check_file==False:
    os.mkdir(path2)



img = os.listdir(path1)

for image in img:
    convert= image[:-4]
    im= Image.open(path1+image)
    im.save(path2+convert+'.png')

