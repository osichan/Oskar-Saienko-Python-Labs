from abc import abstractmethod


class Garden:
    __instance = None

    def __init__(self, area: float = 0.0, number_of_flowers: int = 0, what_is_growing: [] = []):
        self.area = area
        self.number_of_flowers = max(number_of_flowers, 0)
        self.what_is_growing = what_is_growing

    def __iter__(self):
        return iter(self.what_is_growing)

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

    def get_attributes_by_type(obj, data_type):
        return {key: value for key, value in obj.__dict__.items() if isinstance(value, data_type)}

    @abstractmethod
    def __str__(self):
        return (f"area = {self.area},\n"
                f"number of flowers = {self.number_of_flowers},\n" 
                f"number of flowers = {self.what_is_growing},\n")

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = Garden()
        return cls.__instance


if __name__ == '__main__':
    gardens = [Garden(), Garden(20.0, 4), Garden.get_instance(), Garden.get_instance()]
    for garden in gardens:
        print(garden)
