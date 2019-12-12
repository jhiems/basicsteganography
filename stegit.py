"""
Steg it!

"""


option = raw_input("To stegify, enter S. To destegify, enter D: ")
while option not in ['S','s','D','d']:
	print "Invalid response"
	option = raw_input("To stegify, enter S. To destegify, enter D: ")
def stegit(x):
	if x == "S" or x == 's':
		import stegofy
	elif x == "D" or x == 'd':
		import destegofy
		
stegit(option)
		
	
