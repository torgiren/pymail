#*-* coding: utf-8 *-*
import locale

locale.setlocale(locale.LC_ALL,"")
import curses
import time
import logging
class Interface:
    class List:
        def __init__(self, size, win):
            self.elements = []
            self.act = None
            self.start_pos = None
            self.size = size
            self.win = win

            self.log = logging.getLogger('Interface::List')
            self.log.addHandler(logging.FileHandler('log.log'))
            self.log.setLevel(logging.DEBUG)

        def add(self, el):
            self.elements.append(el)
            if not self.act:
                self.act = 0
            if not self.start_pos:
                self.start_pos = 0

        def down(self):
            if self.act == len(self.elements) -1:
                return
            self.act += 1
            if self.act - self.start_pos >= self.size:
                self.start_pos += 1

        def up(self):
            if self.act == 0:
                return
            self.act -= 1
            if self.act < self.start_pos:
                self.start_pos -= 1

        def show(self):
            self.win.erase()
            for n, i in enumerate(self.elements[self.start_pos:self.start_pos + self.size]):
                style = curses.A_NORMAL
                if n + self.start_pos == self.act:
                    style = curses.A_REVERSE
                self.log.debug('addstr: %s' % i)
                self.win.addstr(n,1, "%5d %s" % (n + self.start_pos, i), style)
            self.win.noutrefresh()

    def __init__(self):
        self.stdscr = curses.initscr()
        self.stdscr.clear()
        self.stdscr.refresh()
        curses.noecho()
        curses.cbreak()
        curses.curs_set(0)

        y_size = 40
        self.list_win = curses.newwin(y_size + 1,140, 1,1)
        self.list = Interface.List(y_size, self.list_win)


        self.log = logging.getLogger('Interface')
        self.log.addHandler(logging.FileHandler('log.log'))
        self.log.setLevel(logging.DEBUG)
    def __del__(self):
        curses.endwin()

    def add_list_item(self, date, f, t, sub):
#        self.log.debug('%s %s %s %s' % (type(f), type(t), type(sub), type(date)))
#        self.log.debug('%s %s %s' % (len(f), len(t), len(sub)))
        f = f[:35].ljust(35).encode('utf8')
        t = t[:35].ljust(35).encode('utf8')
        sub = sub[:35].ljust(35).encode('utf8')
        self.log.debug('len: %d, type: %s' % (len(f.ljust(35)), type(f)))
        self.list.add(r"%s %s %s %s" % (f, t, sub, date))


    def show_list(self):
        self.list.show()

    def get_key(self):
        key = self.stdscr.getkey()
        if key == 's':
            self.list.down()
            self.show_list()
        if key == 'w':
            self.list.up()
            self.show_list()
        curses.doupdate()

    def refresh(self):
        self.stdscr.refresh()
#        self.list.refresh()
#        self.menu.refresh()
