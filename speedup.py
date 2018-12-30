from curses import *
import curses

# function for main menu of the game
def mainmenu(stdscr, y, x):
	stdscr.clear()
	stdscr.addstr("1. Play \n", curses.color_pair(4))
	stdscr.addstr("2. Rules \n", curses.color_pair(4))
	stdscr.addstr("3. Quit \n", curses.color_pair(4))
	stdscr.addstr("enter choice : \n", curses.color_pair(4))
	input = stdscr.getch()
	stdscr.getch()
	# curses uses ASCII value in integer input
	if input == 49:   
		pname(stdscr)
	elif input == 50:  
		rules(stdscr)
	elif input == 51:
		curses.nocbreak()
		stdscr.keypad(False)
		curses.echo()
		curses.endwin()
	stdscr.getch()

# function for description and rules
def rules(stdscr, y, x):
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

def pname(stdscr, y, x):
	stdscr.clear()
	curses.echo()
	global player
	stdscr.addstr("Enter your name: \n", curses.color_pair(4))
	player = stdscr.getstr(1, 0, 15)
	play(stdscr, player)
	stdscr.getch()

def play(stdscr, player, y, x):
	stdscr.clear()
	stdscr.addstr("abc")
	stdscr.getch()

def main():
	global stdscr
	stdscr = initscr()
	y, x = stdscr.getmaxyx()
	mainmenu(stdscr, y, x)
	stdscr.getch()
	stdscr.endwin()
	return 0;

if __name__ == '__main__':
	main();