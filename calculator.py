import tkinter as tk

# Function to handle button clicks
def button_pressed(event):
    btn_value = event.widget.cget("text")
    
    if btn_value == "=":
        try:
            calculation = eval(display_var.get())
            display_var.set(calculation)
        except Exception:
            display_var.set("Error")
    elif btn_value == "C":
        display_var.set("")
    else:
        display_var.set(display_var.get() + btn_value)

# Initialize main window
app = tk.Tk()
app.title("Simple Calculator")
app.geometry("320x420")

# Input field
display_var = tk.StringVar()
display_entry = tk.Entry(app, textvariable=display_var, font=("Arial", 20), bd=8, relief=tk.SUNKEN, justify="right")
display_entry.pack(fill=tk.BOTH, padx=10, pady=10, ipadx=8, ipady=10)

# Define button layout
button_values = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

# Frame to hold buttons
button_frame = tk.Frame(app)
button_frame.pack()

# Generate buttons dynamically
for row in button_values:
    row_frame = tk.Frame(button_frame)
    row_frame.pack()
    for value in row:
        btn = tk.Button(row_frame, text=value, font=("Arial", 18), width=5, height=2)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", button_pressed)

# Run the application
app.mainloop()
