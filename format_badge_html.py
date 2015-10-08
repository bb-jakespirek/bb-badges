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


# for future reference, PEP8 says use "snake case" (underscores) instead of camel case for func names
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

user_number = input("Which view? (1 = Admin, 2 = Front-end) ") 
which_view = 1

try:
	which_view = int(user_number)
except:
	which_view = 1


user_number = input("How many to open? ") 
number_to_open = 0

try:
	number_to_open = int(user_number)
except:
	number_to_open = num_rows


ticket_id_col = findColumnIndexByTitle("Ideas")
# print("\n", "Ticket Id Column Index:", ticket_id_col)

makeIDlist(ticket_id_col)
# print(id_list)

open_each_id(id_list,which_view)
