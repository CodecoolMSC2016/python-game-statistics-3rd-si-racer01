
# Report functions
""" reports.py: write only the report functions in it. """


def count_games(file_name):  # 1. How many games are in the file?
    """ Returns how many games are in the file """
    line_counter = 0
    with open(file_name) as f:
        line_counter = len(f.readlines())
    return line_counter
