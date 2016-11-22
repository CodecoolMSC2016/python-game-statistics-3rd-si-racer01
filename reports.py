
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


def get_latest(file_name):  # 3. Which was the latest game?
    data_list = []
    with open(file_name) as f:
        data_list = [line.strip().split('\t') for line in f]
    data_list.sort(key=lambda data: data[2], reverse=True)
    return data_list[0][0]
