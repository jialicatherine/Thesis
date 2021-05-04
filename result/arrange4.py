def arrange4(fileName):
    infile = open(fileName, "r")
    lines = infile.readlines()
    count = 1
    line_ordered = []
    arrage_part = lines[27:]
    l = len(arrage_part)
    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '0110\n' and arrage_part[i+1] == '1001\n' and arrage_part[i+2] == '1000\n' and arrage_part[i+3][:4] == '0100'):
            line_ordered += arrage_part[i:i+5]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '0111\n' and arrage_part[i+1] == '1000\n' and arrage_part[i+2] == '1000\n' and arrage_part[i+3][:4] == '1000'):
            line_ordered += arrage_part[i:i+5]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '0110\n' and arrage_part[i+1] == '1001\n' and arrage_part[i+2] == '1001\n' and arrage_part[i+3][:4] == '0110'):
            line_ordered += arrage_part[i:i+5]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '0111\n' and arrage_part[i+1] == '1010\n' and arrage_part[i+2] == '1100\n' and arrage_part[i+3][:4] == '1000'):
            line_ordered += arrage_part[i:i+5]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '0111\n' and arrage_part[i+1] == '1011\n' and arrage_part[i+2] == '1100\n' and arrage_part[i+3][:4] == '1100'):
            line_ordered += arrage_part[i:i+5]

    i = 0
    for i in range(0, l):
        if (arrage_part[i] == '0111\n' and arrage_part[i+1] == '1011\n' and arrage_part[i+2] == '1101\n' and arrage_part[i+3][:4] == '1110'):
            line_ordered += arrage_part[i:i+5]

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