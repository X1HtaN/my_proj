from tkinter import *
import handler as hd

class Output:
    @classmethod
    def check_format(cls, rub):
        if not isinstance(rub, (int, float)):
            title.config(text="в поле ввода не число")
        if entry.get().count(","):
            title.config(text="вместо | , | введите | . |")
    @staticmethod
    def btn_get():
        Output.check_format(entry.get())
        text_output = f"{hd.Converter.convert(entry.get())}"
        title.config(text=text_output)

root = Tk()
root["bg"] = "Black"
root.title("Conventer")
root.geometry("1600x400")

canvas = Canvas(root, width=900, height=400)
canvas.pack()
frame = Frame(root, bg="Black")
frame.place(relheight=1, relwidth=1)

entry = Entry(frame, width=10, font=("Arial", 30))
entry.pack(expand=True)

btn_convert = Button(frame, text="Convert", width=15, height=2, activeforeground="Black", command=Output.btn_get)
btn_convert.pack(expand=True)

title = Label(frame, text="введите кол-во рублей", font=("Arial", 20), fg="White", background="Black")
title.pack(expand=True)

root.mainloop()