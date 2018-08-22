# -*- coding: utf-8 -*-
import curses
import curses.textpad
class View():

    def __init__(self):
        super(View, self).__init__()
        self.scr = curses.initscr()
        curses.noecho()
        curses.start_color()
        curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
        curses.cbreak()
        self.scr.keypad(1)

    def mainmenu(self):
        self.clear()
        curses.noecho()
        options = ['Add Movie', 'Browse All Movies']
        for i in range(len(options)):
            self.scr.addstr(3 + i, 2, options[i], curses.color_pair(1))
        self.scr.addstr(1, 1, 'a-add, b-browse')
        self.scr.refresh()
        while True:
            key = self.scr.getch()
            if (key == ord("a")):
                return 'addform'
                break
            elif (key == ord("b")):
                return 'browse'
                break

    def addForm(self):
        self.clear()
        curses.echo()
        self.scr.addstr(1, 1, 'Add Movie Form')
        self.scr.addstr(2, 1, 'If you made a mistake you can edit it later', curses.color_pair(2))
        self.scr.addstr(4, 1, 'Title', curses.color_pair(1))
        self.scr.addstr(5, 1, 'Description (ctr+g to end editing', curses.color_pair(1))
        self.scr.addstr(12, 1, 'Your rating', curses.color_pair(1))
        self.scr.addstr(13, 1, 'Extra info', curses.color_pair(1))
        self.scr.refresh()
        title=self.scr.getstr(4,10, 100)
        curses.beep()
        win = curses.newwin(6, 30, 6, 10)
        curses.noecho()
        tb = curses.textpad.Textbox(win)
        desc = tb.edit()
        desc = tb.gather()
        self.scr.refresh()
        curses.echo()
        rating=self.scr.getstr(12,15, 1)
        info=self.scr.getstr(13,15, 100)
        return(title, desc,'',rating,info)
        curses.noecho()
        self.mainmenu()
    def browse(self,loaded_data):
        self.clear()
        self.scr.addstr(1, 1, 'Browse Movies',curses.color_pair(3))
        position=0
        while True:
            if (position<=0):position=0
            elif (position>=len(loaded_data)):position=len(loaded_data)-1
            for i in range(len(loaded_data)):
                if (i!=position):
                    self.scr.addstr(3+i,1,loaded_data[i].title)
                    self.scr.refresh()
                elif (i==position):
                    self.scr.addstr(3+i,1,loaded_data[i].title,curses.color_pair(3))
                    self.scr.refresh()


            key=self.scr.getch()
            if (key==curses.KEY_UP):
                position=position-1
            elif (key==curses.KEY_DOWN):
                position=position+1
            elif (key==curses.ascii.NL):
                return position
                print ("ENTER")
    def details(self, choice, data):
        self.clear()
        self.scr.addstr(1, 1, 'Film: ', curses.color_pair(1))
        self.scr.addstr(1, 7, data[choice].title)
        self.scr.addstr(3, 1, 'Description', curses.color_pair(1))
        self.scr.addstr(4, 2, data[choice].desc)
        self.scr.addstr(12, 1, 'Rating: ', curses.color_pair(1))
        self.scr.addstr(12,12, data[choice].rating)
        self.scr.addstr(13, 1, 'Extra info: ', curses.color_pair(1))
        self.scr.addstr(13,15, data[choice].info)
        self.scr.addstr(15, 1, 'RETURN to retunr ;)', curses.color_pair(3))
        self.scr.refresh()
        while True:
            key=self.scr.getch()
            if (key==curses.ascii.NL):
                    return 'back'
                    break

    def clear(self):
        self.scr.clear()
        self.scr.refresh()
