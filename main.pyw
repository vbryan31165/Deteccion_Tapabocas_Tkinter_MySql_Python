
from tkinter import *
from inicio_Session import *


def main():
    root = Tk()
    root.wm_title("Crud Python MySQL")
    app = Login(root)
    app.mainloop()


if __name__ == "__main__":
    main()
