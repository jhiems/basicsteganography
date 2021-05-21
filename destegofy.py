
from PIL import Image
from os import path
def destegofy(x):
	im = Image.open(picture , 'r')
	pix_val = list(im.getdata())
	message = ""
	for i in pix_val:
		if i[2] %2 == 0:
			message = message + "0"
		elif i[2] % 2 == 1:
			message = message +"1"	
	message = ''.join(chr(int(message[i:i+8], 2)) for i in xrange(0, len(message), 8))# from https://stackoverflow.com/questions/11599226/how-to-convert-binary-string-to-ascii-string-in-python#11599702
	print message

picture = raw_input("Name of picture ")
while not path.isfile(picture):
	print "that is not a valid file name... "
	picture = raw_input("Name of picture: ")
else:
	destegofy(picture)

	
#destegofy(picture)
