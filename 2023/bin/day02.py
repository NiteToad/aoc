import sys
from collections import defaultdict

file = open(sys.argv[1]).read().strip()
possible_outcomes = 0
minimum_sum = 0
game_max = { "red": 12, "green": 13,  "blue" : 14 }
for line in file.split("\n"):
    is_valid = True
    id_, game = line.split(":")
    value_dict = defaultdict(int)
    for section in game.split(";"):
        print(f"Set: {section}")
        for pair in section.split(","):
            number, color = pair.split()
            number = int(number)
            value_dict[color] = max(value_dict[color], number)
            if int(number) > game_max.get(color, 0):
                is_valid = False 
    game_number = 1
    for val in value_dict.values():
        game_number *= val
    minimum_sum += game_number
    if is_valid:
        possible_outcomes += int(id_.split()[-1])
print(f"The sum of the IDs with possible outcomes is: {possible_outcomes}")
print(f"The minimum set of cubes that must be present is: {minimum_sum}")
