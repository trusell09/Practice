#string concatenation (how to put strings together)

# baseballer = "and Robinson Cano"

# print("Ichiro is my favorite Basball Player " + baseballer)
# print("Ichiro is my favorite Baseball Player {}".format(baseballer))
# print(f"Ichiro is my favorite Baseball Player {baseballer}")

adj = input("Adjective: ")
noun1 = input("Food: ")
noun2 = input("Drink: ")
sport = input("Sport: ")
player = input("Favorite Player: ")

madlib = f"Sports are so {adj}! My favorite thing to eat while watching sports is {noun1} and drink is {noun2} \
my favorite sport to play growing up was {sport} and my favorite player to watch was {player}!"

print(madlib)