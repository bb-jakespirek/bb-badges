# https://openpyxl.readthedocs.org/en/latest/
# cd /Users/jake.spirek/GitHub/badges 
# python3 format_badge_html.py 

import webbrowser
import os
os.system("clear")
print("\n ----- Begin Script ----- \n")


# Set up spreadsheet
from openpyxl import load_workbook
from openpyxl.compat import range
from openpyxl.cell import get_column_letter, column_index_from_string

# Load spreadsheet
wb = load_workbook('badge_descriptions.xlsx', guess_types=True)

# Grab the active worksheet by name
ws = wb['Working']
num_rows = len(ws.rows)
num_cols = len(ws.columns)
id_list = []
counter = 1

def findColumnIndexByTitle(title):
	for cell in ws.rows[0]:
		if cell.value == title:
			# print("Found Ticket Subject in: ", column_index_from_string(cell.column), cell.row, cell.coordinate)
			return column_index_from_string(cell.column)


def findColumnByTitle(title):
	for cell in ws.rows[0]:
		if cell.value == title:
			# print("Found Ticket Subject in: ", column_index_from_string(cell.column), cell.row, cell.coordinate)
			return cell.column


def makeIDlist(column_index):
	# Subtract 1 since we're pointing to a list that starts at 0 
	index = column_index - 1
	for cell in ws.columns[index]:
		id_list.append(cell.value)
	# Get rid of the header row
	id_list.pop(0)


def open_each_id(id_list, which_view):
	global number_to_open
	global counter
	print("\n", number_to_open, " = number to open ")
	for id in id_list:
		if str(id) == "None":
			break
		if counter < number_to_open + 1:
			url = ""
			if which_view == 2:
				url = "https://blackbaudk12.ideas.aha.io/ideas/" + str(id)
			else:
				url = "https://blackbaud.aha.io/ideas/" + str(id)
			
			# print("\n", "Ticket Id to open:", url)
			open_in_browser(url)
			counter += 1
			
			continue
		else:
			break


def open_in_browser(url):
	# Open URL in a new tab, if a browser window is already open.
	webbrowser.open_new_tab(url)
	# Open URL in new window, raising the window if possible.
	# webbrowser.open_new(url)


def write_to_textfile(thelist):
	# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
	thelist.pop(0)
	filepath = "badges.html"
	with open(filepath, 'w') as file:
		file.write('<ul class="media-list">\n')
		for index, value in enumerate(thelist):
			file.write('\t<li class="media">\n\t\t<div class="media-left">\n\t\t\t<img class="media-object" src="{}" alt="{}">\n\t\t</div>\n'.format(value, index))
			file.write('\t\t<div class="media-body">\n\t\t\t<h4 class="media-heading">{}</h4>\n\t\t</div>\n'.format(value))
			file.write('\t</li>\n')
		file.write('</ul>\n')
# for index, value in enumerate(my_list):
# 	print(index, value, "\n")
# for item in thelist:
	# thefile = open("hello.txt", "w")
	# for item in incoming_list:
	# 	thefile.write("%s\n" % item)
	# lines_of_text = ["a line of text", "another line of text", "a third line"]
	# fh.writelines(lines_of_text)
	# file.close()


def append_to_textfile():
	# http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
	fh = open("hello.txt", "a")
	lines_of_text = ["a line of text", "another line of text", "a third line"]
	fh.writelines(lines_of_text)
	fh.close()


def cycle_thru_each_row():
	for row in ws.rows:
		print(row[badge_filename_col-1].value, row[badge_type_col-1].value, row[badge_description_col-1].value)
		id_list.append(row[badge_filename_col-1].value)


# user_number = input("Which view? (1 = Admin, 2 = Front-end) ") 
# which_view = 1

# try:
# 	which_view = int(user_number)
# except:
# 	which_view = 1


# user_number = input("How many to open? ") 
# number_to_open = 0

# try:
# 	number_to_open = int(user_number)
# except:
# 	number_to_open = num_rows


# print("\n", ws.columns)


badge_filename_col = findColumnIndexByTitle("Filename")
badge_type_col = findColumnIndexByTitle("Type")
badge_description_col = findColumnIndexByTitle("Description")
print("\n", "Filename Column Index:", badge_filename_col)
# print("\n", "Column A:", ws.columns[badge_filename_col-1])
# print("\n", "Column B:", ws.columns[badge_type_col-1])

print("\n", "Row 1:", ws.rows[badge_filename_col][0].value)

cycle_thru_each_row()

# test write
write_to_textfile(id_list)
append_to_textfile()


print("this list has {} items and {} stuffs".format(len(id_list),29))

# makeIDlist(ticket_id_col)
# print(id_list)

# open_each_id(id_list,which_view)
