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
	decoded_message = ""
	for i in range(0, len(message), 8):
		temp_char = chr(int(message[i:i+8], 2))
		if temp_char == '\x00':
			break
		else:
			decoded_message += temp_char #''.join(chr(int(message[i:i+8], 2))
	#message = ''.join(chr(int(message[i:i+8], 2)) for i in range(0, len(message), 8))# from https://stackoverflow.com/questions/11599226/how-to-convert-binary-string-to-ascii-string-in-python#11599702
	print(decoded_message)

picture = input("Name of picture ")
while not path.isfile(picture):
	print("that is not a valid file name... ")
	picture = input("Name of picture: ")
else:
	destegofy(picture)

	
#destegofy(picture)