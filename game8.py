#game3 more function driven
#game 8 going to take out dictionary and just use functions with an elif to function on random function 
#this works but not way I wanted to I wanted to use dictionary as dispatcher
from sys import exit
import random  
#from random import randint
from textwrap import dedent 

def victory():
	print("CONGRADULATIONS YOU WIN YOU GET TO LIVE")
	exit(0)

			
def death():
	print("YOU ARE DEAD PRESS START BUTTON TO TRY AGAIN")
	print("YOU ARE DEAD PRESS START BUTTON TO TRY AGAIN")
	exit(0)

#launch point and dirctory to dictionary book which is nerve center of scenes
def start():
	print("#"*75)
	print("#"*75)
	print("#"*75)
	print("\nYou are in start function")
	print("\nHere are is your menu of rooms you may enter searching for remote control")
	print("\nbridge")
	print("\narmoury")
	while True:
		user = input("\nType in one of the two menu options...")
		if user == ("bridge"):
			return bridge()
		elif user == ("armoury"):
			return armoury()
		else:
			print("\nTry again or hit CTL-Z")
		
	

def armoury():
	names = ["armoury","bridge","shuttle_room"]
	myDict = {"armoury":armoury,"bridge": bridge,"shuttle_room":shuttle_room}
	print("#"*75)
	print("#"*75)
	print("#"*75)
	print("\nYou are in the armoury there is no remote in this room but there is a door that is to an unknown spot")
	print("\nGrab a weapon  and enter door or  return to start")
	print("\nOnce you have your weapon and want to proceed type random or y to return to main menu")
	while True:
		choice = input("\nIf you want to return to start type 'start' else type 'random' ")
		if choice == ('start'):
			return start()
		elif choice == ('random'):
			print("You have stepped on a telport landmine when you entered room of unknown door ")
			print("You will now be teleported by muxing technology to another room")
			user = random.choice(names)
			return myDict[user]()
			
		else:
			print("Your typing is bad try again")
			
	
def shuttle_room():
		print("You have found the shuttle room, but you must guess the lock code for the shuttle")
		print("The code is a digit between 1 and 9 good luck")
		print("If you guess correctly you may enter the shuttle escape the mother ship and win the game")
		print("Guess wrong and you will be killed by the poison gas used to defend pods from intruders")
		
		code = f"{random.randint(1,9)}"
		guess = int(input("[keypad]> "))
		guesses = 0 
		while guess != code and guesses < 10:
			print("Clock is ticking try again")
			guesses  += 1
			guess = input("[keypad]> ")
		if guess == code:
			print("Congradulations!! you won the game you have access to shuttle!")
			return victory()
		else:
			print("You have run out of attempts you are dead")
			return death()
			
	
	
def bridge():
	print("#"*75)
	print("\nWelcome to the bridge")
	while True:
		choice = input("\nIf you want to search bridge for remote type 'y' if you want to return to 'start' for more options type start")
		if choice == ('y'):
			print("\n")
			print("Congradulations you have found the door to the shuttle room\n")
			return shuttle_room()
		elif choice == ('start'):
			return start()
		else:
			print("\nYour typing is very bad please try again")
			

	
start()
