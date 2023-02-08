from tkinter import *

root = Tk()
root["bg"] = "Black"
root.title("Timer")
root.geometry("800x800")

canvas = Canvas(root, width=800, height=800)
canvas.pack()
frame = Frame(root, bg="Gray")
frame.place(relheight=1, relwidth=1)

#ввод часов
entry_hours = Entry(frame, width=10, font=("Arial", 30))
entry_hours.grid(row=0, column=0)
#ввод минут
entry_minutes = Entry(frame, width=10, font=("Arial", 30))
entry_minutes.grid(row=0, column=1)
#ввод секунд
entry_seconds = Entry(frame, width=10, font=("Arial", 30))
entry_seconds.grid(row=0, column=2)


root.mainloop()