# compare numbers between two text files

def ReadNumbers(filename):
    with open(filename, "r") as file:
        
        nums = file.read()
        numlist = nums.split('\n')
        nums = []
    
        for string in numlist:
            nums.append(int(string))

        return nums

file1nums = ReadNumbers("happynumbers.txt")
file2nums = ReadNumbers("primenumbers.txt")

overlapping = [num for num in file1nums if num in file2nums]

print(overlapping)
