import random

restaurants = ["Sticks", "Yuan Ho", "Melting Pot", "East Garden"]
styles = ["Casual", "Chinese", "Fancy", "Chinese"]
costs = ["$", "$", "$$$", "$$"]

def get_random_restaurant():
    return random.choice(restaurants)

def get_restaurant_style(chosen_style):
    ans = get_random_restaurant()
    while styles[restaurants.index(ans)] != chosen_style:
        ans = get_random_restaurant()
    return ans, chosen_style, costs[restaurants.index(ans)]

def get_restaurant_cost(chosen_cost):
    indices = []
    for index in range(len(costs)):
        if styles[index] == chosen_cost:
            indices.append(index)
    index = random.choice(indices)
    r = restaurants[index]
    s = styles[index]
    c = costs[index]
    return r, s, c


print("Welcome to WahooSpoon!")
print("  1. Get a random restaurant")
print("  2. Get a random restaurant based on style")
print("  3. Get a random restaurant based on cost")
choice = int(input("Choice? "))
if choice == 1:
    r, s, c = get_random_restaurant()
elif choice == 2:
    print(set(styles))
    style = input("What style would you like?: ")
    r, s, c = get_restaurant_style(style)
else:
    print(set(costs))
    cost = input("What cost would you like?: ")
    r, s, c = get_restaurant_cost(cost)

print("We're going to", r, "today! (Style:", s, "/ Cost:", c, ")")
