inventory = {
    'gold': 500,
    'pouch': ['flint','twine','gemstone'],
    'backpack': ['xylophone','dagger','bedroll','bread loaf']
}

# inventory["pocket"] = [ 'seashell', 'strange berry','lint']
# print(inventory)
key = "pocket"
value = ['seashell', 'strange berry','lint']
inventory[key]=value
print(inventory)

inventory["backpack"].remove("dagger")
print(inventory)

inventory["gold"] += 50
print(inventory)
