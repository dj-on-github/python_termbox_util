# python_termbox_util
A library to sit on top of termbox in python to provide a bunch of curses like functions and virtual viewplanes.

Termbox is nice and all, but curses provides more goodies to play with.
This library provides a number of curses-like functions to draw on a termbox screen.

A viewplane class lets you create virtual viewplanes of arbitary size and map a 
viewport onto the viewplane in the real termbox display. The viewplane functions
match the termbox functions and so you can embed viewplanes in viewplanes.

This is not fine, mature code. I'm just throwing it out there so it doesn't get
lost on my disk. Someone might find it useful. I used it to make a linux Point-of-sale
curses program available on Windows without the user having to install half
a dozen libraries. Also the debugger in py6502 uses it.

**Hello World**

The hello world example is pretty verbose by hello world standards.
It clears the screen, works out where the middle is and puts
the text in the middle.


```
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
```

For now the examples moving_window.py, tbu_hello_world.py and util_demo.py are all the documentation.


