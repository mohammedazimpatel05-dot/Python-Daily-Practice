import tkinter as tk

# 1. Initialize the main window (added missing '=' sign)
root = tk.Tk()

# 2. Define a function to run when the button is clicked
def on_click():
    print("Button was clicked!")

# 3. Create the button widget and link it to the function
btn = tk.Button(root, text="Click", command=on_click)

# 4. Position the button inside the window so it becomes visible
btn.pack(pady=20)

# 5. Start the Tkinter event loop to keep the window open
root.mainloop()
