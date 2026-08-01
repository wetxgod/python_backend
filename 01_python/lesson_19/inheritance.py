# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         print(f"{self.name} makes a sound.")


# class Dog(Animal):
#     def bark(self):
#         print(f"{self.name} barks: Woof!")


# dog = Dog("Buddy")
# dog.speak()
# dog.bark()


class Vehicle:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

    def show_info(self):
        print(f"Brand: {self.brand}")
        print(f"Year: {self.year}")


class Car(Vehicle):
    def __init__(self, brand, year, model):
        super().__init__(brand, year)
        self.model = model

    def show_info(self):
        super().show_info()
        print(f"Model: {self.model}")


class Motorcycle(Vehicle):
    def __init__(self, brand, year, engine_volume):
        super().__init__(brand, year)
        self.engine_volume = engine_volume

    def show_info(self):
        super().show_info()
        print(f"Engine Volume: {self.engine_volume}cc")

    def start_engine(self):
        print(f"{self.brand} motorcycle engine started.")


motorcycle = Motorcycle("Yamaha", 2022, 600)
motorcycle.show_info()
motorcycle.start_engine()
