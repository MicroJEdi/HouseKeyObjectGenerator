import Image

def readImage():
	im = Image.open("key.jpg")
	f = open("outputKey.txt", "w")
	f.write("[")
	xsize, ysize = im.size
	x = 0
	y = 0
	threash = 30
	for x in range(0,xsize):
		for y in range(0,ysize):
			r, g, b = im.getpixel((x,y))
			avgVal = (r + g + b) / 3
			diff = abs(avgVal-r) + abs(avgVal-g) + abs(avgVal-b)
			if(avgVal < 110 or diff > threash):
				im.putpixel((x,y), (255, 255, 255))
				f.write(str(x)+","+str(y)+",")
			else:
				im.putpixel((x,y), (0, 0, 0))
				f.write("")
	im.save("output.jpg")
	f.close()
	print "done"

readImage()
