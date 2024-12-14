# Design Patterns and SOLID Principles in Pizza Restaurant System

## Design Patterns Used

### 1. Factory Method Pattern
#### SOLID Principles Addressed
- **Single Responsibility Principle (SRP)**: The `PizzaFactory` is solely responsible for creating pizza objects.
- **Open/Closed Principle (OCP)**: Easy to extend by adding new pizza types without modifying existing code.

#### Implementation
```python
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type == '1':
            return Margherita()
        elif pizza_type == '2':
            return Pepperoni()
```

### 2. Decorator Pattern
#### SOLID Principles Addressed
- **Open/Closed Principle (OCP)**: Allows adding new toppings without modifying existing pizza classes.
- **Single Responsibility Principle (SRP)**: Each topping decorator has a single responsibility of adding description and cost.

#### Implementation
```python
class PizzaDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

class CheeseTopping(PizzaDecorator):
    def get_description(self) -> str:
        return f"{self._pizza.get_description()}, Cheese"
    
    def get_cost(self) -> float:
        return self._pizza.get_cost() + 1.0
```

### 3. Singleton Pattern
#### SOLID Principles Addressed
- **Dependency Inversion Principle (DIP)**: Provides a global point of access to inventory management.
- **Single Responsibility Principle (SRP)**: Ensures only one inventory manager exists.

#### Implementation
```python
class InventoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

### 4. Strategy Pattern
#### SOLID Principles Addressed
- **Open/Closed Principle (OCP)**: Easy to add new payment methods without modifying existing code.
- **Dependency Inversion Principle (DIP)**: Depends on abstractions (PaymentStrategy) rather than concrete implementations.

#### Implementation
```python
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> bool:
        print(f"Paying ${amount:.2f} via PayPal")
        return True
```

## Benefits of Design Patterns

1. **Flexibility**: Each pattern provides a way to make the system more flexible and extensible.
2. **Separation of Concerns**: Breaks down complex logic into manageable, focused components.
3. **Easy Maintenance**: Modular design allows for easier updates and additions to the system.

## Key SOLID Principle Alignments

- **Single Responsibility Principle**: Each class has a single, well-defined responsibility.
- **Open/Closed Principle**: System is open for extension but closed for modification.
- **Liskov Substitution Principle**: Derived classes can be substituted for their base classes.
- **Interface Segregation Principle**: Multiple specific interfaces are better than one general-purpose interface.
- **Dependency Inversion Principle**: High-level modules depend on abstractions, not concrete implementations.
