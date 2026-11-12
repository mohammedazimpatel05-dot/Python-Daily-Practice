import tkinter as tk

root = tk.Tk()
root.title("Tkinter Canvas Example")

canvas = tk.Canvas(root, width=400, height=300, bg="white")
canvas.pack()

# Draw shapes
canvas.create_rectangle(50, 50, 150, 120, fill="blue", outline="black")
canvas.create_oval(200, 50, 300, 150, fill="red")
canvas.create_line(0, 0, 400, 300, fill="green", width=2)
canvas.create_text(200, 220, text="Hello Tkinter Canvas!", font=("Arial", 14))

root.mainloop()
