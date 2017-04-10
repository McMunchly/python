# create a c boilerplate

import sys
import glob

if len(sys.argv) == 1:
    print("You need to supply a filename")
    
else:
    for name in glob.glob(sys.argv[1]):
        if len(sys.argv) < 3:
            print("filename already in use. File not created")
        elif sys.argv[2] == "o":
            print(sys.argv[1], "was overwritten")

    with open(sys.argv[1], "w") as file:
        file.write("/*  */\n#include <stdio.h>\n\nint main(void)\n{\n    return 0;\n}")
