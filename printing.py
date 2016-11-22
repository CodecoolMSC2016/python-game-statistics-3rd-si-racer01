
# Printing functions
""" printing.py: for printing the output of the report functions. You can use this to test your solutions. """

import reports

file_name = "game_stat.txt"
year = 2009

print("1.", reports.count_games(file_name))
print("  ", reports.decide(file_name, int(input("2. Which year? "))))
