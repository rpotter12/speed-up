from curses import *

# function for main menu of the game
def mainmenu(stdscr):
	stdscr.clear()
	stdscr.addstr("1. Play \n")
	stdscr.addstr("2. Rules \n")
	stdscr.addstr("3. Quit \n")
	stdscr.addstr("enter choice : \n")
	input = stdscr.getch()
	if input == 49:
		pname(stdscr)
	elif input == 50:  # curses uses ASCII value in integer input
		rules(stdscr)
	elif input == 51:
		exit()
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
	stdscr.addstr("Enter your name: ")
	stdscr.getch()

#def play():


def main():
	global stdscr
	stdscr = initscr()
	mainmenu(stdscr)
	getch()
	endwin()
	return 0;

if __name__ == '__main__':
	main();