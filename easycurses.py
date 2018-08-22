# -*- coding: utf-8 -*-
import curses
class EasyCurses(curses):

    def __init__(self):
        super(EasyCurses, self).__init__()
        scr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        scr.keypad(1)

