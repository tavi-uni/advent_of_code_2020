def main():
    aoc = open("input 1", "r")

    aoclist = []

    for line in aoc:
        stripped_line = line.strip('\n')
        line_int = int(stripped_line)
        aoclist.append(line_int)

    for a in aoclist:
        for b in aoclist:
            if a + b == 2020:
                print(a * b)
                return

main()


