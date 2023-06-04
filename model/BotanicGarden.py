from model.Garden import Garden


class BotanicGarden(Garden):

    def __init__(self, area=0.0, number_of_flowers=0, what_is_growing=[], number_of_fruit_trees=0,
                 number_of_greenhouses=0):
        super().__init__(area, number_of_flowers, what_is_growing)
        self.number_of_fruit_trees = number_of_fruit_trees
        self.number_of_greenhouses = number_of_greenhouses

    def has_orchard(self):
        return False

    def has_vegetable_garden(self):
        return True

    def __str__(self):
        return super().__str__() + (
            f"number of fruit_trees = {self.number_of_fruit_trees},\n "
            f"number of greenhouses = {self.number_of_greenhouses},\n ")


if __name__ == "__main__":
    botanic_garden = BotanicGarden(10, 11, ["Rosa spp", "Acer palmatum"], 12, 13)
    print(botanic_garden.has_orchard())
    print(botanic_garden)
