from abc import ABC, abstractmethod

# Pizza Base class
class Pizza(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._toppings = []

    def add_topping(self, topping):
        self._toppings.append(topping)

    def get_description(self):
        description = self._name
        if self._toppings:
            description += " with " + ", ".join(topping.name for topping in self._toppings)
        return description

    def get_cost(self):
        return self._price + sum(topping.price for topping in self._toppings)

# Pizza Types
class MargheritaPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Margherita", 5.0)

class PepperoniPizza(Pizza):
    def __init__(self):
        Pizza.__init__(self, "Pepperoni", 6.0)

# Topping Class
class Topping:
    def __init__(self, name, price):
        self.name = name
        self.price = price

# Pizza Factory
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "Margherita":
            return MargheritaPizza()
        elif pizza_type == "Pepperoni":
            return PepperoniPizza()

# Inventory Manager
class InventoryManager:
    _instance = None

    def __new__(self):
        if InventoryManager._instance is None:
            InventoryManager._instance = object.__new__(InventoryManager)
            InventoryManager._instance._inventory = {
                "Margherita": 10,
                "Pepperoni": 10,
                "Toppings": {
                    "Cheese": 15,
                    "Olives": 10,
                    "Mushrooms": 12
                }
            }
        return InventoryManager._instance

    def check_and_decrement(self, item, category="Toppings"):
        if category == "Toppings":
            if self._inventory["Toppings"].get(item, 0) > 0:
                self._inventory["Toppings"][item] -= 1
                return True
        else:  # For pizza base types
            if self._inventory.get(item, 0) > 0:
                self._inventory[item] -=    1
                return True
        return False

    def get_inventory(self):
        return self._inventory

# Payment Strategy
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount} using PayPal.")

class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid ${amount} using Credit Card.")

# Available Toppings
AVAILABLE_TOPPINGS = {
    "1": Topping("Cheese", 1.0),
    "2": Topping("Olives", 0.5),
    "3": Topping("Mushrooms", 0.7)
}

def main():
    inventory_manager = InventoryManager()

    print("Welcome to the Pizza Restaurant!")

    while True:
        # Pizza Selection
        print("\nChoose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0. To exit")
        
        pizza_choice = input("Enter the number of your choice: ")
        if pizza_choice == '0':
            break

        # Create Pizza
        try:
            if pizza_choice == "1":
                pizza_type = "Margherita"
            elif pizza_choice == "2":
                pizza_type = "Pepperoni"
            
            # Check inventory
            if not inventory_manager.check_and_decrement(pizza_type, category="Pizza"):
                print("Pizza unavailable or out of stock!")
                continue

            # Create pizza using factory method
            pizza = PizzaFactory.create_pizza(pizza_type)

            # Add Toppings
            while True:
                print("\nAvailable toppings:")
                print("1. Cheese ($1.0)")
                print("2. Olives ($0.5)")
                print("3. Mushrooms ($0.7)")
                print("4. Finish order")
                
                topping_choice = input("Enter the number of your choice: ")
                
                if topping_choice == "4":
                    break
                
                if topping_choice in AVAILABLE_TOPPINGS:
                    topping = AVAILABLE_TOPPINGS[topping_choice]
                    
                    # Check topping inventory
                    if inventory_manager.check_and_decrement(topping.name):
                        pizza.add_topping(topping)
                    else:
                        print("Topping unavailable or out of stock!")
                else:
                    print("Invalid topping choice!")

            # Display final pizza details
            print("\nYour order:")
            print(f"Description: {pizza.get_description()}")
            print(f"Total cost: ${pizza.get_cost()}")

            # Payment
            print("\nChoose a payment method:")
            print("1. PayPal")
            print("2. Credit Card")
            payment_choice = input("Enter the number of your choice: ")

            if payment_choice == "1":
                payment_strategy = PayPalPayment()
            elif payment_choice == "2":
                payment_strategy = CreditCardPayment()
            else:
                print("Invalid payment method!")
                continue

            payment_strategy.pay(pizza.get_cost())

            # Show final inventory
            print("\nRemaining Inventory:")
            print(inventory_manager.get_inventory())

        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
