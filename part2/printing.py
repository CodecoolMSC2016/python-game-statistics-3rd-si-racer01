
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
    if not file_name:
        file_name = fallback_file_name
    try:
        file_name = check_file(file_name, fallback_file_name)
    except FileNotFoundError as e:
        print("No such file. Exiting...")
    else:
        print("1.", reports.get_most_played(file_name))
        print("2.", reports.sum_sold(file_name))
        print("2.", reports.get_selling_avg(file_name))
        print("2.", reports.count_longest_title(file_name))

if __name__ == "__main__":
    printing()
