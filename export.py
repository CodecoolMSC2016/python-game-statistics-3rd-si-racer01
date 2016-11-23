
# Export functions
""" export.py: for exporting the reports into a single export file.
By running this program Judy will get a single text file with all the answers she needs. """

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


def export():
    fallback_file_name = "game_stat.txt"
    file_name = input("Which file should I analyze? (default: game_stat.txt) ")
    if not file_name:
        file_name = fallback_file_name
    try:
        file_name = check_file(file_name, fallback_file_name)
    except FileNotFoundError as e:
        print("No such file. Exiting...")
    else:
        year = int(input('2. "Is there a game from a given year?" Which year? '))
        genre = input('4. "How many games do we have by genre?" Which genre? ')
        title = input('5. "What is the line number of the given game (by title)?" Which title? ')

        open("export.txt", 'w').close()  # clearing export.txt if exists or creating it if not
        with open("export.txt", 'a') as export_file:
            export_file.write("1. question: " + str(reports.count_games(file_name)) + '\n')
            export_file.write("2. question: " + str(reports.decide(file_name, year)) + '\n')
            export_file.write("3. question: " + reports.get_latest(file_name) + '\n')
            export_file.write("4. question: " + str(reports.count_by_genre(file_name, genre)) + '\n')
            export_file.write("5. question: " + str(reports.get_line_number_by_title(file_name, title)) + '\n')
            export_file.write("B-1. Sorted titles:" + '\n')
            for line in reports.sort_abc(file_name):
                export_file.write("   " + line + '\n')
            export_file.write("B-2. Genres:" + '\n')
            for line in reports.get_genres(file_name):
                export_file.write("   " + line + '\n')
            export_file.write("B-3. question: " + str(reports.when_was_top_sold_fps(file_name)) + '\n')
        print("Exported answers into export.txt")

if __name__ == "__main__":
    export()
