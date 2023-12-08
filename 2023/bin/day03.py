import sys

file = open(sys.argv[1]).read().strip()
total_parts_sum = 0
total_gear_ratio_sum = 0

grid = [list(line) for line in file.split("\n")]

# Function to get the number at a given position
def get_number_at(grid, x, y):
    # Check if the current position is a digit
    if not grid[x][y].isdigit():
        return None

    # move left to find the start of the number
    start_y = y
    while start_y > 0 and grid[x][start_y - 1].isdigit():
        start_y -= 1

    # Construct the number from the start to end
    number = int(grid[x][start_y])
    new_y = start_y + 1
    while new_y < len(grid[0]) and grid[x][new_y].isdigit():
        number = number * 10 + int(grid[x][new_y])
        new_y += 1

    return number

# Function to find adjacent numbers for a gear
def find_adjacent_numbers_for_gear(grid, x, y):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    found_numbers = set()
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            number = get_number_at(grid, nx, ny)
            if number is not None:
                found_numbers.add(number)
    return list(found_numbers)

# Iterate through the grid
for x in range(len(grid)):
    for y in range(len(grid[0])):
        if grid[x][y].isdigit():
            number = int(grid[x][y])
            if y > 0 and grid[x][y-1].isdigit():
                continue  # Skip this number as it's not the start of the multi-digit number

            new_y = y + 1
            while new_y < len(grid[0]) and grid[x][new_y].isdigit():
                number = number * 10 + int(grid[x][new_y])
                new_y += 1

            adjacent_to_symbol = False
            for check_y in range(y, new_y):
                directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
                for dir_x, dir_y in directions:
                    nx, ny = x + dir_x, check_y + dir_y
                    if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and not grid[nx][ny].isdigit() and grid[nx][ny] not in ['.', ' ']:
                        adjacent_to_symbol = True
                        break
                if adjacent_to_symbol:
                    break

            if adjacent_to_symbol:
                total_parts_sum += number

        # Check for gears and calculate gear ratios
        if grid[x][y] == '*':
            adjacent_numbers = find_adjacent_numbers_for_gear(grid, x, y)
            if len(adjacent_numbers) == 2:
                total_gear_ratio_sum += adjacent_numbers[0] * adjacent_numbers[1]

print(f"Total Parts Sum: {total_parts_sum}")
print(f"Total Gear Ratio Sum: {total_gear_ratio_sum}")

# testing
number_at_8_7 = get_number_at(grid, 8, 7)
number_at_8_8 = get_number_at(grid, 8, 8)

print(f"Number at coordinate (8,7): {number_at_8_7}")
print(f"Number at coordinate (8,8): {number_at_8_8}")
