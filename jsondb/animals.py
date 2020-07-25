import json


class Animal:
    energy = 0

    def __init__(self, name: str):
        self._name = name

    def feed(self):
        self.energy += 1

    def as_dict(self) -> dict:
        return {
            "name": self._name,
            "energy": self.energy
        }

    @staticmethod
    def from_dict(animal_dict: dict) -> "Animal":
        name = animal_dict["name"]
        energy = animal_dict["energy"]

        animal = Animal(name)
        animal.energy = energy
        return animal

    def __repr__(self):
        return f"I'm {self._name} with {self.energy}% energy"


def dump_animal(animal: Animal, path: str) -> None:
    with open(path, "w") as f:
        json.dump(animal.as_dict(), f)


def load_animal(path: str) -> Animal:
    with open(path, "rb") as f:
        animal_dict = json.load(f)
        return Animal.from_dict(animal_dict)


if __name__ == "__main__":
    bobby = Animal("Bobby")
    bobby.feed()
    print(bobby, id(bobby))

    animals_db = "animals.json"

    dump_animal(bobby, animals_db)

    bobby_clone = load_animal(animals_db)
    print(bobby_clone, id(bobby_clone))
