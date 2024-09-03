with open("text.txt",mode = "w") as f:
  f.write("hello pycharm!!its python virtual environment day")

with open("text.txt",mode = "a") as f:
    f.write("\n pycharm IDE ")

with open("text.txt") as f:
        content = f.read()
        print(content)