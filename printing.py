
# Printing functions
""" printing.py: for printing the output of the report functions. You can use this to test your solutions. """

import reports

file_name = "game_stat.txt"
year = 2009

print("1.", reports.count_games(file_name))
year = int(input("2. Which year? "))
print("  ", reports.decide(file_name, year))
print("3.", reports.get_latest(file_name))
