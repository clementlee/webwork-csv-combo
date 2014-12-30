import csv


a = '1.csv' #first filename
b = '2.csv' #second filename
o = '3.csv' #output file

c = 'column1'
idxc = 0 #column index of c
d = 'column2'
idxd = 0 #column index of d

cprime = 'column1'
dprime = 'column2'

table = {} #initialize mapping

with open(b) as csvfileb:
    csvb = csv.DictReader(csvfileb)

    #next, put all c' -> d' mappings into the table
    for row in csvb:
        table[row[cprime]] = row[dprime]

with open(a) as csvfilea:
    csva = csv.reader(csvfilea)

    linestoskip = 7 #number of useless lines
    for i in xrange(linestoskip):
        csva.next()

    #now find column indices again
    temp = csva.next()
    for i in xrange(len(temp)):
        if temp[i] == c:
            idxc = i
        elif temp[i] == d:
            idxd = i

    #open output file
    with open(o) as csvfileo:
        csvo = csv.writer(csvfilea)



