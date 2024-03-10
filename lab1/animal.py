class Animal:
    def __init__(self, name, species, animal_type):
        self.name = name
        self.species = species
        self.animal_type = animal_type

    def __str__(self):
        return f"{self.name} - {self.species} ({self.animal_type})"
