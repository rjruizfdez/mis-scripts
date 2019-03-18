#!/usr/bin/env python
import sys

fname = sys.argv[1]

def create_new_file():
	lines = open(fname).read().splitlines()
	new_file_lines = []
	count_table = 0
	
	#  while read p; do   echo 'new_file_lines.append('\'"$p"\'')'; done < a
	new_file_lines.append('<!doctype html>')
	new_file_lines.append('<html lang="en">')
	new_file_lines.append('')
	new_file_lines.append('<head>')
	new_file_lines.append('<meta charset="UTF-8">')
	new_file_lines.append('<meta name="viewport" content="width=device-width, initial-scale=1">')
	new_file_lines.append('<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css">')
	new_file_lines.append('<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>')
	new_file_lines.append('<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js"></script>')
	new_file_lines.append('')
	new_file_lines.append('</head>')
	new_file_lines.append('')
	new_file_lines.append('<body>')
	new_file_lines.append('<div class="container">')
	new_file_lines.append('')
	new_file_lines.append('')

	for l in lines:
		bold_counter = 0
		italic_counter = 0
		chars = []
		for i in range(0,len(l)):
			if l[i] == "*":
				if (i+1) < len(l): 
					if bold_counter % 2 ==0:
							if l[i+1] == "*":
								chars.append("<b>")
								bold_counter += 1	
							elif l[i-1] != "*":
								chars.append("<i>")
								bold_counter += 1	
					else:
							if l[i+1] == "*":
								chars.append("</b>")
								bold_counter += 1	
							elif l[i-1] != "*":
								chars.append("</i>")
								bold_counter += 1	
			else:
				chars.append(l[i])
		l = ''.join(chars)


		if l.startswith("#"):
			h_n = str(l.count('#'))
			l = l.replace("#","")
			new_line = "<h"+h_n+">"+l+"</h"+h_n+">"
		elif l.startswith("`"):
			if count_table % 2 == 0:
				new_line = '<input class="form-control input-lg text-center" rows="2" cols="20" style="border: none;" value="'
			else:
				new_line = '"></input><br>'
			count_table += 1
		elif l.startswith("![Screenshot]"):
			l = l.replace("![Screenshot](","")
			l = l.replace(")","")
			new_line = '<img src="'+l+'">'
		elif l.startswith("----"):
			new_line = ""
		else:
			new_line = l
	
		
		if count_table % 2 == 0:
			new_line += "<br>"
	

		new_file_lines.append(new_line)
	
	new_file_lines.append('')
	new_file_lines.append('')
	new_file_lines.append('')
	new_file_lines.append('</div>')
	new_file_lines.append('</body>')
	new_file_lines.append('</html>')

	#print '\n'.join(new_file_lines)
	open(sys.argv[2],'w').write('\n'.join(new_file_lines))

create_new_file()
