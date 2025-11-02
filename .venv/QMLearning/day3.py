import tkinter as tk
from operator import index
from tkinter import ttk, StringVar, BooleanVar
from tkinter import font
from tkinter import messagebox
import speech_recognition as sr
import pyaudio
import time
import pyttsx3



# voice engine creation
def speak(text):
    temp_engine = pyttsx3.init()
    temp_engine.setProperty('rate', 170)
    temp_engine.setProperty('volume', 1.0)
    voices = temp_engine.getProperty('voices')
    temp_engine.setProperty('voice', voices[141].id)
    temp_engine.say(text)
    temp_engine.runAndWait()
    del temp_engine

r = sr.Recognizer()

# voice input capture
def get_voice_input(prompt, valid_options=None):

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=1)
        max_attempts = 3
        attempts = 0
        speak(prompt)
        time.sleep(0.3)
        while attempts < max_attempts:
            audio = r.listen(source, timeout=10, phrase_time_limit=10)
            try:
                user_input = r.recognize_google(audio).lower().strip()
                print(f"DEBUG: Captured {user_input}, checking against {valid_options}")
                if valid_options is None or user_input in valid_options:
                    return user_input
                else:
                    speak("Sorry, that's not a valid option.")
            except sr.UnknownValueError:
                speak("I didn't catch that. Please try again.")

            attempts += 1
            if attempts < max_attempts:
                speak("Please try again.")
    return None

# price calculation
def calculate_price(coffe, size, addons):
    price = 0.0

    price = prices[menu.index(coffe)]

    if size == "large":
        price += 1.0
    elif size == "medium":
        price += 0.5
    else:
        price += 0.0

    if addons == "milk":
        price += 0.7
    elif addons == "sugar":
        price += 0.5
    elif addons == "both":
        price += 1.2
    else:
        price += 0.0

    return price


# ordering by speaking
def voice_order():
    print("\n=== Starting order ===")

    print("Step 1: Asking for coffee...")
    coffee_choice = get_voice_input("What would you like to order?", menu)
    print(f"Step 1 complete: {coffee_choice}")
    if coffee_choice is None:
        speak("Sorry, I couldn't get your coffee choice. Order cancelled.")
        print("Coffee choice failed, exiting")
        return
    time.sleep(0.5)

    print("\nStep 2: Asking for size...")
    size_choice = get_voice_input("Which size would you like?", availableSizes)
    print(f"Step 2 complete: {size_choice}")
    if size_choice is None:
        speak("Sorry, I couldn't get your size choice. Order cancelled.")
        print("Size choice failed, exiting")
        return
    time.sleep(0.5)

    print("\nStep 3: Asking for addons...")
    add_on_choice = get_voice_input("Would you prefer any add ons?", add_ons)
    print(f"Step 3 complete: {add_on_choice}")
    if add_on_choice is None:
        print("Addon choice failed, exiting")
        speak("Sorry, I couldn't get your addon choice. Order cancelled.")
        return
    time.sleep(0.5)

    price = calculate_price(coffee_choice, size_choice, add_on_choice)

    order = {
        'coffee': coffee_choice,
        'size': size_choice,
        'addons': add_on_choice,
        'price': price,
    }

    speak(f"Your order is {order['size']} {order['coffee']} with {order['addons']} the total price {order['price']:.2f}")
    print(f"Your order is: {order}")


# data
menu = ["espresso", "cappuccino", "latte", "americano"] # list
prices = (3.0, 4.5, 5.0, 3.5) # tuple
availableSizes = ["small", "medium", "large"] # list
add_ons = ["milk", "sugar", "both", "none"]

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

    # order_summary = ""
    # for key, value in order_info.items():
    #     order_summary += f"{key.capitalize()}: {value}\n"
    # order_summary += f"\nTotal amount: ${price:.2f}\n your coffe is in process"
    #
    # messagebox.showinfo("Order summary", order_summary)

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
root.geometry("380x350")

# Create labels
welcomeLabel = ttk.Label(root, text="Welcome to our Café", padding=5, font=("Arial Italic", 20))
welcomeLabel.pack()
labelMenu = ttk.Label(root, text="Today's menu", padding=5, font=("Arial Italic", 16))
labelMenu.pack()
labelMenu.pack()

coffee = StringVar()
menuFrame = ttk.Frame(root, width=300, height=300)
ttk.Combobox(menuFrame, values=menu, textvariable=coffee, state="readonly").grid(column=0, row=0)
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
orderButtonSpeakable = ttk.Button(orderFrame, text="Voice order", command=voice_order)
orderButton = ttk.Button(orderFrame, text="Order", command=process_order)
cancelButton = ttk.Button(orderFrame, text="Cancel", command=lambda: root.destroy())
orderButtonSpeakable.pack(side="top")
cancelButton.pack(side="left")
orderButton.pack(side="left")
orderFrame.pack()


root.mainloop()