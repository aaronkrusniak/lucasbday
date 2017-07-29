"""
An object class for items.
"""


class Item(object):

    """
    If the Inventory is opened in the overworld, items are printed with descriptions below.  Consumables will be printed in a different color.
    Base Power represents either the base damage a weapon can yield (modified by the defense of an enemy), or, in the case of a consumable,
    the amount it will heal the player.
    """
    def __init__(self, name, description, base_pwr, inventory, consumable = False):
        self.name = name
        self.description = description
        self.pwr = base_pwr
        self.consumable = consumable
        inventory.add(self)


"""
Idea - make the item useable or not useable depending on an overall game state that is checked when player attempts to use an item
"""