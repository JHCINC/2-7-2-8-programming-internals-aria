# A price comparison tool
import tkinter as tk

global price, grams, budget, unit_price, product, name

# An empty list that amends as the user enters the different product info
list_product = []
# affordable_products = []

# Function that compares the items in the list
def get_unit_price(product):
    return product["unit_price"]


# Function which shows which is best for the budget
def best_budget():
    affordable_products = []
    budget = float(entry_budget.get())
    for product in list_product:
        if product["price"] <= budget:
            affordable_products.append(product)
            # print("aff",affordable_products)
    if not affordable_products:
        tbox_best_budget.config(state='normal')  # Make sure it's editable
        tbox_best_budget.delete('1.0', tk.END)
        tbox_best_budget.insert(tk.END, "No products found")
        tbox_best_budget.config(state='disabled')
        return

# Then it compares each product that is in the budget unit price to find the lowest one
    # print("aff 1_product", affordable_products[0])
    best_product = affordable_products[0]
    # print("best_product", best_product)
    for product in affordable_products:
        # print("affordable")
        if product["unit_price"] <= best_product["unit_price"]:
            # print("best", best_product)
            best_product = product
            print("best")
    product_info = f"Name: {best_product['name']}, Price: {best_product['price']}"
    tbox_best_budget.config(state='normal')
    tbox_best_budget.delete('1.0', tk.END)
    tbox_best_budget.insert(tk.END, product_info)
    tbox_best_budget.config(state='disabled')



# Function that compares to the budget
def compare_budget():
    budget = float(entry_budget.get())
    for product in list_product:
        print("product", product)
        price = product["price"]
        grams = product["grams"]
        unit_price = product["unit_price"]
        name = product["name"]
    if price <= budget:
        print("This product is within your budget!")
    else:
        print("This product is not within your budget.")


# Function that adds items to the list
def add_item():
    # Get the entry info
    price = float(entry_price.get())
    print(price)
    grams = float(entry_grams.get())
    unit_price = price / grams
    name = entry_name.get()

    list_product.append({
        "price": price,
        "grams": grams,
        "unit_price": unit_price,
        "name": name,
    })

    # Clear the entry boxes so more products can be added
    entry_price.delete(0, tk.END)
    entry_grams.delete(0, tk.END)
    entry_name.delete(0, tk.END)

# Function for the calculating of all the prices
def get_prices():
    price = float(entry_price.get())
    grams = float(entry_grams.get())
    unit_price = price / grams
    name = entry_name.get()

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
title_name = tk.Label(window, text="Name of Product", font=("Arial", 10, "bold"), fg="black", bg="white")

# A entry box for the budget, wholesale price, and grams
entry_budget = tk.Entry(window, width=10)
entry_price = tk.Entry(window, width=10)
entry_grams = tk.Entry(window, width=10)
entry_name = tk.Entry(window, width=20)

# Button to calculate the different prices
btn_calculate_prices = tk.Button(window, text="Calculate Unit Costs", font=("Arial", 13), command=get_prices)

# Text box that displays the unit costs
tbox_unit_price = tk.Text(window, width=5, height=0, state="disabled")

# Text box for the best  price for budget
tbox_best_budget = tk.Text(window, width=23, height=0, state="disabled")

# A button that adds a product to the list
btn_add_product = tk.Button(window, text="Add product", font=("Arial", 13), command=add_item)

# Button that compares to the budget
btn_compare_budget = tk.Button(window, text="See which products fit your budget.", font=("Arial", 13),
                               command=compare_budget)

btn_best_budget = tk.Button(window, text="Best for budget.", font=("Arial", 13,), command=best_budget)

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
btn_compare_budget.place(x=180, y=340)
tbox_best_budget.place(x=20, y=340)
btn_best_budget.place(x=50, y=300)
entry_name.place(x=180, y=40)
title_name.place(x=50, y=40)

tk.mainloop()
