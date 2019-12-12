"""
This program takes a picture and encodes a message in the blue channel of the RGB color space. Blue was chosen specifically because studies have shown that the human eye is least sensitive to blue light, which allows slight changes to the blue channel to go completely undetected.

Works with jpg, png that don't have transparency, and tiff. Does not work with BMP or GIF.

"""

from PIL import Image
from os import path
#import binascii

def stegofy(a,b,c):
	#get pixel data
	im = Image.open(b , 'r')
	width, height = im.size
	totalPixles = width * height
	#print totalPixles
	pix_val = list(im.getdata())
	#print pix_val
	newList = []
	for i in pix_val:
		newList.append(list(i))
	#print newList
	
	#turn message into binary
	binaryMessage = ''.join('{:08b}'.format(ord(c)) for c in a) # from https://stackoverflow.com/questions/11599226/how-to-convert-binary-string-to-ascii-string-in-python#11599702
	#print binaryMessage
	if len(binaryMessage)> totalPixles:
		print "Uh, oh... there aren't enough pixles to hide that message!!! Please shorten the message or choose a higher resolution picture! I'm going to generate crap now :) \n"
	else:	
		counter = 0
		for i in newList:
		
		#print i[2]
			
			if counter < len(binaryMessage):
				if int(binaryMessage[counter]) == 0:
					if i[2] % 2 == 0:
						i[2] = i[2]
					elif i[2] % 2 != 0:
						if i[2] == 255: #255 is the max allowed val
							i[2] -=1
						else:
							i[2] += 1
				elif int(binaryMessage[counter]) == 1:
					if i[2] % 2 == 0:
						i[2] += 1
					elif i[2] % 2 != 0:
						i[2]=i[2]
				counter += 1
			elif i[2] % 2 == 0:
				i[2] = i[2]
			elif i[2] % 2 != 0:
				i[2] +=1
		newPic = []
		for i in newList:
			newPic.append(tuple(i))

		#encode new message into picture
		im2 = Image.new(mode = 'RGB', size = (width, height))
		im2.putdata(newPic)
		im2.save(c)
		print "All done!"



#####run the code 	
message = raw_input("Type your message: \n")
picture = raw_input("Picture file (if png, please ensure no transparency -- png is wonky): \n")
#while not picture.endswith(".jpg") or not path.isfile(picture):
while not path.isfile(picture):
		print "Picture does not exist... "
		picture = raw_input("Picture file: ")
	
#size1 = int(raw_input("Picture size 1 "))
#size2 = int(raw_input("Picture size2 "))
new = raw_input("New picture name (must be png): \n")

while new.endswith(".png") == False or len(new) <5:
	print "File must have .png extension... "
	new = raw_input("New picture name (must be png) \n")


stegofy(message, picture, new)

