"""A price comparison tool."""
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
FIRST = 0
MAX = 3000
MIN = 0
BACKGROUND_BLUE = '#d8e2dc'
BUTTON_COLOUR = '#a9def9'


global price, amount, budget, unit_price, product, name, results, unit

# An empty list that amends as the user enters the different product info
list_product = []


def best_budget():
    """Function which shows which is best for the budget."""
    try:
        affordable_products = []
        budget = float(entry_budget.get())
        for product in list_product:
            if product["price"] <= budget:
                affordable_products.append(product)
        if not affordable_products:
            tbox_best_budget.config(state='normal')  # Make sure it's editable
            tbox_best_budget.delete('1.0', tk.END)
            tbox_best_budget.insert(tk.END, "No products found")
            tbox_best_budget.config(state='disabled')
            return

    # Then it compares each product that is in the budget unit price to find the lowest one

        best_product = affordable_products[FIRST]
        # print("best_product", best_product)
        for product in affordable_products:
            # print("affordable")
            if product["unit_price"] <= best_product["unit_price"]:
                # print("best", best_product)
                best_product = product
        product_info = f"Name: {str(best_product['name'])}, Price: {best_product['price']}"
        tbox_best_budget.config(state='normal')
        tbox_best_budget.delete('1.0', tk.END)
        tbox_best_budget.insert(tk.END, product_info)
        tbox_best_budget.config(state='disabled')
    except ValueError:  messagebox.showinfo("Error", "Please enter values into all of the entry boxes!")


def compare_budget():
    """Function that compares to the budget."""
    try:
        budget = float(entry_budget.get())
        tbox_compare_budget.config(state='normal')
        tbox_compare_budget.delete('1.0', tk.END)

        results = ""

        for product in list_product:
            print("product", product)
            price = product["price"]
            amount = product["amount"]
            unit_price = product["unit_price"]
            name = product["name"]
            if price <= budget:
                results += f"{name}: This product is in your budget!\n"
            else:
                results += f"{name}: This product is not in your budget.\n"
            print(f"Results: {results}")
        tbox_compare_budget.insert(tk.END, results)
        tbox_compare_budget.config(state='disabled')
    except ValueError:
        messagebox.showinfo("Error", "Please enter values into all of the entry boxes!")


def add_item():
    """Function that adds items to the list."""
    # Check if there are empty boxes
    if not entry_price.get() or not entry_grams.get() or not entry_name.get():
        messagebox.showinfo("Error", "Please enter values into all of the entry boxes!")
        return

    # Get the entry info
    try:
        price = float(entry_price.get())
        amount = float(entry_grams.get())
        unit_price = price / amount
        name = str(entry_name.get())
        list_product.append({
            "price": price,
            "amount": amount,
            "unit_price": unit_price,
            "name": name,
        })
        status_label.config(text=f"Product ' {name} ' added successfully!")

    except ValueError:
        messagebox.show_info("Error", "Please enter NUMBERS into the price and amount boxes!")

    # Clear the entry boxes so more products can be added
    entry_price.delete(FIRST, tk.END)
    entry_grams.delete(FIRST, tk.END)
    entry_name.delete(FIRST, tk.END)


def get_prices():
    """Function for the calculating of all the prices."""
    try:
        price = float(entry_price.get())
        amount = float(entry_grams.get())
        unit = dropdown_unit.get()
        if amount <= MIN or price <= MIN:
            messagebox.showerror("Error", "Please enter a number above 0!")
        elif amount > MAX or price > MAX:
            messagebox.showerror("Error", "Sorry, we cannot calculate numbers above 3000!")
            return

        unit_price = price / amount
        name = entry_name.get()

        unit_symbol = ""
        if unit == "Grams":
            unit_symbol = 'g'
        else:
            unit_symbol = 'L'


        tbox_unit_price.config(state="normal")

    # Insert the text into the text box
        tbox_unit_price.delete('1.0', tk.END)
        tbox_unit_price.insert('1.0', str(unit_price) + unit_symbol)
        tbox_unit_price.config(state='disabled')
    except ValueError:
        messagebox.showerror("Error", "Please enter NUMBERS!")


