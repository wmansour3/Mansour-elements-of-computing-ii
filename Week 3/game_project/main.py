from characters.character import Character
from characters.warrior import Warrior
from characters.rogue import Rogue
from characters.mage import Mage
from characters.healer import Healer
from characters.archer import Archer


def battle_round(character, target):
    """
    Simulates a single round of battle between two characters.

    Args:
        character (Character): The character performing the action.
        target (Character): The target of the action.
    """
    # Display the character's information
    print("\nBefore round info:")
    print(character.display_info())
    print(target.display_info())

    print("\nAction taken:")
    # Check the character's type and perform the corresponding action
    if isinstance(character, Rogue):  # If the character is a Rogue
        print(character.sneak_attack(target))  # Perform a sneak attack
    elif isinstance(character, Archer):
        print(character.fire_arrow(target))
    elif isinstance(character, Mage):  # If the character is a Mage
        print(character.cast_spell())  # Cast a spell
    elif isinstance(character, Healer):  # If the character is a Healer
        print(character.heal(target))  # Heal the target
    elif isinstance(character, Warrior):  # If the character is a Warrior
        print(character.strength)  # Display the warrior's strength
    

    print("\nAfter round info:")
    print(character.display_info())
    print(target.display_info())

# Main game execution
if __name__ == "__main__":
    robin = Rogue("Robin", 1000, 100, 100, 10)
    wizard = Mage("Wizard", 5, 100, 10)
    hawkeye = Archer("Hawkeye", 100, 100, 5, 4)

    while hawkeye.arrows > 0: 
        battle_round(hawkeye, wizard) 
    
    battle_round(hawkeye, wizard)

    
