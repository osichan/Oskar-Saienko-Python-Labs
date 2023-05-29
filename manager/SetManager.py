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
        our_list = []
        for obj in self.regular_manager:
            our_list += obj
        if index <= len(our_list):
            return our_list[index]
        raise IndexError("Index out of range")

    def __next__(self):
        our_list = []
        for obj in self.regular_manager:
            our_list += obj
        if self.current_index < len(our_list):
            result = our_list[self.current_index]
            self.current_index += 1
            return result

        raise StopIteration()


if __name__ == "__main__":
    manager = GardenManager()
    manager.add_gardens(
        [BotanicGarden(10, 11, ["Rosa spp", "Acer palmatum"], 12, 13), Farmstead(10, 11, ["Oats", "Sunflower"], 12),
         Orchard(10, 11, ["Apple Trees", "Pear Trees"], 12), UniversityGarden(10, 11, ["Lavandula", "Asclepias"], 12)])

    SM = SetManager(manager.gardens)

    print("\nLength of Set Manager:", len(SM))

    print("\nSet Manager by index:")
    for i in range(len(SM)):
        print(i,SM[i])
