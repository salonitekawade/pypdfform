import tkinter as tk

def update_value(value):
    global selected_value
    selected_value = value

root = tk.Tk()

selected_value = 0  # Initial value

radio_button1 = tk.Radiobutton(root, text="Option 1", value=1, command=lambda: update_value(1))
radio_button2 = tk.Radiobutton(root, text="Option 2", value=2, command=lambda: update_value(2))

# ... (rest of your GUI code)

root.mainloop()