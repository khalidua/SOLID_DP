# SOLID Principles and Design Patterns in Pizza Ordering System

## Design Patterns Applied

### 1. Factory Pattern (PizzaFactory)
**SOLID Principles:**
- **Single Responsibility Principle:** The `PizzaFactory` has a single responsibility of    creating pizza objects.
- **Open/Closed Principle:** The factory can create new pizza types without modifying existing code.

**Implementation:**
```python
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "Margherita":
            return MargheritaPizza()
        elif pizza_type == "Pepperoni":
            return PepperoniPizza()
```

### 2. Singleton Pattern (InventoryManager)
**SOLID Principles:**
- **Single Responsibility Principle:** Manages inventory with only one instance to control.
- **Dependency Inversion Principle:** Provides a global instance access to inventory management.

**Implementation:**
```python
class InventoryManager:
    _instance = None

    def __new__(self):
        if InventoryManager._instance is None:
            InventoryManager._instance = object.__new__(InventoryManager)
            InventoryManager._instance._inventory = {...}
        return InventoryManager._instance
```

### 3. Strategy Pattern (PaymentStrategy)
**SOLID Principles:**
- **Single Responsibility Principle:** Each payment method has its own implementation.
- **Open/Closed Principle:** New payment methods can be added without modifying existing code.
- **Liskov Substitution Principle:** Different payment strategies can be used without any errors in the system.

**Implementation:**
```python
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
```

### 4. Abstract Base Class Pattern (Pizza)
**SOLID Principles :**
- **Single Responsibility Principle:** makes an interface for pizza objects.
- **Liskov Substitution Principle :** Allows different pizza types to be used without problems.

**Implementation:**
```python
class Pizza(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._toppings = []

    def get_description(self):
        ...
```

## Detailed SOLID Principle Analysis

### Single Responsibility Principle
- Each class has a single responsibility:
  - `PizzaFactory` creates pizzas
  - `InventoryManager` manages inventory
  - `PaymentStrategy` handles payment methods
  - `Pizza` manages pizza operations

### Open/Closed Principle 
- The system allows extension without modification:
  - New pizza types can be added to `PizzaFactory`
  - New payment methods can be added by implementing `PaymentStrategy`
  - New toppings can be easily added into the existing methods

### Liskov Substitution Principle
- Derived classes can be used without problems:
  - Different pizza types inherit from the base `Pizza` class
  - Payment strategies can be swapped without changing the logic

### Interface Segregation Principle
- Interfaces are focused:
  - `PaymentStrategy` has a single method `pay()`
  - `Pizza` has clear interface methods

### Dependency Inversion Principle
- some classes depends on abstractions:
  - `PaymentStrategy` is an abstract base class
  - `InventoryManager` provides a global access point
