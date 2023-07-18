class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

        Zoo.__animals += 1

    def get_info(self, species):
        output = ''
        if species == 'mammal':
            output += f"Mammals in {self.zoo_name}: {', '.join(self.mammals)}\n"
        elif species == 'fish':
            output += f"Fishes in {self.zoo_name}: {', '.join(self.fishes)}\n"
        elif species == 'bird':
            output += f"Birds in {self.zoo_name}: {', '.join(self.birds)}\n"

        output += f"Total animals: {Zoo.__animals}"
        return output


name_of_zoo = input()
current_zoo = Zoo(name_of_zoo)
new_animals = int(input())

for i in range(new_animals):
    current_species, current_name = input().split()
    current_zoo.add_animal(current_species, current_name)

detail_species = input()

print(current_zoo.get_info(detail_species))

