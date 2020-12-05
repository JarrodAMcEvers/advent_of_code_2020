import re
with open('./input.txt', 'r') as f:
    lines = f.read()

class Passport():
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    year_regex = r'^\d{4}$'
    height_regex = r'^(\d{2,3})(cm|in)$'
    hair_color_regex = r'^#[a-f|\d]{6}$'
    passport_id_regex = r'^[0-9]{9}$'

    def __init__(self, key_values: str):
        self.dictionary = {}
        regex = re.compile(r'([a-z]{3}):(\S+)')
        for key, value in regex.findall(key_values):
            self.dictionary[key] = value

    def is_valid(self):
        if len(self.dictionary) < len(self.required_fields):
            return False
        for field in self.required_fields:
            if self.dictionary.get(field, None) == None:
                return False

        for year_field in ['byr', 'iyr', 'eyr']:
            if not re.match(self.year_regex, self.dictionary.get(year_field, '')):
                return False

        if not 1920 <= int(self.dictionary.get('byr')) <= 2002:
            return False
        if not 2010 <= int(self.dictionary.get('iyr')) <= 2020:
            return False
        if not 2020 <= int(self.dictionary.get('eyr')) <= 2030:
            return False

        hgt = self.dictionary.get('hgt', '')
        if not re.match(self.height_regex, hgt):
            return False

        height = int(hgt[:-2])
        unit = hgt[::-1][:2][::-1]
        if unit == 'cm' and not 150 <= height <= 193:
            return False
        if unit == "in" and not 59 <= height <= 76:
            return False

        if self.dictionary.get('ecl', '') not in self.eye_colors:
            return False

        if not re.match(self.hair_color_regex, self.dictionary.get('hcl', '')):
            return False
        if not re.match(self.passport_id_regex, self.dictionary.get('pid', '')):
            return False

        return True


required_fields = ['byr', 'ecl', 'eyr', 'hcl', 'hgt', 'iyr', 'pid']
passports = lines.split('\n\n')
def part1():
    valid_count = 0
    for passport in passports:
        passport = passport.replace('\n', ' ')
        passport_fields = [ key_value.split(':')[0] for key_value in passport.split(' ') ]
        field_count = 0
        for field in passport_fields:
            if field == 'byr' or field == 'ecl' or field == 'eyr' or field == 'hcl' or field == 'hgt' or field == 'iyr' or field == 'pid':
                field_count += 1
        if field_count == 7:
            valid_count += 1

    return valid_count

def part2():
    valid_count = 0
    for passport in passports:
        passport = passport.replace('\n', ' ')
        if Passport(passport).is_valid():
            valid_count += 1

    return valid_count


print(part1(), 'valid passports out of', len(passports))
print(part2(), 'valid passports out of', len(passports))