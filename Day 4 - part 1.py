def passport_check():
    passport_open = open("input 4", "r")

    count = 0

    passports = passport_open.read()
    passports = passports.split("\n\n")
    for passport in passports:
        fields = passport.split()
        byr = False
        iyr = False
        eyr = False
        hgt = False
        hcl = False
        ecl = False
        pid = False

        for field in fields:
            if field.startswith("byr"):
                byr = True
            if field.startswith("iyr"):
                iyr = True
            if field.startswith("eyr"):
                eyr = True
            if field.startswith("hgt"):
                hgt = True
            if field.startswith("hcl"):
                hcl = True
            if field.startswith("ecl"):
                ecl = True
            if field.startswith("pid"):
                pid = True

        passport_valid = byr and iyr and eyr and hgt and hcl and ecl and pid
        if passport_valid:
            count += 1

    print(count)

passport_check()
