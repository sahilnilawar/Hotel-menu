menu = {
    "pizza": 120,
    "burger": 30,
    "coffee": 10,
    "chowmein": 30,
    "maggie": 40,
    "dosa": 60,
}

print("Hello, sir!\nWhat help do you want?")
a = input("Type 'order' to place an order or 'list' to see the menu: ").lower()

def order():
    total_order = 0
    while True:
        b = input("What would you like to order?\n").lower()
        if b in menu:
            total_order += menu[b]
            print(f"{b} has been added to your list.")
        else:
            print("We don't have that item, sir.")

        c = input("Want anything else? (yes/no): ").lower()
        if c == 'no':
            break

    if total_order > 0:
        print(f"Your total bill is ₹{total_order}")
    else:
        print("You must buy something whenever you visit next time!")

if a == "order":
    order()

elif a == "list":
    print("\n--- ARISE RESTU MENU ---")
    for item, price in menu.items():
        print(f"{item.title()} - ₹{price}")

else:
    print("Sorry, invalid option!")
