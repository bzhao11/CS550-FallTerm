'''
Benjamin Zhao
Ms. Healey
A Block 

For this project, I really wanted to have at least two fractal images that would contrast but complement each other. As a result, my first and third 
image does just that. Since they have the same calculations for the color portion of the code, I specifically spent quite a bit of time finding a balanced
but contrasting fractal in the mandelbrot set. As a result, I incorporate a spiral for my first image and a vein type picture in my third image. 

The Julia set I incorporated into my second image was just a really cool extension of the red/purple color I was going for. I did some extra research and 
thought the fractal that was printed was really cool so I decided to add that in. The Julia set also connects to the other two as it brings a mistique to the 
red/green + blue theme I have going. 

'''




import random
import tkinter
from tkinter import *

# recursive mandelbrot function gives us the number of iterations to escape
def mandelbrot(z, c, count):
	z = z*z+c
	count = count + 1
	if abs(z) >= 2 or count > maxIt-1: 
		return count
	else: 
		return mandelbrot(z,c,count)


# Fractal 1
WIDTH = 640 # width and height of our picture in pixels
HEIGHT = 640
xmin = -0.5554977137459# changed to the zoom we want to see 
xmax =  -0.547620056012803
ymin = 0.5328271319158665
ymax = 0.5407047896662094

maxIt = 255 # max iterations; corresponds to color


window = Tk()

# create a canvas, and place it in the window
canvas = Canvas(window, width = WIDTH, height = HEIGHT, bg = "#000000")

# set up the canvas so it can hold a picture
img = PhotoImage(width = WIDTH, height = HEIGHT)
canvas.create_image((0, 0), image = img, state = "normal", anchor = tkinter.NW)

# loop through all the pixels in the image
for row in range(HEIGHT):
	for col in range(WIDTH):
		# calculate C for each pixel
		rw = ((xmax-xmin)/WIDTH)*col+xmin
		cl = ((ymax-ymin)/HEIGHT)*row+ymin
		
		c = complex(rw, cl)
		z = complex(0, 0)
		r = mandelbrot(z,c,0)
		#color selected
		rd = hex(r)[2:].zfill(2)
		gr = hex((255+r*50)%255)[2:].zfill(2)
		bl = hex((r*30)%255)[2:].zfill(2)

		img.put("#" + rd + gr + bl, (col, row))

# update the canvas and display drawing
canvas.pack()

# Fractal 2 (Julia set)
WIDTH = 640 # width and height of our picture in pixels
HEIGHT = 640
xmin2 = -2 #the zoom we want to see 
xmax2 = 2
ymin2= -2
ymax2 = 2

maxIt = 255 # max iterations; corresponds to color


window2 = Toplevel()

canvas2 = Canvas(window2, width = WIDTH, height = HEIGHT, bg = "#000000")

img2 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas2.create_image((0, 0), image = img2, state = "normal", anchor = tkinter.NW)


for row in range(HEIGHT):
	for col in range(WIDTH):
		# calculate C for each pixel
		rw = ((xmax2-xmin2)/WIDTH)*col+xmin2
		cl = ((ymax2-ymin2)/HEIGHT)*row+ymin2
		#form Julia set by switching z and c, then assigning specific complex number to c
		z = complex(rw, cl)
		c = complex(0.3, -.01)
		r = mandelbrot(z,c,0)
		
		#colors
		rd = hex((255+r*50)%255)[2:].zfill(2)
		gr = hex((255+r*20)%255)[2:].zfill(2)
		bl = hex((r*30)%255)[2:].zfill(2)
		img2.put("#" + rd + gr + bl, (col, row))

# update the canvas and display our drawing
canvas2.pack()

# Fractal 3
WIDTH = 640 # width and height of our picture in pixels
HEIGHT = 640
xmin3 = -1.4018603791813975 #the zoom we want to see 
xmax3 = -1.4012862984291565
ymin3 = -.0002927462003972078
ymax3 = .0002813345518436927

maxIt = 255 # max iterations; corresponds to color


window3 = Toplevel()

canvas3 = Canvas(window3, width = WIDTH, height = HEIGHT, bg = "#000000")

img3 = PhotoImage(width = WIDTH, height = HEIGHT)
canvas3.create_image((0, 0), image = img3, state = "normal", anchor = tkinter.NW)


for row in range(HEIGHT):
	for col in range(WIDTH):
		# calculate C for each pixel
		rw = ((xmax3-xmin3)/WIDTH)*col+xmin3
		cl = ((ymax3-ymin3)/HEIGHT)*row+ymin3
		
		c = complex(rw, cl)
		z = complex(0, 0)
		r = mandelbrot(z,c,0)
		#colors
		rd = hex(r)[2:].zfill(2)
		gr = hex((255+r*50)%255)[2:].zfill(2)
		bl = hex((r*30)%255)[2:].zfill(2)

		img3.put("#" + rd + gr + bl, (col, row))

# update the canvas and display our drawing
canvas3.pack()

mainloop()


