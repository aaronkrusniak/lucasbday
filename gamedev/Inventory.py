import Item, Playsound

"""
An module for an Inventory.  These are technically static methods, because they exist outside of a class.
"""

inventory = []


def addItem(item):
    inventory.append(item)


def useItem(itemname):
    for item in inventory:
        if item.name is itemname:
            item.use()
            if item.consumable:
                inventory.remove(item)
                consumeSound = Playsound('levelup')
                # overly basic implementation
                # play a sound when used
        return
    # If this point is reached, the item with that name wasn't found.
    print "You look around for that item, but it looks like you don't actually have it.\n"


def displayInventory():
    for item in inventory:
        if item.consumable:
            print "something"
            # print out the item in RED, print the description regularly
        else:
            print "somethingelse"
            # print the item and description regularly
