
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
        title = input('6. "What properties has a game?" Which game? ')

        open("export.txt", 'w').close()  # clearing export.txt if exists or creating it if not
        with open("export.txt", 'a') as export_file:
            export_file.write("1. What is the title of the most played game? " +
                              reports.get_most_played(file_name) + '\n')
            export_file.write("2. How many copies have been sold total? " +
                              str(reports.sum_sold(file_name)) + '\n')
            export_file.write("3. What is the average selling? " +
                              str(reports.get_selling_avg(file_name)) + '\n')
            export_file.write("4. How many characters long is the longest title? " +
                              str(reports.count_longest_title(file_name)) + '\n')
            export_file.write("5. What is the average of the release dates? " +
                              str(reports.get_date_avg(file_name)) + '\n')
            export_file.write("6. What properties has %s?" % title + '\n')
            export_file.write("    Name: " + reports.get_game(file_name, title)[0] + '\n')
            export_file.write("    Million sold: " + str(reports.get_game(file_name, title)[1]) + '\n')
            export_file.write("    Release date: " + str(reports.get_game(file_name, title)[2]) + '\n')
            export_file.write("    Genre: " + reports.get_game(file_name, title)[3] + '\n')
            export_file.write("    Publisher: " + reports.get_game(file_name, title)[4] + '\n')
            export_file.write("B-1. How many games are there grouped by genre?" + '\n')
            count_by_genre = reports.count_grouped_by_genre(file_name)
            for key in count_by_genre:
                export_file.write("    " + str(count_by_genre[key]) + " " + key + '\n')
            del count_by_genre
            export_file.write("B-2. What is the date ordered list of the games?" + '\n')
            titles_ordered_by_date = reports.get_date_ordered(file_name)
            for title in titles_ordered_by_date:
                export_file.write("    " + title + '\n')
        print("Exported answers into export.txt")

if __name__ == "__main__":
    export()
