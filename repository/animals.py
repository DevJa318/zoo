import json
import os


class Animal:

    def __init__(self, name: str, energy: float = 0.0):
        self._name = name
        self._energy = energy

    @property
    def name(self) -> str:
        return self._name

    @property
    def energy() -> float:
        return self._energy

    def feed(self):
        self.energy += 1

    def __repr__(self):
        return f"I'm {self._name} with {self.energy}% energy"


class AnimalsRepository:

    def __init__(self, repository_path: str):
        self._repository = repository_path

    def append(self, animal: Animal) -> None:
        if os.path.exists(self._repository):
            animals_list = self.get_all()
            animals_list.append(animal)
            self._append_all(animals_list)
        else:
            with open(self._repository, "w") as f:
                animal_dict = {
                    "name": animal.name,
                    "energy": animal.energy
                }
                json.dump([animal_dict], f)

    def get_all(self) -> [Animal]:
        if not os.path.exists(self._repository):
            return []
        with open(self._repository, "r") as f:
            return json.load(f)

    def _append_all(self, animals: [Animal]) -> None:
        animals_dict = [
            {
                "name": animal.name,
                "energy": animal.energy
            }
            for animal in animals
        ]
        with open(self._repository, "w") as f:
            json.dump(animals_dict, f)


if __name__ == "__main__":
    zoo = AnimalsRepository(repository_path="animals_db.json")
    zoo.append(Animal(name="Bobby"))

    print(zoo.get_all())
