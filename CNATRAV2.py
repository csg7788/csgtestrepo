from sys import exit

print("See if the push pull works - Tony")

def college():
	print ("Where did you get your commission?")
	print ("1. Naval Academy")
	print ("2. ROTC")
	print ("3. AOCS")
	NSS = 0
	
	coll = int(input("1,2 or 3?:\n\t>"))
	
	if coll == 1:
		NSS = NSS + 20
		print ("Ring knocker!")
		primary (NSS)
	elif coll == 2:
		NSS = NSS + 15
		print ("Party on, dude!")
		primary (NSS)
	elif coll == 3:
		NSS = NSS + 10
		print ("You're a poop!")
		primary (NSS)
	else:
		NSS = NSS - 5
		print ("Try again.")
		college()

	
def primary (NSS):
	print ("Time to fly")
	
	print ("What happens when stick goes left?\n 1. Right wing goes down?\n 2.Right wing goes up?")
	
	stupid_1 = False
	stupid_2 = False
	
	stick = int (input("1 or 2?:\n\t>"))
	
	if stick == 1:
		NSS = NSS-5
		stupid_1 = True
		print ("Nope.")
	elif stick == 2:
		NSS = NSS + 5
		print ("Yep")
	else:
		print ("Wha?")
		NSS = NSS - 5
		stupid_1 = True

	print ("What happens when stick goes right?\n 1. Right wing goes down?\n 2.Right wing goes up?")
	
	stick = int (input("1 or 2?:\n\t>"))
	
	if stick == 1:
		NSS = NSS + 5
		print ("Yep.")
	elif stick == 2:
		NSS = NSS - 5
		stupid_2 = True
		print ("Nope")
	else:
		NSS = NSS - 5
		stupid_2 = True
	
	if stupid_1 == True and stupid_2 == True:
		print ("Naval Aviation is not for you.")
		print ("Washout.  Go back to being a civilian.")
		exit()
	else:
		advanced_decision (NSS)

def advanced_decision (NSS):
	print ("Now we're gonna decide the rest of your life, sorta.")
	
	i = 0
	w = 0

	while i <= 10:
		print (10 - i)
		while w < 10000000:
			w = w + 1
		i = i + 1
		w = 0	
	print ("Decision Complete.")
	print (NSS)

college()

## this series of print statements is to test branch functionality

print("his series of print statements is to test branch functionality")
print("this series of print statements is to test branch functionality")
print("this series of print statements is to test branch functionality")

	
exit()

# python CNATRA.py
