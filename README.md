# python_termbox_util
A library to sit on top of termbox in python to provide a bunch of curses like functions and virtual viewplanes.

Termbox is nice and all, but curses provides more goodies to play with.
This library sits provides a number of curses-like functions to draw on a termbox screen.

A viewplane class lets you create virtual viewplanes of arbitary size and map a 
viewport onto the viewplan in the real termbox display. The viewplane functions
match the termbox_util functions and so you can embed viewplanes in viewplanes.

This is not fine, mature code. I'm just throwing it out there so it doesn't get
lost on my disk. Someone might find it useful. I used it to make a linux Point-of-sale
curses program available on Windows without the user having to install half
a dozen libraries.

How to use..

