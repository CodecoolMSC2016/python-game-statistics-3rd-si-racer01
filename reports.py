
# Report functions
""" reports.py: write only the report functions in it. """


def count_games(file_name):  # 1. How many games are in the file?
    """ Returns how many games are in the file """
    line_counter = 0
    with open(file_name) as f:
        line_counter = len(f.readlines())
    return line_counter


def decide(file_name, year):  # 2. Is there a game from a given year?
    """ Returns whether there is a game from the given year """
    with open(file_name) as f:
        year_list = [int(line.strip().split('\t')[2]) for line in f]
    return year in year_list
