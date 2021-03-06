from email import message
from tkinter import *
from tkinter import messagebox
from matplotlib.font_manager import win32FontDirectory
from matplotlib.pyplot import text

from sqlalchemy import true

root = Tk()
root.title('Tic-Tac-Toe Game Developed by Swarup 😎')

clicked = True
count = 0


def disable_button():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def checkwhowon():
    global winner
    winner = False
    # Check for X
    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="lime")
        b2.config(bg="lime")
        b3.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo X, Win!!!")
        disable_button()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="lime")
        b5.config(bg="lime")
        b6.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo X, Win!!!")
        disable_button()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="lime")
        b8.config(bg="lime")
        b9.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo X, Win!!!")
        disable_button()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="lime")
        b4.config(bg="lime")
        b7.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo X, Win!!!")
        disable_button()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="lime")
        b5.config(bg="lime")
        b8.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo X, Win!!!")
        disable_button()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="lime")
        b6.config(bg="lime")
        b9.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo X, Win!!!")
        disable_button()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="lime")
        b5.config(bg="lime")
        b9.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo X, Win!!!")
        disable_button()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="lime")
        b5.config(bg="lime")
        b7.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo X, Win!!!")
        disable_button()
        # Check for O
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="lime")
        b2.config(bg="lime")
        b3.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo O, Win!!!")
        disable_button()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="lime")
        b5.config(bg="lime")
        b6.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo O, Win!!!")
        disable_button()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="lime")
        b8.config(bg="lime")
        b9.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo O, Win!!!")
        disable_button()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="lime")
        b4.config(bg="lime")
        b7.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo O, Win!!!")
        disable_button()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="lime")
        b5.config(bg="lime")
        b8.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo O, Win!!!")
        disable_button()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="lime")
        b6.config(bg="lime")
        b9.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo O, Win!!!")
        disable_button()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="lime")
        b5.config(bg="lime")
        b9.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo O, Win!!!")
        disable_button()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="lime")
        b5.config(bg="lime")
        b7.config(bg="lime")
        winner = True
        messagebox.showinfo("Swarup's Tic Tac Toe", "Congo O, Win!!!")
        disable_button()


def b_click(b):
    global clicked, count
    if b["text"] == " " and clicked == True:
        b["text"] = "X"
        clicked = False
        count += 1
        checkwhowon()
    elif b["text"] == " " and clicked == False:
        b["text"] = "O"
        clicked = True
        count += 1
        checkwhowon()
    else:
        messagebox.showerror("Swarup's Tic Tac Toe", "Hey it is already selected pick another one")


b1 = Button(root, text=" ", font=("Helvertica", 20), height=3,
            width=6, bg="SystemButtonFace", command=lambda: b_click(b1))
b2 = Button(root, text=" ", font=("Helvertica", 20), height=3,
            width=6, bg="SystemButtonFace", command=lambda: b_click(b2))
b3 = Button(root, text=" ", font=("Helvertica", 20), height=3,
            width=6, bg="SystemButtonFace", command=lambda: b_click(b3))

b4 = Button(root, text=" ", font=("Helvertica", 20), height=3,
            width=6, bg="SystemButtonFace", command=lambda: b_click(b4))
b5 = Button(root, text=" ", font=("Helvertica", 20), height=3,
            width=6, bg="SystemButtonFace", command=lambda: b_click(b5))
b6 = Button(root, text=" ", font=("Helvertica", 20), height=3,
            width=6, bg="SystemButtonFace", command=lambda: b_click(b6))

b7 = Button(root, text=" ", font=("Helvertica", 20), height=3,
            width=6, bg="SystemButtonFace", command=lambda: b_click(b7))
b8 = Button(root, text=" ", font=("Helvertica", 20), height=3,
            width=6, bg="SystemButtonFace", command=lambda: b_click(b8))
b9 = Button(root, text=" ", font=("Helvertica", 20), height=3,
            width=6, bg="SystemButtonFace", command=lambda: b_click(b9))

b1.grid(row=0, column=0)
b2.grid(row=0, column=1)
b3.grid(row=0, column=2)

b4.grid(row=1, column=0)
b5.grid(row=1, column=1)
b6.grid(row=1, column=2)

b7.grid(row=2, column=0)
b8.grid(row=2, column=1)
b9.grid(row=2, column=2)


root.mainloop()