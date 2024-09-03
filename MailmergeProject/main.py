PLACEHOLDER = "[name]"#the variable that needs to be replaced.

with open("./input/names/invited_names.txt") as f:#opens and reads the names
     names = f.readlines()#reads the names in the list in a line.

with open("./input/letters/starting_letter.txt") as d:#opens and reads the starting letter
     letter = d.read()
     for name in names:
      stripped_name = name.strip()#removes the whitespace with \n letter
      new_name =  letter.replace(PLACEHOLDER,stripped_name)
      with open(f"./output/readytosend/letter_for_{stripped_name}.docx",mode = "w") as completed_letter:#creates if and opens writes the personalized letter file.
          completed_letter.write(new_name)
