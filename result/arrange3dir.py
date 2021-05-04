def arrange4(fileName):
    infile = open(fileName, "r")
    lines = infile.readlines()
    count = 1
    line_ordered = []
    arrage_part = lines[27:]
    l = len(arrage_part)
    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '001\n' and arrage_part[i+1] == '100\n' and arrage_part[i+2][:3] == '000'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '011\n' and arrage_part[i+1] == '000\n' and arrage_part[i+2][:3] == '000'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '001\n' and arrage_part[i+1] == '100\n' and arrage_part[i+2][:3] == '010'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '000\n' and arrage_part[i+1] == '100\n' and arrage_part[i+2][:3] == '100'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '011\n' and arrage_part[i+1] == '001\n' and arrage_part[i+2][:3] == '000'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '011\n' and arrage_part[i+1] == '101\n' and arrage_part[i+2][:3] == '110'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '011\n' and arrage_part[i+1] == '100\n' and arrage_part[i+2][:3] == '000'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '010\n' and arrage_part[i+1] == '100\n' and arrage_part[i+2][:3] == '100'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '011\n' and arrage_part[i+1] == '100\n' and arrage_part[i+2][:3] == '100'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '010\n' and arrage_part[i+1] == '100\n' and arrage_part[i+2][:3] == '110'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '011\n' and arrage_part[i+1] == '100\n' and arrage_part[i+2][:3] == '010'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '011\n' and arrage_part[i+1] == '101\n' and arrage_part[i+2][:3] == '000'):
            line_ordered += arrage_part[i:i+4]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '011\n' and arrage_part[i+1] == '101\n' and arrage_part[i+2][:3] == '100'):
            line_ordered += arrage_part[i:i+4]

    with open('arranged_' + fileName, 'w') as outfile:
        for line in lines[:28]:
            if line[0]=='#':
                continue
            outfile.write(line)
        for line in line_ordered:
            outfile.write(line)


fileName = input("File Name: ")
arrange4(fileName)
print("Successfully arranged!")
