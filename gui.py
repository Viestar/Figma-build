# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(
    r"C:\Users\DELL\OneDrive\Documents\Silcodes\PycharmProjects\UltimateHoldingsLimited\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


sign = ''
ans = 0


def add():
    global sign
    sign = "+"


def sub():
    global sign
    sign = "-"


def multiply():
    global sign
    sign = "x"


def divide():
    global sign
    sign = "/"


def evaluate():
    try:
        global sign, ans
        num = int(entry_3.get())
        num_2 = int(entry_2.get())
        if sign == "+":
            ans = num + num_2
        elif sign == "-":
            ans = num - num_2
        elif sign == "x":
            ans = num * num_2
        elif sign == "/":
            ans = num / num_2
        label["text"] = ans

    except:
        msg = "Only Numbers"
        label["text"] = msg


window = Tk()

window.geometry("412x223")
window.configure(bg="#D9D9D9")

canvas = Canvas(
    window,
    bg="#D9D9D9",
    height=223,
    width=412,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    102.0,
    107.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    324.99999237060547,
    138.0,
    image=image_image_2
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    260.0,
    190.5,
    image=entry_image_1
)
label = Label(
    text="Answer",
    bd=0,
    bg="#FFFDF5",
    fg="#000716",
    highlightthickness=0
)
label.place(
    x=218.0,
    y=171.0,
    width=84.0,
    height=37.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    306.5,
    146.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#FFFDF5",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=224.0,
    y=130.0,
    width=165.0,
    height=31.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    306.5,
    65.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#FFFDF5",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=224.0,
    y=49.0,
    width=165.0,
    height=31.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=evaluate,
    relief="flat"
)
button_1.place(
    x=318.3155212402344,
    y=167.0,
    width=75.68447875976562,
    height=47.43849182128906
)

canvas.create_text(
    205.0,
    4.0,
    anchor="nw",
    text="Puppy’s Calculate",
    fill="#820D85",
    font=("Inter SemiBold", 20 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=add,
    relief="flat"
)
button_2.place(
    x=218.0,
    y=89.69033813476562,
    width=41.18712615966797,
    height=45.43849182128906
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=sub,
    relief="flat"
)
button_3.place(
    x=263.0,
    y=90.10321807861328,
    width=39.0,
    height=43.025604248046875
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=divide,
    relief="flat"
)
button_4.place(
    x=308.0,
    y=88.0,
    width=40.0,
    height=44.12882995605469
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=multiply,
    relief="flat"
)
button_5.place(
    x=354.0,
    y=88.69033813476562,
    width=40.0,
    height=44.12882995605469
)
window.resizable(False, False)
window.mainloop()
