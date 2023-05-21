class Garden:
    __instance = None

    def __init__(self, area: float = 0.0, has_orchard: bool = False, has_vegetable_garden: bool = False,
                 number_of_flowers: int = 0):
        self.__area = area
        self.__has_orchard = has_orchard
        self.__has_vegetable_garden = has_vegetable_garden
        self.__number_of_flowers = number_of_flowers

    def plant_flowers(self, number_of_flowers_to_plant: int):
        self.__number_of_flowers += number_of_flowers_to_plant

    def remove_flowers(self, number_of_flowers_to_remove: int):
        self.__number_of_flowers -= number_of_flowers_to_remove
        if self.__number_of_flowers < 0:
            self.__number_of_flowers = 0

    def add_vegetable_garden(self):
        self.__has_vegetable_garden = True

    def to_str(self):
        return (f"area = {self.__area},"
                f"\nhas orchard = {self.__has_orchard},"
                f"\nhas vegetable garden = {self.__has_vegetable_garden},"
                f"\nnumber of flowers = {self.__number_of_flowers} ")

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = value

    @property
    def has_orchard(self):
        return self.__has_orchard

    @has_orchard.setter
    def has_orchard(self, value):
        self.__has_orchard = value

    @property
    def has_vegetable_garden(self):
        return self.__has_vegetable_garden

    @has_vegetable_garden.setter
    def has_vegetable_garden(self, value):
        self.__has_vegetable_garden = value

    @property
    def number_of_flowers(self):
        return self.__number_of_flowers

    @number_of_flowers.setter
    def number_of_flowers(self, value):
        self.__number_of_flowers = value

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Garden()
        return cls.__instance


if __name__ == '__main__':
    gardens = [Garden(), Garden(20.0, True, False, 4), Garden.get_instance(), Garden.get_instance()]
    for garden in gardens:
        print(garden.to_str() + "\n")
