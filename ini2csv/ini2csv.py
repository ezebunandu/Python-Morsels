"""Program that accepts an INI-like file
and converts it to a CSV-like file."""

import csv
import sys
import configparser


def process_ini_file(input_file, output_file):
    config = configparser.ConfigParser()
    config.read(input_file)
    with open(output_file, 'wt') as f:
        writer = csv.writer(f)
        for section in config.sections():
            for key, value in config.items(section):
                row = (section,
                       key,
                       value)
                writer.writerow(row)


def main():
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    process_ini_file(input_file, output_file)


if __name__ == "__main__":
    main()
