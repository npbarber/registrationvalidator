#!/usr/bin/python

# Assumptions made:
# Report format has:
# Division Name in field 1
# Gender is the last field
# Date Of Birth is the next-to-last field

import argparse

GENDER_MAP = {
    'Male': 'B',
    'Female': 'G'
}


def parse_args():
    parser = argparse.ArgumentParser(description='problematic registration detector type thing')
    parser.add_argument('--reportfile', required=True,
                        help='csv report exported from rms')
    return parser.parse_args()


def age_division_ok(div, dob):
    year_born = dob.split('/')[-1]
    return year_born in div


def gender_division_ok(div, gender):
    gender_id = GENDER_MAP[gender]
    return 'U-%s' % gender_id in div


def spit(age_anomolies, gender_anomolies):
    print('\n\nA G E   A N O M O L I E S')
    print('=========================')
    for a in age_anomolies:
        print a

    print('\n\nG E N D E R   A N O M O L I E S')
    print('=========================')
    for a in gender_anomolies:
        print a


def main(args):

    age_anomolies = []
    gender_anomolies = []
    with open(args.reportfile) as h:
        for line in h:
            parts = line.split('","')
            div = parts[1]
            dob = parts[-2]
            gender = parts[-1].strip('\r\n"')

            if 'Division Name' in div:
                continue
            if 'Schoolyard' in div:
                continue
            if 'VIP' in div:
                continue


            if not age_division_ok(div, dob):
                age_anomolies.append(line)

            if not gender_division_ok(div, gender):
                gender_anomolies.append(line)
    spit(age_anomolies, gender_anomolies)

if __name__ == '__main__':
    args = parse_args()
    main(args)
