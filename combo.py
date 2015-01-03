import csv


a = 'a.csv' #first filename
b = 'b.csv' #second filename
o = 'o.csv' #output file

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
print table.keys()

with open(a) as csvfilea:
    with open(o, 'w') as csvfileo:
        csva = csv.reader(csvfilea)
        csvo = csv.writer(csvfileo)

        #write header row with new headers
        temp = csva.next()
        temp.extend(gradeheader)
        csvo.writerow(temp)

        #write second row without changing
        csvo.writerow(csva.next())

        #append rows
        for row in csva:
            print row[2]
            if row[2] in table:
                row.extend(table[row[2]])
                csvo.writerow(row)
            else:
                for i in xrange(len(gradeheader)):
                    row.extend(0)
                csvo.writerow(row)





