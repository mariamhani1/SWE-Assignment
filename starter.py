from abc import ABC, abstractmethod

class Pizza(ABC):
    @abstractmethod
    def price(self) -> float:
        pass

    @abstractmethod
    def details(self) -> str:
        pass


class PepperoniPizza(Pizza):
    def price(self) -> float:
        return 6.0

    def details(self) -> str:
        return "Pepperoni Pizza"

class MargheritaPizza(Pizza):
    def price(self) -> float:
        return 5.0

    def details(self) -> str:
        return "Margherita Pizza"
class PizzaFactory:
    @staticmethod
    def make_pizza(pizza_type: str) -> Pizza:
        if pizza_type == "1":
            return MargheritaPizza()
        elif pizza_type == "2":
            return PepperoniPizza()
        else:
            raise ValueError("Invalid pizza type")

class Toppings(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

class OlivesToppings(Toppings):
    def price(self) -> float:
        return self._pizza.price() + 0.5
    def details(self) -> str:
        return self._pizza.details() + ", Olives"


class MushroomsToppings(Toppings):
    def price(self) -> float:
        return self._pizza.price() + 0.7

    def details(self) -> str:
        return self._pizza.details() + ", Mushrooms"

class CheeseTopping(Toppings):
    def price(self) -> float:
        return self._pizza.price() + 1.0

    def details(self) -> str:
        return self._pizza.details() + ", Cheese"


class PayementWay(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class PayPalPayment(PayementWay):
    def pay(self, amount: float) -> bool:
        print(f"Processing ${amount:.2f} payment via PayPal...")
        return True

class CreditCardPayment(PayementWay):
    def pay(self, amount: float) -> bool:
        print(f"Processing ${amount:.2f} payment via Credit Card...")
        return True

class StorageManager:
    _storage = {
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,
    }
    def check_and_decrement(self, item: str) -> bool:
        if self._storage.get(item, 0) > 0:
            self._storage[item] -= 1
            return True
        return False

    def get_storage(self):
        return self._storage

def main():
    storage_manager = StorageManager()
    print("Welcome to the Pizza Restaurant!")

    while True:
        print("Choose your base pizza:")
        print("1. Margherita ($5.0)")
        print("2. Pepperoni ($6.0)")
        print("0 => to exit")
        pizza_choice = input("Enter the number of your choice: ")
        
        if pizza_choice == '0':
            break

        try:
            pizza = PizzaFactory.make_pizza(pizza_choice)
            
            while True:
                print("\nAvailable toppings:")
                print("1. Cheese ($1.0)")
                print("2. Olives ($0.5)")
                print("3. Mushrooms ($0.7)")
                print("4. Finish order")
                toppings = input("Enter the number of your choice: ")

                if toppings == "1" and storage_manager.check_and_decrement("Cheese"):
                    pizza = CheeseTopping(pizza)
                elif toppings == "2" and storage_manager.check_and_decrement("Olives"):
                    pizza = OlivesToppings(pizza)
                elif toppings == "3" and storage_manager.check_and_decrement("Mushrooms"):
                    pizza = MushroomsToppings(pizza)
                elif toppings == "4":
                    break
                else:
                    print("Topping unavailable or out of stock!")

            print("\nYour order:")
            print(f"Description: {pizza.details()}")
            print(f"Total cost: ${pizza.price():.2f}")

            # Payment processing
            print("\nChoose payment method:")
            print("1. PayPal")
            print("2. Credit Card")
            payment_choice = input("Enter payment method (1/2): ")
            
            payment_strategy = PayPalPayment() if payment_choice == "1" else CreditCardPayment()
            if payment_strategy.pay(pizza.price()):
                print("Payment successful! Thank you for your order.")
            
            print("\nRemaining Inventory:")
            print(storage_manager.get_storage())

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
