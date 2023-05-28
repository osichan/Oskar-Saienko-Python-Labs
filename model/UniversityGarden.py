from model.Garden import Garden


class UniversityGarden (Garden):

    def __init__(self, area=0.0, number_of_flowers=0, number_of_sculptures=0,):
        super().__init__(area, number_of_flowers)
        self.number_of_sculptures = number_of_sculptures

    def has_orchard(self):
        return False

    def has_vegetable_garden(self):
        return False

    def __str__(self):
        return super().__str__() + (
            f"number of sculptures = {self.number_of_sculptures},\n ")


if __name__ == "__main__":
    university_garden  = UniversityGarden (10, 11, 12)
    print(university_garden.has_orchard())
    print(university_garden)