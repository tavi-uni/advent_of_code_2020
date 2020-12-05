def main():
    aoc = open("input 1", "r")

    aoc_list = []

    for line in aoc:
        stripped_line = line.strip('\n')
        line_int = int(stripped_line)
        aoc_list.append(line_int)

    for a in aoc_list:
        for b in aoc_list:
            for c in aoc_list:
                if a + b + c == 2020:
                    print(a * b * c)
                    return


main()
