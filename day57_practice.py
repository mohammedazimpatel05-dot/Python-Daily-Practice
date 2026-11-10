import tkinter as tk

def open_file():
    print("Open clicked!")

root = tk.Tk()
root.title("Tkinter Menu Example")
root.geometry("300x200")

# Create the main menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create File dropdown menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open...", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Create Help dropdown menu
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=lambda: print("Tkinter Menu Demo"))

root.mainloop()
