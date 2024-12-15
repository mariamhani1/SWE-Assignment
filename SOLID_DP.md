# Design Patterns and SOLID Principles Analysis

## Factory Method Pattern
- **Single Responsibility Principle**: The PizzaFactory class has one responsibility - creating pizza objects.
- **Open/Closed Principle**: Adding new pizza types only requires creating new pizza classes without modifying existing code.
- **Dependency Inversion**: High-level modules depend on abstractions (Pizza interface) not concrete classes.

## Decorator Pattern (Toppings)
- **Single Responsibility Principle**: Each topping class handles one specific topping addition.
- **Open/Closed Principle**: New toppings can be added by creating new decorator classes without changing existing code.
- **Liskov Substitution**: All decorators can replace the base Pizza object seamlessly.

## Strategy Pattern (Payment)
- **Single Responsibility Principle**: Each payment strategy handles one payment method.
- **Open/Closed Principle**: New payment methods can be added without modifying existing code.
- **Interface Segregation**: PaymentWay interface is focused on a single method (pay).
