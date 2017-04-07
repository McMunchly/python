# count how many of each name are in an external file

# get names from nameslist
names = {}
with open("nameslist.txt", "r") as file:

    line = file.readline()
    while line:
        line = line.strip()
        if line in names:
            names[line] = names[line] + 1
        else:
            names[line] = 1
            
        line = file.readline()

print(names)
    
# get count of categories from training_01
categories = {}

with open("Training_01.txt", "r") as newfile:

    line = newfile.readline()
    while line:
        line = line.strip()
        line = line[3:-25]
        print(line)
        if line in categories:
            categories[line] = categories[line] + 1
        else:
            categories[line] = 1

        line = newfile.readline()

print(categories)
