import tkinter as tk

# Function to update input field
def click(event_text):
    if event_text == "=" or event_text == "Return":  # Enter key
        try:
            result = str(eval(entry.get()))
            entry_var.set(result)
        except Exception:
            entry_var.set("Error")
    elif event_text == "C":
        entry_var.set("")
    elif event_text == "BackSpace":  # Delete last character
        entry_var.set(entry_var.get()[:-1])
    else:
        entry_var.set(entry_var.get() + event_text)

# Function to handle both button clicks and keyboard presses
def on_key(event):
    allowed_keys = "0123456789.+-*/"
    if event.keysym in allowed_keys:
        click(event.keysym)
    elif event.char in allowed_keys:
        click(event.char)
    elif event.keysym in ["Return", "BackSpace"]:
        click(event.keysym)

# Main window
root = tk.Tk()
root.title("Stylish Python Calculator")
root.geometry("360x500")
root.config(bg="#2b2b2b")
root.resizable(False, False)

entry_var = tk.StringVar()

# Entry field
entry = tk.Entry(root, textvar=entry_var, font=("Helvetica", 24), bd=0, bg="#1e1e1e", fg="white", justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=20, padx=10)

# Button frame
frame = tk.Frame(root, bg="#2b2b2b")
frame.pack(expand=True, fill="both")

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# Style buttons using grid for perfect alignment
for i, row in enumerate(buttons):
    for j, btn_text in enumerate(row):
        btn = tk.Button(
            frame, text=btn_text,
            font=("Helvetica", 20),
            bg="#3c3c3c" if btn_text not in ["=", "C"] else "#ff9500" if btn_text == "=" else "#ff3b30",
            fg="white",
            bd=0,
            relief="flat",
            activebackground="#5a5a5a",
            activeforeground="white"
        )
        btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
        btn.bind("<Button-1>", lambda e, text=btn_text: click(text))

# Add the "C" button spanning all columns
btn_clear = tk.Button(
    frame, text="C",
    font=("Helvetica", 20),
    bg="#ff3b30",
    fg="white",
    bd=0,
    relief="flat",
    activebackground="#5a5a5a",
    activeforeground="white"
)
btn_clear.grid(row=len(buttons), column=0, columnspan=4, sticky="nsew", padx=2, pady=2)
btn_clear.bind("<Button-1>", lambda e: click("C"))

# Make buttons expand equally
for i in range(len(buttons) + 1):  # +1 for "C" button row
    frame.rowconfigure(i, weight=1)
for j in range(4):
    frame.columnconfigure(j, weight=1)

# Bind keyboard events
root.bind("<Key>", on_key)

root.mainloop()
