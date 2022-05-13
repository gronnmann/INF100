def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(f"{v} {k}")
        item_total += v
    return item_total


def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)

        inventory[item] += 1

    return inventory


inv = {"egg": 42, "apple": 1}
dragonLoot = ["banana", "banana", "ruby", "apple"]

print(addToInventory(inv, dragonLoot))