# A window for the GUI
window = tk.Tk()
window.geometry("600x500")
window.config(bg=BACKGROUND_BLUE)
# So that the window stays the size I put it.
window.resizable(width=False, height=False)
window.title("Price Comparison")


# A label for the title of the program
title_heading = tk.Label(window, text="Price Comparison", font=("Arial", 20, "bold"), fg="black", bg='#d8e2dc')
# A label for the budget, wholesale price, and grams entry boxes
title_budget = tk.Label(window, text="Budget ($)", font=("Arial", 13, "bold"), fg="black", bg="white")
title_price = tk.Label(window, text="Price ($)", font=("Arial", 13, "bold"), fg="black", bg="white")
title_amount = tk.Label(window, text="Amount", font=("Arial", 13, "bold"), fg="black", bg="white")
title_name = tk.Label(window, text="Name of Product", font=("Arial", 13, "bold"), fg="black", bg="white")

# A entry box for the budget, wholesale price, and grams
entry_budget = tk.Entry(window, width=10)
entry_price = tk.Entry(window, width=10)
entry_grams = tk.Entry(window, width=10)
entry_name = tk.Entry(window, width=20)

# Button to calculate the different prices
btn_calculate_prices = tk.Button(window, text="Calculate Unit Costs", font=("Arial", 13), command=get_prices,
                                 bg=BUTTON_COLOUR)

# Drop down box
unit_options = ["Grams", "Liters"]
dropdown_unit = ttk.Combobox(window, values=unit_options, width=10, height=10, state="readonly")
dropdown_unit.current(FIRST)

# Text box that displays the unit costs
tbox_unit_price = tk.Text(window, width=5, height=0, state="disabled")

# Text box for the best  price for budget
tbox_best_budget = tk.Text(window, width=23, height=0, state="disabled")

# Text box for if it fits the budget
tbox_compare_budget = tk.Text(window, width=25, height=5, state="disabled")

# Exit button
btn_exit = tk.Button(window, width=5, height=0, text="Exit", font=("Arial", 13), command=exit, fg='red', bg='white')

# Unit label
title_unit = tk.Label(window, text="Choose unit", font=("Arial", 10, "bold"), fg="black", bg="white")

# A status label that says when the product has been added
status_label = tk.Label(window, text="", font=("Arial", 10), fg="green", bg=BACKGROUND_BLUE)

# Line to seperate input and output


# A button that adds a product to the list
btn_add_product = tk.Button(window, text="Add product", font=("Arial", 13), command=add_item, bg=BUTTON_COLOUR)

# Button that compares to the budget
btn_compare_budget = tk.Button(window, text="See which products fit your budget.", font=("Arial", 13),
                               command=compare_budget, bg=BUTTON_COLOUR)

btn_best_budget = tk.Button(window, text="Best for budget.", font=("Arial", 13,), command=best_budget, bg=BUTTON_COLOUR)

separator = ttk.Separator(window, orient='horizontal')


# Placing elements on screen
title_heading.place(x=160, y=5)
entry_budget.place(x=210, y=80)
title_budget.place(x=60, y=80)
entry_price.place(x=210, y=120)
title_price.place(x=60, y=120)
entry_grams.place(x=210, y=170)
dropdown_unit.place(x=290, y=170)
btn_calculate_prices.place(x=190, y=200)
tbox_unit_price.place(x=210, y=240)
btn_add_product.place(x=50, y=230)
btn_compare_budget.place(x=320, y=310)
tbox_best_budget.place(x=20, y=350)
btn_best_budget.place(x=50, y=310)
entry_name.place(x=210, y=40)
title_name.place(x=50, y=40)
tbox_compare_budget.place(x=350, y=360)
btn_exit.place(x=10, y=450)
title_amount.place(x=65, y=170)
status_label.place(x=340, y=40)
separator.place(x=10, y=270, width=580, height=2)


tk.mainloop()
