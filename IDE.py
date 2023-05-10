from tkinter import *


def ideprint(text):
    global console
    console.insert(0, text)


def run_code():
    run_da_code = str(code.get())
    exec(run_da_code)


def clear():
    global console
    console.destroy()
    console = Entry(window)
    console.config(width=400, bg="black", fg="white", font=("Ariel", 25))
    console.place(x=0, y=100)


window = Tk()
window.title("Pyde")
window = Canvas(window, width=400, height=138)
window.pack()
code = Entry(window)
code.config(width=400, bg="black", fg="white", font=("Ariel", 25))
code.place(x=0, y=0)
console_text = Label(window, text="Console:", font=("Ariel", 25))
console_text.place(x=10, y=45)
console = Entry(window)
console.config(width=400, bg="black", fg="white", font=("Ariel", 25))
console.place(x=0, y=100)
run = Button(window, text="Run", command=run_code, bg="black", fg="white")
run.place(x=150, y=55)
clear = Button(window, text="Clear Console", command=clear, bg="black", fg="white")
clear.place(x=220, y=55)
window.mainloop()
