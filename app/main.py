class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        Animal.alive.append(self)

    def __repr__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, "
            f"Hidden: {self.hidden}}}")

    def change_health(self, amount: int) -> None:
        self.health += amount
        if self.health <= 0:
            self.die()

    def die(self) -> None:
        self.health = 0
        if self in Animal.alive:
            Animal.alive.remove(self)


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    def bite(self, target: Animal) -> None:
        if isinstance(target, Carnivore):
            return "Can't bite another carnivore"
        if target.hidden:
            return "Cant't bite hidden target"
        target.change_health(-50)
