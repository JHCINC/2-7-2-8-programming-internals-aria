# A price comparison tool
import tkinter as tk

# A window for the GUI
window = tk.Tk()
window.geometry("500x400")
window.config(bg="white")
window.resizable(width=False, height=False) # So that the window stays the size I put it.
window.title("Price Comparison")

# A label for the title of the program
title_heading = tk.Label(window, text="Price Comparison", font=("Arial", 13, "bold"), fg="black", bg="white")

# Placing elements on screen
title_heading.place(x=180, y=10)

tk.mainloop()
