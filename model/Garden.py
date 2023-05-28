from abc import abstractmethod


class Garden:
    __instance = None

    def __init__(self, area: float = 0.0, number_of_flowers: int = 0):
        self.area = area
        self.number_of_flowers = max(number_of_flowers, 0)

    @abstractmethod
    def has_orchard(self):
        pass

    @abstractmethod
    def has_vegetable_garden(self):
        pass

    def plant_flowers(self, number_of_flowers_to_plant: int):
        self.number_of_flowers += number_of_flowers_to_plant

    def remove_flowers(self, number_of_flowers_to_remove: int):
        self.number_of_flowers -= number_of_flowers_to_remove

    @abstractmethod
    def __str__(self):
        return (f"area = {self.area},\n"
                f"number of flowers = {self.number_of_flowers},\n ")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Garden()
        return cls.__instance


if __name__ == '__main__':
    gardens = [Garden(), Garden(20.0, 4), Garden.get_instance(), Garden.get_instance()]
    for garden in gardens:
        print(garden)
