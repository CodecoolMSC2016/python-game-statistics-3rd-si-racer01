
# Printing functions
""" printing.py: for printing the output of the report functions. You can use this to test your solutions. """

import reports


def check_file(file_name, fallback_file_name=""):
    try:
        f = open(file_name)
    except FileNotFoundError as e:
        print(e)
        if fallback_file_name:
            check = check_file(fallback_file_name)
            print("[NOTE] Using default file")
            return check
        else:
            raise
    else:
        f.close()
        return file_name


def printing():
    fallback_file_name = "game_stat.txt"
    file_name = input("Which file should I analyze? (default: game_stat.txt) ")
    try:
        file_name = check_file(file_name, fallback_file_name)
    except FileNotFoundError as e:
        print("No such file. Exiting...")
    else:
        print("1.", reports.count_games(file_name))
        year = int(input("2. Which year? "))
        print("  ", reports.decide(file_name, year))
        print("3.", reports.get_latest(file_name))
        genre = input("4. Which genre? ")
        print("  ", reports.count_by_genre(file_name, genre))
        title = input("5. Which title? ")
        print("  ", reports.get_line_number_by_title(file_name, title))

printing()
