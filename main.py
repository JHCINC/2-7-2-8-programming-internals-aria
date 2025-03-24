# A price comparison tool
import tkinter as tk

global price, grams, budget, unit_price

# An empty list that amends as the user enters the different product info
list_product = []

# Function that compares the items in the list

# Function that compares to the budget

# Function that adds items to the list
def add_item():
    # Get the entry info
    price = float(entry_price.get())
    grams = float(entry_grams.get())
    unit_price = price / grams

    list_product.append({
        "price": price,
        "grams": grams,
        "unit_price": unit_price
    })

    # Clear the entry boxes so more products can be added
    entry_price.delete(0, tk.END)
    entry_grams.delete(0, tk.END)

# Function for the calculating of all the prices
def get_prices():
    price = float(entry_price.get())
    grams = float(entry_grams.get())
    unit_price = price / grams

    tbox_unit_price.config(state="normal")

    # Insert the text into the text box
    tbox_unit_price.delete('1.0', tk.END)
    tbox_unit_price.insert(tk.END, unit_price)
    tbox_unit_price.config(state='disabled')


# A window for the GUI
window = tk.Tk()
window.geometry("500x400")
window.config(bg="white")
# So that the window stays the size I put it.
window.resizable(width=False, height=False)
window.title("Price Comparison")


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

# A button that adds a product to the list
btn_add_product = tk.Button(window, text="Add product", font=("Arial", 13), command=add_item)

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
btn_add_product.place(x=180, y=300)

tk.mainloop()
