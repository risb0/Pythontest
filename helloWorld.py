import time

name = input("Please enter your name: \n")

def hi(name):
	print("Hello {}\n".format(name))

def typingMsg():
	print("\nUser is typing...\n")

typingMsg()
time.sleep(5)	
hi(name)
