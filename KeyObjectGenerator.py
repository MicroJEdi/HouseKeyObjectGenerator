from PIL import Image

def readImage():
	im = Image.open("key.jpg")
	f = open("outputKey.txt", "w")
	#f.write("[")
	xsize, ysize = im.size
	x = 0
	y = 0
	threash = 60
	rprev1, gprev1, bprev1 = im.getpixel((20,20))
	rprev2, gprev2, bprev2 = im.getpixel((300,20))
	for x in range(0,xsize):
		for y in range(0,ysize):
			r, g, b = im.getpixel((x,y))
			diff1 = abs(rprev1-r) + abs(gprev1-g) + abs(bprev1-b)
			diff2 = abs(rprev2-r) + abs(gprev2-g) + abs(bprev2-b)
			if(diff1 > threash and diff2 > threash):
				im.putpixel((x,y), (255,255,255))
				f.write(str(x)+","+str(y)+"\n")
			else:
				f.write("")
				im.putpixel((x,y), (0,0,0))
	im.save("output.jpg")
	f.close()
	print("done")

readImage()
