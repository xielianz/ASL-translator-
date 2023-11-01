from tkinter import (PhotoImage, Frame, Label, Text, Entry, X, Y, BOTH, BOTTOM, TOP, LEFT, RIGHT, DISABLED, NORMAL, END, Tk)
import os
import random
from random import choice

class ASL:

    def __init__(self, name: str, image_filepath: str):
        self.name = name
        self.image = image_filepath

class GAME(Frame):
    STATUS_RIGHT_ANSWER = "CORRECT!"
    STATUS_WRONG_ANSWER = "Try Again"
    STATUS_DEFAULT = "Too long."
    EXIT_GAME = ["quit"]

    WIDTH = 800
    HEIGHT = 700

    def __init__(self, parent: Tk):
        Frame.__init__(self, parent)
        self.pack(fill=BOTH, expand=1)
        self.font_size = 20
    
    def setting_up_gui(self):
        self.player_input = Entry(self, bg="black", fg="lightgreen", font=('Helvetica', self.font_size))
        self.player_input.bind("<Return>", self.process_input)
        self.player_input.pack(side=BOTTOM, fill=X)
        self.player_input.focus()

        img = None
        img_width = GAME.WIDTH
        img_height = GAME.HEIGHT
        self.image_container = Label(self, width = img_width, height = img_height, image = img, bg="black")

        self.image_container.image = img
        self.image_container.pack(side=TOP, fill=Y)
        self.image_container.pack_propagate(False)

        text_container_width = GAME.WIDTH // 2
        text_container = Frame(self, width=text_container_width)

        self.text = Text(text_container, bg="black", fg="white", state=DISABLED)
        self.text.pack(fill=BOTH, expand=1)

        text_container.pack(side=RIGHT, fill=Y)
        text_container.pack_propagate(False)

    def change_font_size(self, new_size):
        self.font_size = new_size
        self.player_input.config(font=('Comic Sans', self.font_size))

    def setting_up_game(self):

        a = ASL("A", os.path.join("new_pics","a.png"))
        b = ASL("B", os.path.join("new_pics","b.png"))
        c = ASL("C", os.path.join("new_pics","c.png"))
        d = ASL("D", os.path.join("new_pics","d.png"))
        e = ASL("E", os.path.join("new_pics","e.png"))
        f = ASL("F", os.path.join("new_pics","f.png"))
        g = ASL("G", os.path.join("new_pics","g.png"))
        h = ASL("H", os.path.join("new_pics","h.png"))
        i = ASL("I", os.path.join("new_pics","i.png"))
        j = ASL("J", os.path.join("new_pics","j.png"))
        k = ASL("K", os.path.join("new_pics","k.png"))
        l = ASL("L", os.path.join("new_pics","l.png"))
        m = ASL("M", os.path.join("new_pics","m.png"))
        n = ASL("N", os.path.join("new_pics","n.png"))
        o = ASL("O", os.path.join("new_pics","o.png"))
        p = ASL("P", os.path.join("new_pics","p.png"))
        q = ASL("Q", os.path.join("new_pics","q.png"))
        r = ASL("R", os.path.join("new_pics","r.png"))
        s = ASL("S", os.path.join("new_pics","s.png"))
        t = ASL("T", os.path.join("new_pics","t.png"))
        u = ASL("U", os.path.join("new_pics","u.png"))
        v = ASL("V", os.path.join("new_pics","v.png"))
        w = ASL("W", os.path.join("new_pics","w.png"))
        x = ASL("X", os.path.join("new_pics","x.png"))
        y = ASL("Y", os.path.join("new_pics","y.png"))
        z = ASL("Z", os.path.join("new_pics","z.png"))

        letters = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]

        self.current_pic = random.choice(letters)


    def set_status(self, status, text_widget):
        text_widget.config(state=NORMAL)
        text_widget.delete(1.0,END)
        text_widget.insert(END,status)
        text_widget.config(state=DISABLED)

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
        self.set_status(GAME.STATUS_DEFAULT, self.text_widget)
        self.clear_entry()

    def play(self):
        self.setting_up_gui()
        self.setting_up_game()
        self.set_images()
        self.text_widget = self.text
        self.set_status("", self.text_widget)

        self.player_input.bind("<Return>", self.process_input)

    def process_input(self, event):
        user_answer = self.player_input.get().upper()

        if user_answer == self.current_pic.name:
            self.set_status(GAME.STATUS_RIGHT_ANSWER, self.text_widget)
            self.clear_entry()

            self.setting_up_game()
            self.set_images()
            self.set_status("", self.text_widget)

        else:
            self.set_status(GAME.STATUS_WRONG_ANSWER, self.text_widget)

        action = self.player_input.get()
        action = action.lower()

        if action in GAME.EXIT_GAME:
            exit()

        words = action.split()

        if len(words) != 1:
            self.handle_default()
            return

        self.clear_entry()







window = Tk()
window.title("ASL learning game")
game = GAME(window)
game.play()
window.mainloop()



