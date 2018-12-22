from unicurses import *

# function for main menu of the game
def mainmenu():
	clear()
	addstr("1. Play \n")
	addstr("2. Rules \n")
	addstr("3. Quit \n")
	addstr("enter choice : ")
	input = getch()
	if input == 50:  # curses uses ASCII value in integer input
		rules()
	elif input == 51:
		exit()
	getch()

# function for description and rules
def rules():
	clear()
	addstr("---------------------\n")
	addstr("|    Description    |\n")
	addstr("---------------------\n")
	addstr("1. every second new words will flow from left side of your screen to right side of your screen. \n")
	addstr("2. every word will stay on screen for 20 seconds. \n")
	addstr("3. the word will disappear after you have written it. \n")
	addstr("4. this game will tell you the total time taken, words per minute. \n")
	addstr("5. if the word flows from left to right completely and you have not written that word then miss will increase with +1. \n")
	addstr("6the word will disappear after you have written it.. every word will stay on screen for 20 seconds. \n\n\n")
	addstr("---------------------\n")
	addstr("|       Rules       |\n")
	addstr("---------------------\n")
	addstr("1. you have to type the words which are on the screen before it gets disappear \n")
	addstr("2. after 10 miss your game will be over \n")
	getch()
	mainmenu()

def main():
	stdscr = initscr()
	mainmenu()
	getch()
	endwin()
	return 0;

if __name__ == '__main__':
	main();