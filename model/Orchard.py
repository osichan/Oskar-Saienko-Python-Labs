from model.Garden import Garden


class Orchard(Garden):

    def __init__(self, area=0.0, number_of_flowers=0, number_of_pods=0, ):
        super().__init__(area, number_of_flowers)
        self.number_of_pods = number_of_pods

    def has_orchard(self):
        return True

    def has_vegetable_garden(self):
        return False

    def __str__(self):
        return super().__str__() + (
            f"number of pods = {self.number_of_pods},\n ")


if __name__ == "__main__":
    orchard = Orchard(10, 11, 12)
    print(orchard.has_orchard())
    print(orchard)
