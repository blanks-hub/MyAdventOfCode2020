import re

f = open('day4input')
f = [line for line in f]
fstring = ""
for line in f:
    fstring += line
passports = fstring.split('\n\n')

validctr = 0
validlist = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# Part Two
def validate_field(key, val):
    def _hgt_check(val):
        return (
                ("cm" in val and 150 <= int(val.replace("cm", "")) <= 193) or
                ("in" in val and 59 <= int(val.replace("in", "")) <= 76)
        )

    rules = {
        "byr": lambda x: 1920 <= int(x) <= 2002,
        "cid": lambda x: True,
        "ecl": lambda x: x in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
        "eyr": lambda x: 2020 <= int(x) <= 2030,
        "hcl": lambda x: bool(re.match(r"^#[a-fA-F0-9]{6}$", x)),
        "hgt": _hgt_check,
        "iyr": lambda x: 2010 <= int(x) <= 2020,
        "pid": lambda x: bool(re.match(r"^[0-9]{9}$", x)),
    }
    return key in rules.keys() and rules[key](val)


pattern = '(([a-z]+):([^ \n]+))+'
for passport in passports:
    matches = re.findall(pattern, passport)
    keylist = list()
    for match in matches:
        key = match[1]
        val = match[2]
        if validate_field(key, val): # needed for Part Two
            keylist.append(key)

    checklist = [i for i in validlist if i not in keylist]
    print(checklist)
    if not checklist:
        validctr += 1
        print("Valid\n")
    else:
        print("Not valid\n")

print(validctr)
