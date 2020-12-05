def calculate_trees(right, down):
    mapy = open("input 3", "r")

    trees = 0
    for line_number, line in enumerate(mapy):
        modeven = (line_number + 1) % down
        if modeven == 0:
            line = line.strip('\n')
            count = line_number * right
            mod = count % len(line)
            if line[mod] == "#":
                trees += 1

    return trees


all_trees = calculate_trees(3, 1)

print(all_trees)
