from model.Garden import Garden


class Farmstead(Garden):

    def __init__(self, area=0.0, number_of_flowers=0, what_is_growing=[], house_area=0):
        super().__init__(area, number_of_flowers, what_is_growing)
        self.house_area = house_area

    def has_orchard(self):
        return True

    def has_vegetable_garden(self):
        return True

    def __str__(self):
        return super().__str__() + (
            f"house area = {self.house_area},\n ")


if __name__ == "__main__":
    farmstead = Farmstead(10, 11, ["oats", "sunflower"], 12)
    print(farmstead.has_orchard())
    print(farmstead)
