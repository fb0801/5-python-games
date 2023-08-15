import curses
from curses import wrapper

def start_screen(stdscr):
    stdscr.clear() #clear the screen

    stdscr.addstr('Welcome to the Speed typing test')
    stdscr.addstr('\nPress any key to begin!')

    stdscr.refresh()
    stdscr.getkey()

def wpm_test(stdscr):
    tget_text = ['hello world this is some text','To learn to type quickly, practice often and adopt the proper technique. This will help you develop muscle memory and create automatic reflexes. Keep practicing and gradually pick up the pace. You will see results after just a few weeks!', 
                   'Fly relate house expert charge interview itself because job consider knowledge color low late hope significant understand business home where entire tonight want heavy such sell way employee by civil hold executive become station successful enough task exacFtly reflect about fear let perform term always industry spend feeling play federal performance season major buy ability evidence treat wall true like project return popular whether inside especially say size fast really activity final use strategy maintain see add explain conference school line almost economy rise various claim range imagine their central watch art right century scientist thought radio rule call administration light concern pick coach make chair suddenly information show rock pretty ready hang finally music cold join professional later though series head college building career consumer everyone sure area maybe history wear land matter save realize family plan risk compare prepare simply meet last however score rest card also bring begin movement moment material night reduce these live condition yeah food than morning city speak enjoy laugh teacher cell health well summer player interesting might subject movie themselves price trip address anything million get image probably recent why reveal billion write hair may remove car response just']
    target_text = 'hello this is some text'
    current_text= []
   
    

    
    

    while True:
        stdscr.clear() #clear the screen
        stdscr.addstr(target_text)

        for char in current_text:
            stdscr.addstr(char, curses.color_pair(1))

        stdscr.refresh()

        key = stdscr.getkey()

        if ord(key) == 27:
            break
        if key in ('KEY_BACKSPACE', '\b', '\x7f'):
            if len(current_text) > 0:
                current_text.pop()

            else:
                current_text.append(key)

        current_text.append(key)

        

def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

    start_screen(stdscr)
    wpm_test(stdscr)

wrapper(main)

