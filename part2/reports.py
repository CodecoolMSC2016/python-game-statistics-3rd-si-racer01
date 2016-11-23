
# Report functions
""" reports.py: write only the report functions in it. """
# Minecraft->23->2009->Survival game->Microsoft


def get_most_played(file_name):  # 1. What is the title of the most played game?
    with open(file_name) as f:
        most_played_list = [(line.split('\t')[0].strip(), float(line.split('\t')[1].strip())) for line in f]
    most_played_list.sort(key=lambda game: game[1], reverse=True)
    return most_played_list[0][0]


def sum_sold(file_name):  # 2. How many copies have been sold total?
    with open(file_name) as f:
        total_sold = sum([float(line.split('\t')[1].strip()) for line in f])
    return total_sold


def get_selling_avg(file_name):  # 3. What is the average selling?
    with open(file_name) as f:
        selling_list = [float(line.split('\t')[1].strip()) for line in f]
    avg_selling = sum(selling_list) / len(selling_list)
    return avg_selling


def count_longest_title(file_name):  # 4. How many characters long is the longest title?
    return int()


def get_date_avg(file_name):  # 5. What is the average of the release dates?
    return int(avg_year)
    # Other expectation: the return value must be the rounded up average


def get_game(file_name, title):  # 6. What properties has a game?
    pass
    # Expected output of the function: a list of all the properties of the game (a list of various type).
