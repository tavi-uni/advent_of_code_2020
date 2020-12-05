input2 = open("input 2", "r")

final_count = 0

for line in input2:
    print(line)
    line2 = line.split()
    # 10-15 g: ggckgcgmcgjgggglgdgk
    # line2[0] == "10-15"
    pos = line2[0].split("-")
    # min_max == ["10", "15"]
    pos1 = int(pos[0])
    pos2 = int(pos[1])

    # line2[1] == "g:"
    char = line2[1]
    char = char[0]

    if (line2[2][pos1 - 1] == char) != (line2[2][pos2 - 1] == char):
        final_count = final_count + 1

print(final_count)
