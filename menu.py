# Menu dictionary
menu = {
    "Antipasti": {
        "Truffled Agave & Goat Cheese Bruschetta ": .99,
        "Arancini": .69,
        "Pane Romano": .49,
        "Truffle Gnocchi Bites": 1.99
    },
    "Meals": {
        "Ahi Tuna": 4.49,
        "Tortellone": 9.99,
        "Baked Eggplant Parm": 7.49,
        "Linguini & Meatballs": 6.99,
        "Pizza": {
            "Capracotta": 8.99,
            "Raffaella": 10.99,
            "Molisana": 9.99
        },
        "Sandwiches": {
            "Gianluca": 7.49,
            "Tonno": 8.49
        }
    },
    "Drinks": {
        "Limonata": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Water": {
            "Club": 2.49,
            "Sparkling": 3.99,
            "Still": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Americano": 2.99,
            "Cappuccino": 3.49
        }
    },
    "Dolce": {
        "Tiramisu": 10.99,
        "Gelati & Sorbetti": {
            "Cactus Pear": 4.99,
            "Black Current": 6.49
        },
        "Cannolo": 9.99,
        "Flourless Chocolate Cake": 4.99,
        "Dolce Vita": 4.49
    }
}

# Create an empty list. This list will later store a customer's order in the dictionary.
order_list = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_category = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():
            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]
            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_category_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # Ask customer to input menu item number
            menu_selection = input("Type item number: ")

            # Use input validation to check if the customer input menu_selection is a number.
            if menu_selection.isdigit():
                menu_selection = int(menu_selection)

                # Check if the menu selection is in the menu items
                if menu_selection in menu_items.keys():
                    # Get the item name from the menu_items dictionary and store it as a variable.
                    item_name = menu_items[menu_selection]["Item name"]

                    # Ask the customer for the quantity of the menu item, using the item name variable in the question,
                    # and let them know that the quantity will default to 1 if their input is invalid.
                    quantity = input(f"How many {item_name} would you like to order? (Default: 1) ")

                    # Check that the customer input is a number. If it isn't, set the quantity to 1.
                    if quantity.isdigit():
                        quantity = int(quantity)
                    else:
                        quantity = 1

                    # Append the customer's order to the order list in dictionary format.
                    order_list.append({
                        "Item name": item_name,
                        "Price": menu_items[menu_selection]["Price"],
                        "Quantity": quantity
                    })
                else:
                    # Print an error if the menu selection is not in menu_items keys.
                    print("Invalid item number.")
            else:
                # Print an error if the menu selection is not a number.
                print("Invalid item number.")
        else:
            # Print an error if the menu category selection is not valid.
            print(f"{menu_category} was not a menu option.")
    else:
        # Print an error if the customer didn't select a number.
        print("You didn't select a number.")

    while True:
        # Ask the customer if they would like to order anything else
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ")

        # Use a match-case statement for input validation
        match keep_ordering.lower():
            case "y":
                # Set place_order variable to True and break from the continuous while loop.
                place_order = True
                break
            case "n":
                # Set place_order variable to False, print "Thank you for your order," and break from the continuous while loop.
                place_order = False
                print("Thank you for your order.")
                break
            case _:
                # Default: Tell the customer to try again because they didn't type a valid input.
                print("Invalid input. Please enter 'Y' or 'N'.")

# Print out the customer's order receipt
print("This is your order receipt:\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# Loop through the items in the customer's order and print the receipt
for item in order_list:
    item_name = item["Item name"]
    price = item["Price"]
    quantity = item["Quantity"]

    # Calculate the number of empty spaces for formatting
    item_spaces = " " * (25 - len(item_name))
    price_spaces = " " * (10 - len(f"${price:.2f}"))
    quantity_spaces = " " * (10 - len(str(quantity)))

    # Create the space strings
    formatted_item_name = item_name + item_spaces
    formatted_price = f"${price:.2f}" + price_spaces
    formatted_quantity = str(quantity) + quantity_spaces

    # Print the line for the receipt using the specified format
    print(f"{formatted_item_name}| {formatted_price}| {formatted_quantity}")

# Calculate the total cost of the order using list comprehension
total_cost = sum([item["Price"] * item["Quantity"] for item in order_list])

# Display the total cost to the customer
print("\nTotal cost of your order:", f"${total_cost:.2f}")
