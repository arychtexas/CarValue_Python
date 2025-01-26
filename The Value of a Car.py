class Car:
    def __init__(self):
        self.model_year = 0
        self.purchase_price = 0  # Added purchase_price attribute
        self.current_value = 0
        self.model_make = f"{make}"
        self.model_name = f"{model}"

    def calc_current_value(self, current_year):
        depreciation_rate = 0.15
        # Car depreciation formula
        car_age = current_year - self.model_year
        self.current_value = round(self.purchase_price * (1 - depreciation_rate) ** car_age)

    def print_info(self):
        """Prints the car's model year, purchase price, and current value."""
        print(f"Car's information:\n\tCar Make: {self.model_make}\n\tCar Model: {self.model_name}\n\tModel year: {self.model_year}\n\tPurchase price: ${self.purchase_price:,}\n\tCurrent value: ${self.current_value:,}")


if __name__ == "__main__":
    make = input("Enter the maker name of the car: " )
    model = input("Enter the model name of the car: ")
    year = int(input("Enter the model year of the car: "))
    price = int(input("Enter the purchase price of the car: "))
    current_year = int(input("Enter the current year: "))

    my_car = Car()
    my_car.model_year = year
    my_car.purchase_price = price
    my_car.calc_current_value(current_year)
    my_car.print_info()
