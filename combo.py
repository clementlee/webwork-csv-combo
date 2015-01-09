import csv

#usage: python combo.py a.csv b.csv o.csv

import sys
a = sys.argv[1]
b = sys.argv[2]
o = sys.argv[3]

table = {}
header = None
firstcol = 0
lastcol = 0

with open(b) as csvfileb:
    csvfileb.readline()

    csvb = csv.reader(csvfileb)
    firstcol = 6
    lastcol = firstcol
    header = [i.strip() for i in csvb.next()]
    while header[lastcol] != 'summary':
        lastcol += 1

    for i in xrange(5): #skip header
        csvb.next()

    for row in csvb: #create table list
        grades = []
        for i in xrange(firstcol, lastcol):
            grades.append(row[i])
        table[row[0].strip()] = grades

gradeheader = header[firstcol:lastcol]

with open(a) as csvfilea:
    with open(o, 'w') as csvfileo:
        csva = csv.reader(csvfilea)
        csvo = csv.writer(csvfileo)

        ## addition: modify the headers
        gradeheader = ["webwork " + i for i in gradeheader]

        #write header row with new headers
        temp = csva.next()
        temp = temp[:6]
        temp.extend(gradeheader)
        csvo.writerow(temp)

        #write second row without changing
        temp = csva.next()
        temp = temp[:6]
        for i in xrange(len(gradeheader)):
            temp.extend('')
        csvo.writerow(temp)

        #append rows
        for row in csva:
            row = row[:6]
            if row[2] in table:
                row.extend(table[row[2]])
                csvo.writerow(row)
            else:
                for i in xrange(len(gradeheader)):
                    row.extend(0)
                csvo.writerow(row)





