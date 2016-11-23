
# Report functions
""" reports.py: write only the report functions in it. """
# Minecraft->23->2009->Survival game->Microsoft


def count_games(file_name):  # 1. How many games are in the file?
    """ Returns how many games are in the file """
    with open(file_name) as f:
        line_counter = len(f.readlines())
    return line_counter


def decide(file_name, year):  # 2. Is there a game from a given year?
    """ Returns whether there is a game from the given year """
    with open(file_name) as f:
        year_list = [int(line.split('\t')[2].strip()) for line in f]
    return year in year_list


def get_latest(file_name):  # 3. Which was the latest game?
    """ Returns the title of the latest game """
    with open(file_name) as f:
        data_list = [[data.strip() for data in line.split('\t')] for line in f]
    data_list.sort(key=lambda data: data[2], reverse=True)
    return data_list[0][0]


def count_by_genre(file_name, genre):  # 4. How many games do we have by genre?
    """ Returns how many games are with the given genre """
    with open(file_name) as f:
        # creating a list of lowercase genres,
        #   filtering out any other genres which isn't the same as the genre parameter,
        #   and counting them by replacing the values with 1 and summing them
        genre_counter = sum([1 for line in f if line.lower().split('\t')[3].strip() == str(genre).lower()])
    return genre_counter


def get_line_number_by_title(file_name, title):  # 5. What is the line number of the given game (by title)?
    """ Returns which row in the given file is the given game by title """
    with open(file_name) as f:
        data_list = [line.lower().split('\t')[0].strip() for line in f]
    return data_list.index(title.lower()) + 1


def sort_abc(file_name):  # B-1. What is the alphabetical ordered list of the titles?
    with open(file_name) as f:
        title_list = [line.split('\t')[0].strip() for line in f]
    ordered = False
    while not ordered:
        ordered = True
        for index in range(1, len(title_list)):
            if title_list[index - 1] > title_list[index]:
                title_list[index - 1], title_list[index] = title_list[index], title_list[index - 1]
                ordered = False
    return title_list
