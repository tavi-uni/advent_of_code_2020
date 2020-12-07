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
                byrcheck = field
                byrcheck = byrcheck.strip('byr:')
                if int(byrcheck) >= 1920:
                    if int(byrcheck) <= 2002:
                        byr = True

            if field.startswith("iyr"):
                iyrcheck = field
                iyrcheck = iyrcheck.strip('iyr:')
                if int(iyrcheck) >= 2010:
                    if int(iyrcheck) <= 2020:
                        iyr = True

            if field.startswith("eyr"):
                eyrcheck = field
                eyrcheck = eyrcheck.strip('eyr:')
                if int(eyrcheck) >= 2020:
                    if int(eyrcheck) <= 2030:
                        eyr = True

            if field.startswith("hgt"):
                hgtcheck = field
                hgtcheck = hgtcheck.strip('hgt:')
                if hgtcheck.endswith("cm"):
                    hgtcheck = hgtcheck.strip('cm')
                    if int(hgtcheck) >= 150:
                        if int(hgtcheck) <= 193:
                            hgt = True
                if hgtcheck.endswith("in"):
                    hgtcheck = hgtcheck.strip('in')
                    if int(hgtcheck) >= 59:
                        if int(hgtcheck) <= 76:
                            hgt = True

            if field.startswith("hcl"):
                hclcheck = field
                hclcheck = hclcheck.lstrip('hcl:')
                if hclcheck[0] == "#":
                    if len(hclcheck) == 7:
                        if ("0" <= hclcheck[1] <= "9") or ("a" <= hclcheck[1] <= "f"):
                            if ("0" <= hclcheck[2] <= "9") or ("a" <= hclcheck[2] <= "f"):
                                if ("0" <= hclcheck[3] <= "9") or ("a" <= hclcheck[3] <= "f"):
                                    if ("0" <= hclcheck[4] <= "9") or ("a" <= hclcheck[4] <= "f"):
                                        if ("0" <= hclcheck[5] <= "9") or ("a" <= hclcheck[5] <= "f"):
                                            if ("0" <= hclcheck[6] <= "9") or ("a" <= hclcheck[6] <= "f"):
                                                hcl = True

            if field.startswith("ecl"):
                eclcheck = field
                eclcheck = eclcheck.lstrip('ecl:')
                if eclcheck in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                    ecl = True

            if field.startswith("pid"):
                pidcheck = field
                pidcheck = pidcheck.strip('pid:')
                if len(pidcheck) == 9:
                    if "0" <= pidcheck[0] <= "9":
                        if "0" <= pidcheck[1] <= "9":
                            if "0" <= pidcheck[2] <= "9":
                                if "0" <= pidcheck[3] <= "9":
                                    if "0" <= pidcheck[4] <= "9":
                                        if "0" <= pidcheck[5] <= "9":
                                            if "0" <= pidcheck[6] <= "9":
                                                if "0" <= pidcheck[7] <= "9":
                                                    if "0" <= pidcheck[8] <= "9":
                                                        pid = True

        passport_valid = byr and iyr and eyr and hgt and hcl and ecl and pid
        if passport_valid:
            count += 1

    print(count)


passport_check()
