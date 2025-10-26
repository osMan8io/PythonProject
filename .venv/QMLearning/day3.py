import tkinter as tk
from tkinter import ttk, StringVar, BooleanVar
from tkinter import font
from tkinter import messagebox


# data
menu = ["Espresso", "Cappuccino", "Latte", "Americano"] # list
prices = (3.0, 4.5, 5.0, 3.5) # tuple
availableSizes = ["small", "medium", "large"] # set

# order setting
orders = [] # list


# Invoice function
def process_order():

    selected_coffee = coffee.get()
    selected_size = choice.get()
    selected_milk = milkVar.get()
    selected_suger = sugerVar.get()
    order = []

    # base restrictions
    if selected_coffee not in menu:
        messagebox.showerror("Error", "Please select a valid Coffee.")
        return
    if selected_size not in availableSizes:
        messagebox.showerror("Error", "Please select a valid Size.")
        return

    price = prices[menu.index(selected_coffee)]

    if selected_milk:
        price += 0.70
    if selected_suger:
        price += 0.50

    if selected_size == "medium":
        price += 0.70
    elif selected_size == "large":
        price += 1.0
    else:
        price += 0.0

    order_info = {}  # dictionary

    order_info = {
        "coffee": selected_coffee,
        "size": selected_size,
        "milk": selected_milk,
        "suger": selected_suger,
        "price": price,
    }


    # order popup
    popup = tk.Toplevel(root)
    popup.geometry("200x230")
    popup.title("Order Summary")

    ttk.Label(popup, text=f"Coffee: {order_info['coffee']}").pack(pady=5)
    ttk.Label(popup, text=f"Size: {order_info['size']}").pack(pady=5)
    ttk.Label(popup, text=f"Milk: {order_info['milk']}").pack(pady=5)
    ttk.Label(popup, text=f"Suger: {order_info['suger']}").pack(pady=5)
    ttk.Label(popup, text=f"Total Price: ${order_info['price']}").pack(pady=5)
    ttk.Label(popup, text="Your order will be ready...", font=("Arial Italic", 14)).pack(pady=5)

    ttk.Button(popup, text="OK", command=popup.destroy).pack(pady=10)

    orders.append(order)

# GUI begins
root = tk.Tk()
font.names()
root.title("Café Order App")
root.geometry("350x320")

# Create labels
welcomeLabel = ttk.Label(root, text="Welcome to our Café", padding=5, font=("Arial Italic", 20))
welcomeLabel.pack()
labelMenu = ttk.Label(root, text="Today's menu", padding=5, font=("Arial Italic", 16))
labelMenu.pack()
labelMenu.pack()

coffee = StringVar()
menuFrame = ttk.Frame(root, width=300, height=300)
ttk.Combobox(menuFrame, values=menu, textvariable=coffee,state="readonly").grid(column=0, row=0)
menuFrame.pack()

# choosing available size
choice = StringVar()
sizeFrame = ttk.LabelFrame(root, padding=10, relief="ridge")
labelSize = ttk.Label(sizeFrame, text="Select Size", padding=2, font=("Arial Italic", 14))
small = ttk.Radiobutton(sizeFrame, text="Small", variable=choice, value="small")
medium = ttk.Radiobutton(sizeFrame, text="Medium", variable=choice, value="medium")
large = ttk.Radiobutton(sizeFrame, text="Large", variable=choice, value="large")
labelSize.pack(side="top")
small.pack(side="left")
medium.pack(side="left")
large.pack(side="left")
sizeFrame.pack()


# Create buttons & add-ons
milkVar = BooleanVar()
milkCheck = ttk.Checkbutton(root, text="Add Milk", variable=milkVar, padding=5)
milkCheck.pack()
sugerVar = BooleanVar()
sugerCheck = ttk.Checkbutton(root, text="Add Suger", variable=sugerVar, padding=5)
sugerCheck.pack()

# order & cancel buttons
orderFrame = ttk.LabelFrame(root, padding=5, relief="ridge")
orderButton = ttk.Button(orderFrame, text="Order", command=process_order)
cancelButton = ttk.Button(orderFrame, text="Cancel", command=lambda: root.destroy())
cancelButton.pack(side="left")
orderButton.pack(side="left")
orderFrame.pack()


root.mainloop()