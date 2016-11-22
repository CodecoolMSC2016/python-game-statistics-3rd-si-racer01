
# Report functions
""" reports.py: write only the report functions in it. """


def count_games(file_name):  # 1. How many games are in the file?
    """ Returns how many games are in the file """
    with open(file_name) as f:
        data_list = [line.strip().split('\t') for line in f]
    return len(data_list)
