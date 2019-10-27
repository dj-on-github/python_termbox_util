#!/usr/bin/python3
# -*- encoding: utf-8 -*-

import termbox
import random

from termbox_util import termbox_util
from termbox_util import viewplane

with termbox.Termbox() as tbinst:
    tb = termbox_util(tbinst)
    
    maxx,maxy = tb.getmaxxy()
    
    # A virtual viewplane the same size as the screen    
    vp=viewplane(maxx,maxy) 
    vptb = termbox_util(vp)
    
    #view window width
    vww = 8
    #view window height
    vwh = 8
    
    srcx = 8
    srcy = 8
    
    viewx = 8
    viewy = 8

    
    #Fill the viewplane with stuff.
    vptb.clear()
    for y in range(maxx):
        for x in range(maxy):
            vptb.addstr(x,y,random.choice([u"\u2215",'\\','-',' ']))
            
    tb.clear()
    tb.box()        
    tb.present()
    pid1 = tb.add_persistent_viewplane_window(vp,vww,vwh,srcx,srcy,viewx,viewy,active=True)
    
    newx=10
    newy=10
    
    while True:
            
        tb.move_persistent_viewplane_window(pid1,newx,newy)
        tb.move_persistent_viewplane_position(pid1,newx,newy)
        tb.draw_persistent_viewplanes()
        tb.box()
        tb.present_without_persistent_viewplanes()
        tb.clear()

        # Get a keypress
        event = tbinst.poll_event()
        # untangle it's fields
        (type, ch, key, mod, w, h, x, y ) = event
        
        # Exit when escape pressed.
        if type==termbox.EVENT_KEY and key == tb.TB_KEY_ARROW_LEFT:
            newx = newx-1
        elif type==termbox.EVENT_KEY and key == tb.TB_KEY_ARROW_RIGHT:
            newx = newx+1
        elif type==termbox.EVENT_KEY and key == tb.TB_KEY_ARROW_UP:
            newy = newy-1
        elif type==termbox.EVENT_KEY and key == tb.TB_KEY_ARROW_DOWN:
            newy = newy+1
        elif type==termbox.EVENT_KEY and key == termbox.KEY_ESC:
            break
        
