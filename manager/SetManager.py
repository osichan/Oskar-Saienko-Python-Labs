from manager.GardenManager import GardenManager
from model.BotanicGarden import BotanicGarden
from model.Farmstead import Farmstead
from model.Orchard import Orchard
from model.UniversityGarden import UniversityGarden


class SetManager:
    current_index = 0

    def __init__(self, regular_manager):
        self.regular_manager = regular_manager

    def __iter__(self):
        return iter(self.regular_manager)

    def __len__(self):
        length = 0
        for garden in self.regular_manager:
            length += len(garden.what_is_growing)
        return length

    def __getitem__(self, index):
        for obj in self.regular_manager:
            what_is_growing_set = obj.what_is_growing
            if index < len(what_is_growing_set):
                return list(what_is_growing_set)[index]
            index -= len(what_is_growing_set)
        raise IndexError("Index out of range")

    def __next__(self):
        for obj in self.regular_manager:
            what_is_growing_set = obj.what_is_growing
            if len(what_is_growing_set) > 0:
                return list(what_is_growing_set)[0]
        raise StopIteration


if __name__ == "__main__":
    manager = GardenManager()
    manager.add_gardens(
        [BotanicGarden(10, 11, ["Rosa spp", "Acer palmatum"], 12, 13), Farmstead(10, 11, ["oats", "sunflower"], 12),
         Orchard(10, 11, ["Apple Trees", "Pear Trees"], 12), UniversityGarden(10, 11, ["Lavandula", "Asclepias"], 12)])

    SM = SetManager(manager.gardens)

    print("\nLength of Set Manager:", len(SM))

    print("\nSet Manager by index:")
    for i in range(len(SM)):
        print(SM[i])