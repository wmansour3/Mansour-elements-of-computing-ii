from .warrior import Warrior

class Archer(Warrior):
    """
    Represents an Archer character, inheriting from Warrior.

    Attributes:
        name (str): The archer's name.
        level (int): The archer's level.
        health (int): The archer's current health.
        strength (int): The archer's strength.
        arrows (int): The archer's amount of arrows left.
    """
    def __init__(self, name, level, health, strength, arrows):
        """Initializes a new Archer object.
        """
        super().__init__(name, level, health, strength)

        self.arrows = arrows

    def fire_arrow(self, target):
        """
        Fires an arrow at the target, reducing their health by the archer's strength.

        Args:
            target (Character): The target of the arrow attack.

        Returns:
            str: A message describing the arrow attack.
        """
        
        if self.arrows > 0:
            self.arrows -= 1
            damage = self.strength
            target.health -= damage
            return f'{self.name} shoots an arrow at {target.name} and lowers their HP by {damage} to {target.health}. {self.name} has {self.arrows} arrows remaining.'
        else:
            return f'{self.name} does not have any more arrows available'
