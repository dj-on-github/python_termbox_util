#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# The termbox library for writing to the screen
import termbox

# termbox_util is a class that adds higher level drawing
# funtions. It can operate over a termbox window or a viewplane
# A viewplane is a virtual window with an interface very similar to
# termbox, so termbox_util can operate over it.

from termbox_util import termbox_util
from termbox_util import termbox_editableline

def el_validator(e):
    (type, ch, key, mod, w, h, x, y ) = e
    if type==termbox.EVENT_KEY and key == termbox.KEY_ENTER:
        return(7)
    else:
        return(ch)

# viewplane is a class that behaves like termbox but is virtual. 
# The window exists in memory and needs to be displayed in a real
# termbox to be seen.
# Viewplanes are useful for scrolling windows, configurable layouts
# and similar things.

from termbox_util import viewplane

# A virtual viewplane that can be displayed.    
vp=viewplane(11,5) 

# Get a set of utils to do things with it.
vptb = termbox_util(vp)  

# Use a real termbox window tbinst.   
with termbox.Termbox() as tbinst:
        event = "no_event"

        # Put something in the virtual viewplane
        vptb.addstr(3,2,"Hello")
        vptb.border()
        
        i=0
        # Get some utilities to run over the real window
        tb = termbox_util(tbinst)
        
        # This adds a persistent view of the virtual viewplane in the physical viewplane
        # With the _window version, it can be a view of only part of the viewplane
        # Parameters are : vp,width,height,srcx,srcy,viewx,viewy,active
        pid1 = tb.add_persistent_viewplane_window(vp,11,5,0,0,4,8)
        
        # This does the same in a different position. Without the _window suffix.
        # So it's the whole viewplane that will be displayed at x=14, y=15.
        pid2 = tb.add_persistent_viewplane(vp,4,15)

        el = termbox_editableline(tbinst,tb,2,2,10)
        
        #(keymap, eventmap) = tb.keymapper()
        
        while True:
            tb.clear()
            
            #Display some information
            (maxx,maxy) = tb.getmaxxy()
            tb.fill_area('x',28,8,33,10)
            
            #Put a box around the whole window
            tb.box()
            
            # Display some information in the window
            tb.addstr(4,5,"maxxy="+str(maxx)+","+str(maxy)+"  len vp.ch="+str(len(vp.chars[0])),bold=True)
            tb.addstr(4,6,str(event)+ "  i="+str(i))
            #if event in eventmap:
            #    tb.addstr(4,20,eventmap[event])
        
            #tb.draw_viewplane_window(vp,11,5,0,0,4,8)
            
            # Activate one or the other persistent viewplane
            # to be visible in the window.
            if (i%10)<3:
                tb.activate_persistent_vp(pid1)
                tb.deactivate_persistent_vp(pid2)
            else:
                tb.deactivate_persistent_vp(pid1)
                tb.activate_persistent_vp(pid2)
                
            if (i%10)>5:
                vptb.addstr(3,2,"Gbyee")
            else:
                vptb.addstr(3,2,"Hello")

            # Statically draw the viewplane in the window.
            tb.draw_viewplane(vp,25,15)

            # Drawing a filled rectangle directly into the window
            tb.fill_area(' ',16,8,24,19,fg=tb.fg,bg=tb.fg)
            tb.box(16,8,24,19)
            tb.present()
            i = i+1
            
            # Get a keypress
            event = tbinst.poll_event()
            # untangle it's fields
            (type, ch, key, mod, w, h, x, y ) = event
            
            # Go to an edit box if the user presses 'e'
            if type==termbox.EVENT_KEY and ch=='e':
                content=el.edit(el_validator,max_width=10)
 
            # Exit when escape pressed.
            if type==termbox.EVENT_KEY and key == termbox.KEY_ESC:
                break


