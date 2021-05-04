def find(fileName):
    g0 = 0
    g1 = 0
    alledges = set()
    with open(fileName, 'r') as infile:
        for line in infile:
            if line[0]=='#':
                continue
            line = line.split()
            edge = (line[0], line[1])
            reverseEdge = (line[1], line[0])
            if reverseEdge in alledges:
                g1 += 1
                g0 -= 1
            else:
                alledges.add(edge)
                g0 += 1
    print("G0: " + str(g0), "G1: " + str(g1))


fileName = input("File Name: ")
find(fileName)

