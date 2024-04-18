# main.py
import tkinter as tk
from main_window import MainMenu

if __name__ == "__main__":
    root = tk.Tk()
    main_menu = MainMenu(root)
    root.mainloop()
