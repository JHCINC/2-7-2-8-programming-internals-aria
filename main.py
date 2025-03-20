# A price comparison tool
import tkinter as tk

# Function for the best price for the budget

# A window for the GUI
window = tk.Tk()
window.geometry("500x400")
window.config(bg="white")
# So that the window stays the size I put it.
window.resizable(width=False, height=False)
window.title("Price Comparison")


# Function for the calculating of all the prices
def get_prices():
    price = int(entry_price.get())
    grams = int(entry_grams.get())
    div = price / grams

    tbox_unit_price.config(state="normal")

    # Insert the text into the text box
    tbox_unit_price.delete('1.0', tk.END)
    tbox_unit_price.insert(tk.END, div)
    tbox_unit_price.config(state='disabled')


# A label for the title of the program
title_heading = tk.Label(window, text="Price Comparison", font=("Arial", 13, "bold"), fg="black", bg="white")
# A label for the budget, wholesale price, and grams entry boxes
title_budget = tk.Label(window, text="Budget", font=("Arial", 10, "bold"), fg="black", bg="white")
title_price = tk.Label(window, text="Price", font=("Arial", 10, "bold"), fg="black", bg="white")
title_grams = tk.Label(window, text="Grams", font=("Arial", 10, "bold"), fg="black", bg="white")

# A entry box for the budget, wholesale price, and grams
entry_budget = tk.Entry(window, width=10)
entry_price = tk.Entry(window, width=10)
entry_grams = tk.Entry(window, width=10)

# Button to calculate the different prices
btn_calculate_prices = tk.Button(window, text="Calculate Unit Costs", font=("Arial", 13), command=get_prices)

# Text box that displays the unit costs
tbox_unit_price = tk.Text(window, width=5, height=0, state="disabled")

# Placing elements on screen
title_heading.place(x=180, y=10)
entry_budget.place(x=180, y=80)
title_budget.place(x=180, y=60)
entry_price.place(x=180, y=120)
title_price.place(x=180, y=100)
entry_grams.place(x=180, y=170)
title_grams.place(x=180, y=140)
btn_calculate_prices.place(x=160, y=200)
tbox_unit_price.place(x=180, y=230)

tk.mainloop()
