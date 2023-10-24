from tkinter import (PhotoImage, Frame, Label, Text, Entry, X, Y, BOTH, BOTTOM, TOP, LEFT, RIGHT, DISABLED, NORMAL, END, Tk)
import os
import random
from asl import ASL
from random import choice

class GAME(Frame):
    STATUS_RIGHT_ANSWER = "CORRECT!"
    STATUS_WRONG_ANSWER = "Try Again"
    STATUS_DEFAULT = "Not a word."
    EXIT_GAME = ["quit"]

    WIDTH = 800
    HEIGHT = 600

    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=1)
    
    def setting_up_gui(self):
        self.player_input = Entry(self)
        self.player_input.bind("<Return>", self.process_input)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()

        img = None
        img_width = GAME.WIDTH
        self.image_container = Label(self, width = img_width, image = img)

        self.image_container.image = img
        self.image_container.pack(side=TOP, fill=Y)
        self.image_container.pack_propagate(False)

        text_container_width = GAME.WIDTH
        text_container = Frame(self, width=text_container_width)

        self.text = Text(text_container, state=DISABLED)
        self.text.pack(fill=Y, expand=1)

        text_container.pack(side=BOTTOM, fill=Y)
        text_container.pack_propagate(False)

    def setting_up_game(self):

        a = ASL("A", os.path.join("ASL_images","a.gif"))
        b = ASL("B", os.path.join("ASL_images","b.gif"))
        c = ASL("C", os.path.join("ASL_images","c.gif"))
        d = ASL("D", os.path.join("ASL_images","d.gif"))
        e = ASL("E", os.path.join("ASL_images","e.gif"))
        f = ASL("F", os.path.join("ASL_images","f.gif"))
        g = ASL("G", os.path.join("ASL_images","g.gif"))
        h = ASL("H", os.path.join("ASL_images","h.gif"))
        i = ASL("I", os.path.join("ASL_images","i.gif"))
        j = ASL("J", os.path.join("ASL_images","j.gif"))
        k = ASL("K", os.path.join("ASL_images","k.gif"))
        l = ASL("L", os.path.join("ASL_images","l.gif"))
        m = ASL("M", os.path.join("ASL_images","m.gif"))
        n = ASL("N", os.path.join("ASL_images","n.gif"))
        o = ASL("O", os.path.join("ASL_images","o.gif"))
        p = ASL("P", os.path.join("ASL_images","p.gif"))
        q = ASL("Q", os.path.join("ASL_images","q.gif"))
        r = ASL("R", os.path.join("ASL_images","r.gif"))
        s = ASL("S", os.path.join("ASL_images","s.gif"))
        t = ASL("T", os.path.join("ASL_images","t.gif"))
        u = ASL("U", os.path.join("ASL_images","u.gif"))
        v = ASL("V", os.path.join("ASL_images","v.gif"))
        w = ASL("W", os.path.join("ASL_images","w.gif"))
        x = ASL("X", os.path.join("ASL_images","x.gif"))
        y = ASL("Y", os.path.join("ASL_images","y.gif"))
        z = ASL("Z", os.path.join("ASL_images","z.gif"))

        letters = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

        self.current_pic = a

    def set_status(self, status):
        self.text.config(state=NORMAL)
        self.text.delete(1.0, END) 

        self.text.config(state=DISABLED)

    def set_images(self):
        img = PhotoImage(file = self.current_pic.image)

        self.image_container.config(image=img)
        self.image_container.image = img 

    def clear_entry(self):
        self.player_input.delete(0, END)

    def handle_default(self):
        self.set_status(GAME.STATUS_DEFAULT)
        self.clear_entry()

    def play(self):
        self.setting_up_gui()
        self.setting_up_game()
        self.set_images()
        self.set_status("")

    def process_input(self, event):
        action = self.player_input.get()
        action = action.lower()

        if action in GAME.EXIT_GAME:
            exit()

        words = action.split()

        if len(words) != 1:
            self.handle_default()
            return 
        
        self.clear_entry()


