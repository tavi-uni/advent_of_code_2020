input2 = open("input 2", "r")

final_count = 0

for line in input2:
    print(line)
    line2 = line.split()
    # 10-15 g: ggckgcgmcgjgggglgdgk
    # line2[0] == "10-15"
    min_max = line2[0].split("-")
    # min_max == ["10", "15"]
    min = int(min_max[0])
    max = int(min_max[1])

    # line2[1] == "g:"
    char = line2[1]
    char = char[0]

    count = 0

    for letter in line2[2]:
        if letter == char:
            count = count + 1

    if count >= min and count <= max:
        final_count = final_count + 1

print(final_count)
