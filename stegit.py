"""
Steg it!

"""


option = input("Would you like to [S]tegify or [D]estegify?: ")
while option not in ['S','s','D','d']:
	print("Invalid response")
	option = input("To stegify, enter S. To destegify, enter D: ")
def stegit(x):
	if x == "S" or x == 's':
		import stegofy
	elif x == "D" or x == 'd':
		import destegofy
		
stegit(option)
		
	
