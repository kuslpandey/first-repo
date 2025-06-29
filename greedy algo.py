__author__ = "8241115, Hartung, 8329002, Pandey"

matrix1 = [[1, 5, 3],
           [- 4, 8, 6],
           [-10, - 8, 9]]

matrix2 = [[1, 3, 4, 6, 1],
           [1, 3, 4, 6, 1],
           [1, 3, 4, 6, 1],
           [1, 3, 4, 6, 1],
           [1, 3, 4, 6, 1]]

# matrix[i][j] --> i = rows, j = columns
# cooridnates: (i, j) --> (row, columns)

def matrix_way(matrix):
    n = len(matrix)
    # List of visited fields, starting with field(0, 0)
    visited_fields = [(0, 0)]
    (i, j) = (0, 0)
    coord = (i, j)
    # Sum of values in the way, starting with the value of
    # the starting field
    sum_of_way = matrix[0][0]
    

    while True:
        adjacent_fields = dict()
        # Check, whether our current position is on any edges
        first_row = False
        last_row = False
        first_column = False
        last_column = False
        if coord[0] == 0:
            first_row = True
        if coord[0] == n - 1:
            last_row = True
        if coord[1] == 0:
            first_column = True
        if coord[1] == n - 1:
            last_column = True
        # Add the element to the left of our currrent position
        if first_column == False and (i, j - 1) not in visited_fields:
            adjacent_fields.update({(i, j - 1): matrix[i][j - 1]})
        # Add the element to the right of our currrent position
        if last_column == False and (i, j + 1) not in visited_fields:
            adjacent_fields.update({(i, j + 1): matrix[i][j + 1]})
        # Add the element above our currrent position
        if first_row == False and (i - 1, j) not in visited_fields:
            adjacent_fields.update({(i - 1, j): matrix[i - 1][j]})
        # Add the element below our currrent position
        if last_row == False and (i + 1, j) not in visited_fields:
            adjacent_fields.update({(i + 1, j): matrix[i + 1][j]})
        # Get the coordinates of the adjacent field with the lowest value
        if len(adjacent_fields) > 0:
            lowest_value_coord = min(adjacent_fields, key = adjacent_fields.get)
            sum_of_way = sum_of_way + adjacent_fields[lowest_value_coord]
            (i, j) = lowest_value_coord
            coord = (i, j)
            visited_fields.append(lowest_value_coord)
        if (i, j) == (n-1, n-1) or len(adjacent_fields) == 0:
            return (visited_fields, sum_of_way)


def globally_best_way(matrix, i, j, visited_fields):
    possible_ways = []
    n = len(matrix)


    # What happens, if goal is reached
    if (i, j) == (n - 1, n - 1):
        sum_of_way = 0
        possible_ways.append((visited_fields))
        for way in possible_ways:
            for field in way:
                sum_of_way += matrix[field[0]][field[1]]
            way.append(sum_of_way)
        return possible_ways

    adjacent_fields = []

    # Check upper neighbor
    if i > 0:
        adjacent_fields.append((i - 1, j))

    # Check lower neighbor
    if i < n - 1:
        adjacent_fields.append((i + 1, j))

    # Check left neighbor
    if j > 0:
        adjacent_fields.append((i, j - 1))

    # Check right neighbor
    if j < n - 1:
        adjacent_fields.append((i, j + 1))

    # adjacent_fields = [(0, 1), (1, 0)]

    for field in adjacent_fields:
        if field not in visited_fields:
            new_visited_fields = visited_fields.copy()
            new_visited_fields.append(field)
            possible_ways.extend(globally_best_way
                                 (matrix, field[0], field[1], new_visited_fields))

    
    return possible_ways


(visited_fields, sum_of_way) = matrix_way(matrix1)

print("Der Greedy Weg ist:", visited_fields)
print("Dieser Weg kostet:", sum_of_way)

  
possible_ways = (globally_best_way(matrix1, 0, 0, [(0, 0)]))
costs = []
for way in possible_ways:
    costs.append(way[-1])
best_way_index = costs.index(min(costs))
best_way = possible_ways[best_way_index]
best_cost = best_way[-1]

print(possible_ways)
print("Der beste Weg ist:", best_way)
print("Dieser Weg kostet:", best_cost)
