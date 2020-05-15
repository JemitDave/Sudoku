import json
from collections import OrderedDict
fc=OrderedDict()
pv=OrderedDict()
fc[11]=3            #values entered for simplicity, will be looped later
fc[12]=0
fc[13]=2
fc[14]=9
fc[15]=6
fc[16]=4
fc[17]=8
fc[18]=5
fc[19]=1
fc[21]=9
fc[22]=0
fc[23]=4
fc[24]=8
fc[25]=1
fc[26]=5
fc[27]=0
fc[28]=7
fc[29]=0
fc[31]=0
fc[32]=0
fc[33]=1
fc[34]=3
fc[35]=7
fc[36]=2
fc[37]=0
fc[38]=9
fc[39]=6
fc[41]=0
fc[42]=4
fc[43]=0
fc[44]=1
fc[45]=0
fc[46]=9
fc[47]=0
fc[48]=2
fc[49]=8
fc[51]=1
fc[52]=0
fc[53]=9
fc[54]=0
fc[55]=4
fc[56]=6
fc[57]=0
fc[58]=0
fc[59]=5
fc[61]=5
fc[62]=2
fc[63]=0
fc[64]=7
fc[65]=0
fc[66]=3
fc[67]=0
fc[68]=1
fc[69]=4
fc[71]=2
fc[72]=0
fc[73]=8
fc[74]=6
fc[75]=0
fc[76]=1
fc[77]=5
fc[78]=4
fc[79]=7
fc[81]=4
fc[82]=1
fc[83]=0
fc[84]=0
fc[85]=3
fc[86]=0
fc[87]=2
fc[88]=0
fc[89]=0
fc[91]=0
fc[92]=0
fc[93]=5
fc[94]=0
fc[95]=0
fc[96]=7
fc[97]=1
fc[98]=0
fc[99]=3
for m in range(1,10):              #makes entry in possible values (pv) dictionary
    for n in range(1,10):
        ij=int(str(m)+str(n))
        #fc[ij]=0
        pv[ij]=[1,2,3,4,5,6,7,8,9]
#BLOCK LISTS
b1=[11,12,13,21,22,23,31,32,33]
b2=[14,15,16,24,25,26,34,35,36]
b3=[17,18,19,27,28,29,37,38,39]
b4=[41,42,43,51,52,53,61,62,63]
b5=[44,45,46,54,55,56,64,65,66]
b6=[47,48,49,57,58,59,67,68,69]
b7=[71,72,73,81,82,83,91,92,93]
b8=[74,75,76,84,85,86,94,95,96]
b9=[77,78,79,87,88,89,97,98,99]
block_list=[b1,b2,b3,b4,b5,b6,b7,b8,b9]
counter=dict()
for count in range(1,10):
    counter[count]=0

while True :                #accepting values from question
    inp=input('Would you like to add fc: y/done: ')
    if inp=='done':
        break
    else:
        i=int(input('enter i: '))
        j=int(input('enter j: '))
        val=int(input('enter val: '))
        ij=int(str(i)+str(j))
        fc[ij]= val

for iteration in fc.values():
    if iteration!=0:
        def update():
            for fcell, value in fc.items():  # UPDATES PV WRT FC ie removes all the fc in pv
                if value != 0:
                    if fcell in pv:
                        try:
                            pv.pop(fcell)
                        except KeyError:
                            pass


        def check_row(i, j, value):
            for pcell, value2 in pv.items():
                m = pcell // 10
                n = pcell % 10
                if m == i:
                    try:
                        value2.remove(value)
                    except ValueError:
                        pass


        def check_col(i, j, value):
            for pcell, value2 in pv.items():
                m = pcell // 10
                n = pcell % 10
                if n == j:
                    try:
                        value2.remove(value)
                    except ValueError:
                        pass


        def check_block(fcell, value):              #removes fc value from pv for each block
            for block in block_list:
                for blockcell in block:
                    if blockcell == fcell:
                        for blockcell in block:
                            try:
                                pv[blockcell].remove(value)
                            except:
                                ValueError

        def update2():                              #checks if there is only one instance of any value present and
            for block in block_list:                #puts it as the fc
                for blockcell in block:
                    try:
                        for value in pv[blockcell]:
                            counter[value] += 1
                    except: KeyError

            for key, value in counter.items():
                if value==1:
                    fc[blockcell]=value

        update()
        for fcell, value in fc.items():  # UPDATES ROW AND COL
            if value != 0:
                i = fcell // 10
                j = fcell % 10
                check_row(i, j, value)
                check_col(i, j, value)

        for fcell, value in fc.items():  # UPDATES pv blockwise
            if value != 0:
                check_block(fcell, value)

        newpv = pv.copy()
        for pcell, value2 in newpv.items():
            if len(value2) == 1:
                for ans in value2:
                    fc[pcell] = ans
                    update()
                    update2()


#print(json.dumps(pv, indent=7))
#print(json.dumps(fc, indent=4))

printer=list()                              #printing in sudoku format
for keys,values in fc.items():
    i=keys//10
    j=keys%10
    #print(keys)
    printer.append(values)
    if i==4 and j==9 or i==7 and j==9:
        print('-------------------------------------')
    if len(printer)==9:
        printer.insert(3,'/')
        printer.insert(7,'/')
        print(printer)
        printer.clear()


