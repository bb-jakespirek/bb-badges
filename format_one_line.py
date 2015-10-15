#!/usr/bin/python

# cd /Users/jake.spirek/GitHub/badges
# python3 format_one_line.py 
import re

file_to_convert = "html_to_convert.txt"
file_converted = "html_one_line.txt"
lines = []

def read_file(filepath):
	# with open(filepath) as file:
	# 	content = file.readlines()
	# 	for item in content:
	# 		print(item)
	content = open(filepath, "r")
	print("Name of the file: ", content.name)
	# line = content.readline()
	
	for index, item in enumerate(content):
		tabs = re.sub(r'\t', '\\\\t',item)
		newlines = re.sub(r'\n', '\\\\n',tabs)
		returns = re.sub(r'\r', '\\\\r',newlines)
		print("Read Line {}: {}".format(index, item)) 
		print("Replaced Line {}: {}".format(index, returns)) 
		lines.append(returns)





def write_file(filepath):
	with open(filepath, 'w') as file:
		joined_lines = ''.join(lines)
		file.write(joined_lines)
		print(joined_lines)
			# file.write('<ul class="media-list">\n')
			# for index, item in enumerate(lines):

			# 	file.write('\t<li class="media">\n\t\t<div class="media-left">\n\t\t\t<img class="media-object" src="http://static.smallworldlabs.com/blackbaud/content/icons/badges/{}/{}" alt="{}">\n\t\t</div>\n'.format(item[badge_type_col].value.lower(), item[badge_filename_col].value, index))
			# 	file.write('\t\t<div class="media-body">\n\t\t\t<h4 class="media-heading">{}</h4>\n\t\t<p>{}</p></div>\n'.format(item[badge_heading_col].value, item[badge_description_col].value))
			# 	file.write('\t</li>\n')
			# file.write('</ul>\n')


read_file(file_to_convert)

write_file(file_converted)