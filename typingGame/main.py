import curses
from curses import wrapper

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    stdscr.clear() #clear the screen

    stdscr.addstr('hello world')
    stdscr.refresh()
    stdscr.getkey()

wrapper(main)

