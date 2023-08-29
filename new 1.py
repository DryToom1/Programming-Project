# Initialise the menu dictionary with item names as keys and prices as values 
menu = { 
    "Beef Pie": 3.00, 
    "Vegetable Pastie": 3.00, 
    "Sausage Roll": 2.50, 
    "Hamburger": 3.50, 
    "Hot Dog": 3.00, 
    "Cheesie": 0.80, 
    "Pizza Roll": 1.50, 
    "Ham and Cheese Roll": 4.00, 
    "Chicken and Salad Roll": 4.50, 
    "Flavoured Milk": { 
        "300ml": { 
            "Chocolate": 1.80, 
            "Strawberry": 1.80, 
            "Banana": 1.80, 
            "Spearmint": 1.80 
        }, 
        "600ml": { 
            "Chocolate": 3.20, 
            "Strawberry": 3.20, 
            "Banana": 3.20, 
            "Spearmint": 3.20 
        } 
    }, 
    "Orange C": { 
        "300ml": 1.80, 
        "600ml": 2.80 
    }, 
    "600ml Water": 1.80, 
    "Ice Fruit Sticks": 0.50, 
    "Boost Bliss Bar": 2.00, 
    "Billabong": 1.50, 
    "Frozen Yoghurt": 1.70 
} 
  
# Initialise variables for item summary and day’s turnover 
item_summary = {}  # Dictionary to store item summary totals (item name -> {'total': total_cost, 'quantity': quantity}) 
days_turnover = 0 

def calculate_takeaway_charge(item_price): 
    takeaway_charge = 0.05 * item_price 
    total_price = item_price + takeaway_charge 
    return total_price 
  
def calculate_discount(total_amount): 
    if len(item_summary) >= 3: 
        discount = 0.10 * total_amount 
        discounted_total = total_amount - discount 
        return discounted_total 
    return total_amount 
  
def update_item_summary(item, item_price, quantity): 
    if item in item_summary: 
        item_summary[item]['total'] += item_price * quantity 
        item_summary[item]['quantity'] += quantity 
    else: 
        item_summary[item] = {'total': item_price * quantity, 'quantity': quantity} 
    global days_turnover 
    days_turnover += item_price * quantity 
  
def process_order(item, quantity, order_type): 
    if item == "Flavoured Milk": 
        while True: 
            size = input("Select flavored milk size (300ml or 600ml): ") 
            if size in ['300ml', '600ml']: 
                break 
            else: 
                print("Invalid input. Please enter '300ml' or '600ml'.") 
         
        while True: 
            flavor = input("Select flavored milk flavor (Chocolate, Strawberry, Banana, Spearmint): ").capitalize() 
            if flavor in ['Chocolate', 'Strawberry', 'Banana', 'Spearmint']: 
                break 
            else: 
                print("Invalid input. Please enter a valid flavor.") 
         
        item_price = menu["Flavoured Milk"][size][flavor] 
         
    elif item == "Orange C": 
        while True: 
            size = input("Select Orange C size (300ml or 600ml): ") 
            if size in ['300ml', '600ml']: 
                break 
            else: 
                print("Invalid input. Please enter '300ml' or '600ml'.") 
         
        item_price = menu["Orange C"][size] 
    else: 
        item_price = menu.get(item, 0) 
     
    if order_type == 'takeaway': 
        item_price = calculate_takeaway_charge(item_price) 
     
    return item_price * quantity 

def process_orders(order_items):
    total_amount = 0.00
    for item, quantity, order_type in order_items:
        item_total = process_order(item, quantity, order_type)
        total_amount += item_total
    return total_amount

def main():
    order_items = []
  
    while True:
        item = input("Enter item name (or 'done' to finish): ")
        if item not in menu:
            print(f"{item} is not on the menu. Please enter a valid item.")
            continue  # Skip to the next iteration if the item is not on the menu
        if item.lower() == "done":
            break
        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity <= 0:
                    print("Quantity must be a positive number.")
                else:
                    break
            except ValueError:
                print("Invalid input. Please enter a valid quantity.")
         
            while True:
                order_type = input("Dine-in or takeaway? ").lower()
                if order_type in ['dine-in', 'takeaway']:
                    break
                else:
                    print("Invalid input. Please enter 'dine-in' or 'takeaway'.")
          
            order_items.append((item, quantity, order_type))
  
    order_total = process_orders(order_items)
  
    for item, details in item_summary.items():
        print(f"{item}: Total - {details['total']}, Quantity - {details['quantity']}")
  
    discounted_total = calculate_discount(order_total)
    print("Order total:", order_total)
    
    if discounted_total != order_total:
        print("Discounted total:", discounted_total)
    else:
        print("No discount applied.")

    print("Day's turnover:", days_turnover)

if __name__ == "__main__":
    main()
