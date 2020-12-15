import re

with open('day7input') as f:
    lines = f.readlines()

# Part One
# Set up the rules dict rules[color]= containing colors

rules = {}

primary_color_pattern = "([a-z]+ [a-z]+)"
contains_pattern = ("\d ([a-z]+ [a-z]+)")

for rule in lines:
    color_primary = re.match(primary_color_pattern, rule).group(1)
    contains = re.findall(contains_pattern, rule)
    rules[color_primary] = contains

# recursive function that returns true if color == shiny gold or any child of color == shiny gold
def shiny_gold(color):
    if color == "shiny gold":
        return True
    else:
        return any(shiny_gold(child) for child in rules[color])

# sums all true occurrences of shiny_gold() - 1 because we don't want the color itself
print("Sum of all Bags directly or indirectly containing a shiny gold bag: ",
      sum(shiny_gold(color) for color in rules.keys()) - 1)

# Part Two
