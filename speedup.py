from curses import *
import curses
import sys,os

# function for main menu of the game
def mainmenu(stdscr):
	stdscr.clear()
	stdscr.addstr("---------------------\n")
	stdscr.addstr("|     1. Play       |\n")
	stdscr.addstr("---------------------\n")
	stdscr.addstr("---------------------\n")
	stdscr.addstr("|     2. Rules      |\n")
	stdscr.addstr("---------------------\n")
	stdscr.addstr("---------------------\n")
	stdscr.addstr("|     3. Quit       |\n")
	stdscr.addstr("---------------------\n")
	stdscr.addstr("enter choice : \n")
	input = stdscr.getch()
	stdscr.getch()
	# curses uses ASCII value in integer input
	if input == 49:   
		play(stdscr)
	elif input == 50:  
		rules(stdscr)
	elif input == 51:
		curses.nocbreak()
		stdscr.keypad(False)
		curses.echo()
		curses.endwin()
	stdscr.getch()

# function for description and rules
def rules(stdscr):
	stdscr.clear()
	stdscr.addstr("---------------------\n")
	stdscr.addstr("|    Description    |\n")
	stdscr.addstr("---------------------\n")
	stdscr.addstr("1. every second new words will flow from left side of your screen to right side of your screen. \n")
	stdscr.addstr("2. every word will stay on screen for 20 seconds. \n")
	stdscr.addstr("3. the word will disappear after you have written it. \n")
	stdscr.addstr("4. this game will tell you the total time taken, words per minute. \n")
	stdscr.addstr("5. if the word flows from left to right completely and you have not written that word then miss will increase with +1. \n")
	stdscr.addstr("6the word will disappear after you have written it.. every word will stay on screen for 20 seconds. \n\n\n")
	stdscr.addstr("---------------------\n")
	stdscr.addstr("|       Rules       |\n")
	stdscr.addstr("---------------------\n")
	stdscr.addstr("1. you have to type the words which are on the screen before it gets disappear \n")
	stdscr.addstr("2. after 10 miss your game will be over \n")
	stdscr.getch()
	mainmenu(stdscr)

def pname(stdscr):
	stdscr.clear()
	curses.echo()
	global player
	stdscr.addstr("Enter your name: \n")
	player = stdscr.getstr(1, 0, 15)
	play(stdscr, player)
	stdscr.getch()



def play(stdscr):
	stdscr.clear()
	x=0
	words=["start","totoro","vegeta","yagami","get","not","amazing","people","interesting","gross","ended","read","accelerate",
		"speed","excellent","negligible","expected","anything","walk","talk","angel","beautiful","haunted","horror","acting",
		"ignore","appearance","dominating","together","forever","yelled","hot","hustle","lime","ladyfinger","mango","height",
		"body","excess","soft","broken","broad","vulture","gaming","software","lovely","life","actually","emit","express",
		"feeling","famous","catch","capable","silent","helpful","caring","knowledgable","afraid","eligible","entity"]
	while 1:
		stdscr.addstr(1, 0, words[x])
		x=x+1
		stdscr.getch()
		stdscr.clear()
	

# y=24, x=80
def main():
	global stdscr
	stdscr = initscr()
	y, x = stdscr.getmaxyx()
	mainmenu(stdscr)
	stdscr.getch()
	stdscr.endwin()
	return 0;

if __name__ == '__main__':
	main();
