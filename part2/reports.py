
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
    with open(file_name) as f:
        max_title_length = max([len(line.split('\t')[0].strip()) for line in f])
    return max_title_length


def get_date_avg(file_name):  # 5. What is the average of the release dates?
    with open(file_name) as f:
        release_list = [int(line.split('\t')[2].strip()) for line in f]
    avg_year = round(sum(release_list) / len(release_list))
    return avg_year


def get_game(file_name, title):  # 6. What properties has a game?
    with open(file_name) as f:
        for line in f:
            current_game = [data.strip() for data in line.split('\t')]
            if current_game[0].lower() == title.strip().lower():
                return [current_game[0], float(current_game[1]), int(current_game[2]), current_game[3], current_game[4]]
    return []


def count_grouped_by_genre(file_name):  # B-1. How many games are there grouped by genre?
    count_by_genre = dict()
    with open(file_name) as f:
        for line in f:
            current_game = [data.strip() for data in line.split('\t')]
            if current_game[3] in count_by_genre:
                count_by_genre[current_game[3]] += 1
            else:
                count_by_genre[current_game[3]] = 1
    return count_by_genre


def get_date_ordered(file_name):  # B-2. What is the date ordered list of the games?
    with open(file_name) as f:
        data_list = [(line.split('\t')[0].strip(), line.split('\t')[2].strip()) for line in f]
    data_list.sort(key=lambda game: game[0])
    data_list.sort(key=lambda game: game[1], reverse=True)
    return [game[0] for game in data_list]
    # Expected output of the function: the date ordered list of the titles (list of string)
    # Other expectation: The secondary ordering rule is the alphabetical ordering of the titles.
    #   So if there are titles from the same year, you need to order them alphabetically in ascending order.
