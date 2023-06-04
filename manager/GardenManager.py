from model.Garden import Garden
from model.BotanicGarden import BotanicGarden
from model.Farmstead import Farmstead
from model.Orchard import Orchard
from model.UniversityGarden import UniversityGarden


def log_parameters(func):
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with parameters: args={args} kwargs={kwargs}")
        return func(*args, **kwargs)

    return wrapper


def log_return_value(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result

    return wrapper


class GardenManager:
    gardens = []
    current_index = 0

    @log_parameters
    @log_return_value
    def add_gardens(self, gardens_to_add):
        self.gardens += gardens_to_add

    @log_parameters
    @log_return_value
    def find_garden_with_flowers_more_than(self, number_of_flowers_to_check):
        answer = [garden for garden in self.gardens if number_of_flowers_to_check >= garden.number_of_flowers]
        return answer

    @log_parameters
    @log_return_value
    def find_garden_with_area_less_than(self, area_to_check):
        answer = [garden for garden in self.gardens if area_to_check <= garden.area]
        return answer

    @log_return_value
    def __len__(self):
        return len(self.gardens)

    @log_parameters
    @log_return_value
    def __getitem__(self, index):
        return self.gardens[index]

    def __iter__(self):
        return iter(self.gardens)

    def __next__(self):
        if self.current_index < len(self.gardens):
            self.current_index += 1
            return self.gardens[self.current_index - 1]
        raise StopIteration

    @log_return_value
    def results_of_has_orchard(self):
        return [garden.has_orchard() for garden in self.gardens]

    @log_return_value
    def obj_and_his_index(self):
        return [f"{index}: {type(garden)}" for index, garden in enumerate(self.gardens)]

    @log_return_value
    def obj_and_result_of_has_orchard(self):
        return zip(self.gardens, [garden.has_orchard() for garden in self.gardens])

    @log_parameters
    @log_return_value
    def check_condition(self, condition_to_check):
        result = f"all: {all(condition_to_check(garden) for garden in self.gardens)}", \
            f"any: {any(condition_to_check(garden) for garden in self.gardens)}"
        return result


def is_in_garden_flowers_more_than_10(garden_to_check):
    return garden_to_check.number_of_flowers > 10


if __name__ == "__main__":
    manager = GardenManager()
    manager.add_gardens(
        [BotanicGarden(10, 11, ["Rosa spp", "Acer palmatum"], 12, 13), Farmstead(10, 11, ["oats", "sunflower"], 12),
         Orchard(10, 11, ["Apple Trees", "Pear Trees"], 12), UniversityGarden(10, 11, ["Lavandula", "Asclepias"], 12)])

    for garden in manager.gardens:
        print(f"{type(garden).__name__}\n{garden}")

    print(manager.results_of_has_orchard(), "\n")

    print(manager.obj_and_his_index(), "\n")

    for obj in manager.obj_and_result_of_has_orchard():
        print(obj)

    print("\n")

    for garden in manager.gardens:
        print(garden.get_attributes_by_type(int))

    print("\n")

    print(manager.check_condition(is_in_garden_flowers_more_than_10))
