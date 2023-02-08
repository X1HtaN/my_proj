from tkinter import *
from datetime import datetime
import clock

class Clock:
    @staticmethod
    def btn_update():
        title.config(text=f"{clock.current_time()}")
        title.after(200, Clock.btn_update)


root = Tk()
root["bg"] = "#fafafa"
root.title("clock")
root.geometry("300x300")

root.resizable(width=False, height=False)

canvas = Canvas(root, width=300, height=300)
canvas.pack()

frame = Frame(root, bg="#fafafa")
frame.place(relheight=1, relwidth=1)

title = Label(frame, text="", font=140)
title.pack(expand = True)

Clock.btn_update()
root.mainloop()