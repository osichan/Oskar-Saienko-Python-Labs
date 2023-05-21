from model.Garden import Garden
from model.BotanicGarden import BotanicGarden
from model.Farmstead import Farmstead
from model.Orchard import Orchard
from model.UniversityGarden import UniversityGarden


class GardenManager:
    gardens = []

    def add_gardens(self, gardens_to_add):
        self.gardens += gardens_to_add

    def find_garden_with_flowers_more_than(self, number_of_flowers_to_check):
        answer = []
        for garden in self.gardens:
            if garden.number_of_flowers >= number_of_flowers_to_check:
                answer += garden
        return answer

    def find_garden_with_area_less_than(self, area_to_check):
        answer = []
        for garden in self.gardens:
            if garden.area <= area_to_check:
                answer += garden
        return answer


if __name__ == "__main__":
    manager = GardenManager()
    manager.add_gardens(
        [BotanicGarden(1, 2, 3, 4), Farmstead(5, 6, 7), Orchard(8, 9, 10), UniversityGarden(11, 12, 13)])
    for garden in manager.gardens:
        print(f"{type(garden).__name__}\n{garden}")
