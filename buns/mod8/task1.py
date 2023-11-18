class Transport:
    def __init__(self, *args, **kwargs):
        self.coordinates = args[0]
        self.speed = args[1]
        self.brand = kwargs["brand"]
        self.year = year
        self.number = number

    @property
    def coordinates(self):
        return self.__coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        self.__coordinates = coordinates

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, speed):
        self.__speed = speed

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def coordinates(self, brand):
        self.__brand = brand

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        self.__year = year

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        self.__number = number


class Passenger(Transport):
    def __init__(self, passengers_capacity, number_of_passengers, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.passengers_capacity = passengers_capacity
        self.number_of_passengers = number_of_passengers

    @property
    def passengers_capacity(self):
        return self.__passengers_capacity

    @passengers_capacity.setter
    def passengers_capacity(self, passengers_capacity):
        self.__passengers_capacity = passengers_capacity

    @property
    def number_of_passengers(self):
        return self.__number_of_passengers

    @number_of_passengers.setter
    def number_of_passengers(self, number_of_passengers):
        self.__number_of_passengers = number_of_passengers


class Cargo(Transport):
    def __init__(self, carrying, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__carrying = carrying

    @property
    def carrying(self):
        return self.__carrying

    @carrying.setter
    def carrying(self, carrying):
        self.__carrying = carrying


class Plane(Transport):
    def __init__(self, height, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if height < 0:
            raise ValueError("Высота не может быть глубиной.")
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        self.__height = height


class Auto(Transport):
    pass


class Ship(Transport):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.port = kwargs["port"]


class Car(Auto):
    pass


class Bus(Auto, Passenger):
    pass


class CargoAuto(Auto, Cargo):
    pass


class Boat(Ship):
    pass


class PassengerShip(Ship, Passenger):
    pass


class CargoShip(Ship, Cargo):
    pass
