# SOLID Principles and Design Patterns in Pizza Ordering System

## Design Patterns Applied

### 1. Factory Pattern (PizzaFactory)
**SOLID Principles Adhered:**
- **Single Responsibility Principle (SRP):** The `PizzaFactory` has a single responsibility of creating pizza objects.
- **Open/Closed Principle (OCP):** The factory can be extended to create new pizza types without modifying existing code.

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
**SOLID Principles Adhered:**
- **Single Responsibility Principle (SRP):** Manages inventory with a single point of control.
- **Dependency Inversion Principle (DIP):** Provides a global point of access to inventory management.

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
**SOLID Principles Adhered:**
- **Single Responsibility Principle (SRP):** Each payment method has its own implementation.
- **Open/Closed Principle (OCP):** New payment methods can be added without modifying existing code.
- **Liskov Substitution Principle (LSP):** Different payment strategies can be used interchangeably.

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
**SOLID Principles Adhered:**
- **Single Responsibility Principle (SRP):** Defines a common interface for pizza objects.
- **Liskov Substitution Principle (LSP):** Allows different pizza types to be used interchangeably.

**Implementation:**
```python
class Pizza(ABC):
    def __init__(self, name, price):
        self._name = name
        self._price = price
        self._toppings = []

    def get_description(self):
        # Common implementation for all pizza types
        ...
```

## Detailed SOLID Principle Analysis

### Single Responsibility Principle (SRP)
- Each class has a single, well-defined responsibility:
  - `PizzaFactory` creates pizzas
  - `InventoryManager` manages inventory
  - `PaymentStrategy` handles payment methods
  - `Pizza` manages pizza-related operations

### Open/Closed Principle (OCP)
- The system allows extension without modification:
  - New pizza types can be added to `PizzaFactory`
  - New payment methods can be added by implementing `PaymentStrategy`
  - New toppings can be easily incorporated into the existing structure

### Liskov Substitution Principle (LSP)
- Derived classes can be used interchangeably:
  - Different pizza types inherit from the base `Pizza` class
  - Payment strategies can be swapped without changing the core logic

### Interface Segregation Principle (ISP)
- Interfaces are kept minimal and focused:
  - `PaymentStrategy` has a single method `pay()`
  - `Pizza` has clear, minimal interface methods

### Dependency Inversion Principle (DIP)
- High-level modules depend on abstractions:
  - `PaymentStrategy` is an abstract base class
  - `InventoryManager` provides a global access point
  - Concrete implementations depend on abstract interfaces
