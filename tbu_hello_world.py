#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import termbox
from termbox_util import termbox_util

with termbox.Termbox() as tbinst:
    tb = termbox_util(tbinst)

    # Find the middle of the screen
    maxx,maxy=tb.getmaxxy()
    x = int(maxx/2) - 6   # 6 is half of length of "Hello World"
    y = int(maxy/2)

    tb.clear()          # clear screen
    tb.border()         # border around screen
    tb.addstr(x, y, "Hello World!")  # Put Hello World! into screen
    tb.present()        # Display it

    # Get a keypress to exit
    event = tbinst.poll_event()
 
