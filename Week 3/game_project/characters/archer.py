from .warrior import Warrior

class Archer(Warrior):
    def __init__(self, name, level, health, strength, arrows):
        """Initializes a new Archer object."""
        super().__init__(name, level, health, strength)

        self.arrows = arrows

    def fire_arrow(self, target):
        if self.arrows > 0:
            self.arrows -= 1
            damage = self.strength
            target.health -= damage
            return f'{self.name} shoots an arrow at {target.name} and lowers their HP by {damage} to {target.health}. {self.name} has {self.arrows} arrows remaining.'
        else:
            return f'{self.name} does not have any more arrows available'
