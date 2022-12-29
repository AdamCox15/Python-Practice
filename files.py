with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

with open("how_many_lines.txt") as lines_doc:
  for line in lines_doc.readlines():
    print(line)
    
