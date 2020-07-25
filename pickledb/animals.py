import pickle


class Animal:
    energy = 0

    def __init__(self, name: str):
        self._name = name

    def feed(self):
        self.energy += 1

    def __repr__(self):
        return f"I'm {self._name} with {self.energy}% energy"


def dump_animal(animal: Animal, path: str) -> None:
    with open(path, "wb") as f:
        pickle.dump(animal, f)


def load_animal(path: str) -> Animal:
    with open(path, "rb") as f:
        return pickle.load(f)


if __name__ == "__main__":
    animal = Animal("Bobby")
    print(animal)

    animal.feed()
    print(animal)

    animals_db = "animals.dump"

    dump_animal(animal, animals_db)

    animal = load_animal(animals_db)
    print(animal)
