from abc import abstractmethod
from exception.InvalidFlowersNumberException import InvalidFlowersNumberException

import logging

def logged(exception, mode):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except exception:
                logger = logging.getLogger(__name__)
                if mode == "console":
                    logger.error(f"Exception {exception.__name__} occurred, in {func.__name__}")
                elif mode == "file":
                    logger_file = logging.FileHandler("EXCEPTION.txt")
                    logger.addHandler(logger_file)
                    logger.error(f"Exception {exception.__name__} occurred, in {func.__name__}")
                    logger.removeHandler(logger_file)
                    logger_file.close()
                else:
                    raise ValueError("Invalid mode. Choose 'console' or 'file'.")
        return wrapper
    return decorator

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

    @logged(InvalidFlowersNumberException, "file")
    def plant_flowers(self, number_of_flowers_to_plant: int):
        if number_of_flowers_to_plant < 0:
            raise InvalidFlowersNumberException("Number of flowers to plant cannot be negative")
        self.number_of_flowers += number_of_flowers_to_plant

    @logged(InvalidFlowersNumberException, "console")
    def remove_flowers(self, number_of_flowers_to_remove: int):
        if number_of_flowers_to_remove < 0:
            raise InvalidFlowersNumberException("Number of flowers to remove cannot be negative")
        self.number_of_flowers -= number_of_flowers_to_remove

    def get_attributes_by_type(self, data_type):
        return {key: value for key, value in self.__dict__.items() if isinstance(value, data_type)}

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

    garden = Garden(1,2)
    garden.plant_flowers(-5)
    garden.remove_flowers(-5)
