import tkinter as tk

# 1. Initialize the root window
root = tk.Tk()
root.geometry("300x100")
root.title("Tkinter Checkbutton Example")

# 2. Create a variable to track the state (1 = Checked, 0 = Unchecked)
chk_var = tk.IntVar()

# 3. Create the Checkbutton and link it to the variable
chk = tk.Checkbutton(root, text="Option 1", variable=chk_var)

# 4. Pack the widget to make it visible
chk.pack(pady=20)

# 5. Start the application loop
root.mainloop()
