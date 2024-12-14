# Design Patterns and Overengineering in Pizza Restaurant System

## Design Patterns Detailed Explanation

### 1. Factory Method Pattern
#### Problem Before Pattern
Before implementing the Factory Method, pizza creation was tightly coupled with the client code. This meant:
- Direct instantiation of specific pizza types in the main function
- Hard-coded pizza creation logic
- Difficult to add new pizza types

#### Solution with Factory Method
```python
class PizzaFactory:
    @staticmethod
    def create_pizza(pizza_type: str) -> Pizza:
        if pizza_type == '1':
            return Margherita()
        elif pizza_type == '2':
            return Pepperoni()
```

#### Improvements
- Centralized pizza creation
- Easy to add new pizza types
- Decouples pizza creation from client code

### 2. Decorator Pattern
#### Problem Before Pattern
- Static pizza classes with fixed descriptions and costs
- No flexible way to add toppings
- Each topping combination would require a new class

#### Solution with Decorator
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

#### Improvements
- Dynamic topping addition
- Runtime modification of pizza properties
- No need for multiple subclasses for each topping combination

### 3. Singleton Pattern
#### Problem Before Pattern
- Multiple inventory managers could be created
- Inconsistent inventory tracking
- Potential data synchronization issues

#### Solution with Singleton
```python
class InventoryManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
```

#### Improvements
- Guaranteed single instance
- Global point of access
- Consistent inventory management

### 4. Strategy Pattern
#### Problem Before Pattern
- Hardcoded payment methods
- Difficult to add new payment options
- Payment logic mixed with order processing

#### Solution with Strategy
```python
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class PaymentContext:
    def __init__(self, strategy: PaymentStrategy):
        self._strategy = strategy

    def pay(self, amount: float) -> bool:
        return self._strategy.pay(amount)
```

#### Improvements
- Interchangeable payment methods
- Easy to add new payment strategies
- Separation of payment logic

## Overengineering: A Cautionary Example

### Potential Overengineering Scenario
```python
# Overengineered Pizza Creation
class AbstractPizzaBuilder:
    def __init__(self):
        self._extremely_complex_pizza = {}
    
    def set_base_type(self, base_type: str):
        self._extremely_complex_pizza['base_type'] = base_type
        return self
    
    def add_custom_sauce(self, sauce_complexity: int):
        self._extremely_complex_pizza['sauce_complexity'] = sauce_complexity
        return self
    
    def add_precision_topping_distribution(self, distribution_algorithm: str):
        self._extremely_complex_pizza['topping_distribution'] = distribution_algorithm
        return self
    
    def build(self):
        # Extremely complex pizza creation logic
        return self._extremely_complex_pizza

# Usage
pizza_builder = AbstractPizzaBuilder()
pizza = (pizza_builder
    .set_base_type('Margherita')
    .add_custom_sauce(5)
    .add_precision_topping_distribution('gaussian')
    .build())
```

### Why This is Overengineering
1. Unnecessary Complexity
   - Simple pizza creation doesn't need such an elaborate builder
   - Adds significant cognitive overhead
   - Increases development and maintenance time

2. Premature Abstraction
   - Solving problems that don't exist
   - Creating flexibility where none is needed
   - Violates YAGNI (You Aren't Gonna Need It) principle

3. Performance Overhead
   - Additional method calls
   - More memory usage
   - Increased computational complexity

### Signs of Overengineering
- Multiple layers of abstraction
- Excessive flexibility
- Complex design for simple requirements
- Anticipating hypothetical future needs

### Best Practices
1. Start Simple
2. Refactor When Necessary
3. Follow SOLID Principles
4. Keep Design Proportional to Problem Complexity
